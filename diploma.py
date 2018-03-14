import requests
import json
import time

a_token = " "
source_id = " "


def timeout(fn):
    def wrapper(*args):
        try:
            fn
            result = fn(*args)
        except TimeoutError or ConnectionError:
            time.sleep(30)
            timeout(fn)
        return result
    return wrapper


def avoid_too_many_requests(count):
    if count % 3 == 0:
        time.sleep(1)
    return


@timeout
def get_friends(source_user_id, token):
    """
    :param source_user_id: The id of the user you need to get info about.
    :param token: An access token.
    :return: A list of ids belonging to the friends of the targeted user.
    """
    params = {
        "user_id": source_user_id,
        "access_token": token,
        "v": "5.73"
    }

    response = requests.get("https://api.vk.com/method/friends.get", params)
    friends = response.json()["response"]["items"]

    return friends


@timeout
def get_groups(user_id, token):
    """
    :param user_id: The id of the user you need to get info about.
    :param token: An access token.
    :return: A list of group ids that the targeted user is a member of.
    """
    params = {
        "user_id": user_id,
        "access_token": token,
        "v": "5.73"
    }

    response = requests.get("https://api.vk.com/method/groups.get", params)
    groups = response.json()["response"]["items"]

    return groups


@timeout
def get_unique_groups(source_user_id, token):
    """
    Getting groups that the targeted user is the only member of (among user's friends).
    :param source_user_id: The id of the user you need to get info about.
    :param token: An access token.
    :return: A list of group ids.
    """
    friends_list = get_friends(source_user_id, token)  # list of the targeted user's friends
    groups_list = get_groups(source_user_id, token)  # list of groups that the targeted user is a member of
    count = 1
    print("Getting groups of each friend...")
    for friend in friends_list:
        try:
            friend_groups = get_groups(friend, token)
            print("- {} friends left".format(len(friends_list) - count))
            for friend_group in friend_groups:
                if friend_group in groups_list:
                    groups_list.remove(friend_group)
                else:
                    continue
            count += 1
            avoid_too_many_requests(count)
        except KeyError:
            print("- {} friends left".format(len(friends_list) - count))
            count += 1
            avoid_too_many_requests(count)
    print("Collected unique groups.")
    return groups_list


@timeout
def get_friends_groups(source_user_id, token):
    """
    :param source_user_id: The id of the user you need to get info about.
    :param token: An access token.
    :return: A list of sets which include group ids that each friend is a member of.
    """
    friends_list = get_friends(source_user_id, token)  # list of the targeted user's friends
    friends_groups_list = []
    count = 1
    print("Getting groups of each friend...")
    for friend in friends_list:
        try:
            friend_groups = set(get_groups(friend, token))
            friends_groups_list.append(friend_groups)
            print("- {} friends left".format(len(friends_list) - count))
            count += 1
        except KeyError:
            print("- {} friends left".format(len(friends_list) - count))
            count += 1
            continue
    return friends_groups_list


@timeout
def find_common_groups_with_one(source_user_id, token):
    """
    Getting groups that the targeted user and at least one of his/her friends are members of.
    :param source_user_id: The id of the user you need to get info about.
    :param token: An access token.
    :return: A list of group ids.
    """
    groups_list = get_groups(source_user_id, token)  # list of groups that the targeted user is a member of
    friends_groups_list = get_friends_groups(source_user_id, token)  # list of sets with group ids for each friend
    common_with_one = []
    for group in friends_groups_list:
        common_with_each_friend = set(groups_list) & group
        for group_id in common_with_each_friend:
            common_with_one.append(group_id)
    return common_with_one


@timeout
def find_common_groups_with_more(source_user_id, token, friends_number):
    """
    Getting groups that the targeted user and more than one of his/her friends are members of.
    :param source_user_id: The id of the user you need to get info about.
    :param token: An access token.
    :param friends_number: Number of friends with whom the targeted user has common groups.
    :return: A list of group ids.
    """
    common_with_one = find_common_groups_with_one(source_user_id, token)
    common_with_more = []
    for i in common_with_one:
        group_occurrence = common_with_one.count(i)
        if group_occurrence == friends_number and i not in common_with_more:
            common_with_more.append(i)
    return common_with_more


def get_requested_info(group_all_info):
    """
    Making a dictionary with group's required characteristics as keys.
    :param group_all_info: A dictionary with all characteristics of a group collected through "groups.getById" method.
    :return: A dictionary.
    """
    group_requested_info = dict()

    for group in group_all_info:
        group_requested_info["id"] = group["id"]
        group_requested_info["name"] = group["name"]
        group_requested_info["members_count"] = group["members_count"]

    return group_requested_info


@timeout
def get_group_info(group_uid, token):
    """
    Making a dictionary with all characteristics of a group.
    :param group_uid: Group's id.
    :param token: An access token.
    :return: A dictionary.
    """
    params = {
        "group_id": group_uid,
        "access_token": token,
        "v": "5.73",
        "fields": ["name", "id", "members_count"]
    }

    response = requests.get("https://api.vk.com/method/groups.getById", params)
    group_all_info = response.json()["response"]

    group_result_info = get_requested_info(group_all_info)

    return group_result_info


@timeout
def get_specific_groups_info(groups_list, token):
    """
    Getting required info about specific groups.
    :param groups_list: A list of groups.
    :param token: An access token.
    :return: A list of dictionaries.
    """
    specific_groups_info = []
    count = 1
    print("Getting group's info.")
    for group in groups_list:
        try:
            info = get_group_info(group, token)
            print("- {} groups left".format(len(groups_list) - count))
            specific_groups_info.append(info)
            count += 1
            avoid_too_many_requests(count)
        except KeyError:
            print("- {} groups left".format(len(groups_list) - count))
            count += 1
            avoid_too_many_requests(count)

    return specific_groups_info


def write_json(groups_list, token):
    """
    Writing groups' info into json file.
    :param groups_list: A list of dictionaries with groups' info.
    :param token: An access token.
    :return: File "groups.json"
    """
    result_data = get_specific_groups_info(groups_list, token)
    with open("groups.json", "w", encoding="utf-8") as file:
        json.dump(result_data, file, ensure_ascii=False)
    return


def find_groups(source_user_id, token):
    """
       Choosing what groups to search for: unique or common with specific number of friends.
       :param source_user_id: The id of the user you need to get info about.
       :param token: An access token.
       :return: A function
       """
    friends_number = int(input("Enter the number of friends with whom the targeted user"
                               " is expected to have common groups "))
    if friends_number == 0:
        unique_groups = get_unique_groups(source_user_id, token)
        write_json(unique_groups, token)
        return
    elif friends_number == 1:
        common_with_one = find_common_groups_with_one(source_user_id, token)
        write_json(common_with_one, token)
        return
    elif friends_number >= 2:
        common_with_some = find_common_groups_with_more(source_user_id, token, friends_number)
        write_json(common_with_some, token)
        return
    else:
        raise Exception("This is an invalid number. Please try again.")

find_groups(source_id, a_token)
