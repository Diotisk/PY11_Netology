import chardet
import collections
from operator import itemgetter

with open("newsit.txt", "rb") as file:
    data = file.read()
    result = chardet.detect(data)
    # print(result)
    a = data.decode(result["encoding"])
    # print(a)

with open("newsfr.txt", "rb") as file:
    data = file.read()
    result = chardet.detect(data)
    # print(result)
    b = data.decode(result["encoding"])
    # print(b)

with open("newscy.txt", "rb") as file:
    data = file.read()
    result = chardet.detect(data)
    # print(result)
    c = data.decode(result["encoding"])
    # print(c)

with open("newsafr.txt", "rb") as file:
    data = file.read()
    result = chardet.detect(data)
    # print(result)
    d = data.decode(result["encoding"])
    # print(d)

text = a + b + c + d
words_list = text.split(" ")

# module collections
frequency = collections.Counter()
for word in words_list:
    if len(word) > 6:
        frequency[word] += 1
print(frequency.most_common(10))

# dictionary
words_frequency = dict()
words_frequency_values = []

for i in words_list:
    if len(i) > 6:
        n = words_list.count(i)
        words_frequency[i] = n

for key, value in words_frequency.items():
    words_frequency_values.append(value)

sorted_values = sorted(words_frequency_values, reverse=True)
# print(sorted_values)
top_ten = sorted_values[:10]

for key, value in words_frequency.items():
    if value in top_ten:
        print(key, value)

# itemgetter
words_frequency_sorted = sorted(words_frequency.items(), key=itemgetter(1), reverse=True)
top_frequency = words_frequency_sorted[:10]
print(top_frequency)
