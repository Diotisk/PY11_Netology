import simplejson as json
import chardet
from pprint import pprint
import collections
import os

cwd = os.getcwd()


def search_file(current_dir, extension):
    searched_files = []
    for file in os.listdir(current_dir):
        i = os.path.splitext(file)
        if extension in i:
            searched_files.append(file)
    print("All {} files:".format(extension), searched_files)
    return searched_files

json_files = search_file(os.getcwd(), ".json")


def read_file(filename):
    with open(filename) as file:
        content = json.load(file)
    # pprint(content)
    return content


def decode_json(filename):
    with open(filename, "rb") as file:
        content = file.read()
        decoded_content = chardet.detect(content)
        # pprint(decoded_content)
        result_content = content.decode(decoded_content["encoding"])
        # pprint(result_content)
        text = json.loads(result_content)
        # pprint(text)
    return text


def most_common_words(content_type):
    content = content_type
    all_news = str()
    for i in content["rss"]["channel"]["items"]:
        news_text = str(i["description"])
        all_news += news_text
    # pprint(all_news)
    words_list = all_news.split(" ")
    frequency = collections.Counter()
    for word in words_list:
        if len(word) > 6:
            frequency[word] += 1
    pprint(frequency.most_common(10))
    return

for q in json_files:
    try:
        content_utf8 = read_file(q)
        print(q, "utf-8")
        most_common_words(content_utf8)
    except UnicodeDecodeError:
        print(q, "Needed decoding")
        decoded_text = decode_json(q)
        most_common_words(decoded_text)
