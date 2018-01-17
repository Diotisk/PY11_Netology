import simplejson as json
import chardet
from pprint import pprint
import collections

news_list = []


#def compose_news_list():

with open("newsafr.json") as newsafr:
    text_newsafr = json.load(newsafr)
    news_list.append(text_newsafr)

with open("newscy.json", "rb") as newscy:
    t_newscy = newscy.read()
    decoded_newscy = chardet.detect(t_newscy)
    print(decoded_newscy)
    result_newscy = t_newscy.decode(decoded_newscy["encoding"])
    # pprint(result_newscy)
    text_newscy = json.loads(result_newscy)
    # pprint(text_newscy)
    news_list.append(text_newscy)

with open("newsfr.json", "rb") as newsfr:
    t_newsfr = newsfr.read()
    decoded_newsfr = chardet.detect(t_newsfr)
    result_newsfr = t_newsfr.decode(decoded_newsfr["encoding"])
    text_newsfr = json.loads(result_newsfr)
    # pprint(text_newsfr)
    news_list.append(text_newsfr)

with open("newsit.json", "rb") as newsit:
    t_newsit = newsit.read()
    decoded_newsit = chardet.detect(t_newsit)
    result_newsit = t_newsit.decode(decoded_newsit["encoding"])
    text_newsit = json.loads(result_newsit)
    # pprint(text_newsit)
    news_list.append(text_newsit)

# pprint(news_list)
all_news = str()

for j in news_list:
    for i in j["rss"]["channel"]["items"]:
        news_text = i["description"]
        all_news += news_text
    # pprint(all_news)
    # pprint(type(all_news))

words_list = all_news.split(" ")

frequency = collections.Counter()
for word in words_list:
    if len(word) > 6:
        frequency[word] += 1
pprint(frequency.most_common(10))
