import chardet
import collections
# from operator import itemgetter

# #1
def read_file(x):
    with open(x, "rb") as file:
        data = file.read()
        result = chardet.detect(data)
        # print(result)
        end_file = data.decode(result["encoding"])
        # print(end_file)
    return end_file


def most_common_words():
    i = read_file(filename)
    words_list = i.split(" ")
    frequency = collections.Counter()
    for word in words_list:
        if len(word) > 6:
            frequency[word] += 1
    print("Most common words in the file {} are:".format(filename), frequency.most_common(10))
    return

files = ["newsit.txt", "newsfr.txt", "newscy.txt", "newsafr.txt"]
for filename in files:
    most_common_words()


# #2 with common words and stems

def common_in_files():
    files = ["newsit.txt", "newsfr.txt", "newscy.txt", "newsafr.txt"]
    for i in files:
        with open(i, "rb") as file:
            data = file.read()
            result = chardet.detect(data)
            # print(result)
            end_file = data.decode(result["encoding"])
            # print(end_file)

        def most_common_stems():
            words_list = end_file.split(" ")
            frequency = collections.Counter()
            for word in words_list:
                if len(word) > 6:
                    frequency[word.lower()[:-2]] += 1
            print("Most common stems in the file {} are:".format(i), frequency.most_common(10))
            return

        def most_common_words():
            words_list = end_file.split(" ")
            frequency = collections.Counter()
            for word in words_list:
                if len(word) > 6:
                    frequency[word] += 1
            print("Most common words in the file {} are:".format(i), frequency.most_common(10))
            return

        most_common_stems()
        most_common_words()
    return

common_in_files()

# # dictionary
# words_frequency = dict()
# words_frequency_values = []
#
# for i in words_list:
#     if len(i) > 6:
#         n = words_list.count(i)
#         words_frequency[i] = n
#
# for key, value in words_frequency.items():
#     words_frequency_values.append(value)
#
# sorted_values = sorted(words_frequency_values, reverse=True)
# # print(sorted_values)
# top_ten = sorted_values[:10]
#
# for key, value in words_frequency.items():
#     if value in top_ten:
#         print(key, value)
#
# # itemgetter
# words_frequency_sorted = sorted(words_frequency.items(), key=itemgetter(1), reverse=True)
# top_frequency = words_frequency_sorted[:10]
# print(top_frequency)
