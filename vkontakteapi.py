import requests

a_token = "some_token"


def get_friends(source_id, target_ids):  # with access token

    params = {
        "source_uid": source_id,
        "target_uids": target_ids,  # as a list
        "access_token": a_token
    }

    response = requests.get("https://api.vk.com/method/friends.getMutual", params)
    common_friends = response.json()["response"]

    for friend in common_friends:
        url = "https://vk.com/id" + str(friend)
        print(friend, url)

    return


def get_friend(uid):  # without access token
    params = {"user_id": uid}
    response = requests.get("https://api.vk.com/method/friends.get", params)
    friends = response.json()["response"]
    return friends


def get_common_friends(u_ids):
    """
    :argument u_ids requires a list of user_ids
    """
    all_friends_list = []
    common_friends_list = []

    for user in u_ids:
        fr_l = get_friend(user)
        all_friends_list.extend(fr_l)

    for friend in all_friends_list:
        c = all_friends_list.count(friend)
        if c == len(u_ids) and friend not in common_friends_list:
            common_friends_list.append(friend)
        else:
            continue

    for friend_id in common_friends_list:
        url = "https://vk.com/id" + str(friend_id)
        print(friend_id, url)

    return
