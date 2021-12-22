from nltk.tokenize import regexp_tokenize
from nltk.tokenize import WhitespaceTokenizer
from collections import Counter
f = open(f'/Users/liudawei/PycharmProjects/Text Generator/Text Generator/task/{input()}', "r", encoding="utf-8")
wt = WhitespaceTokenizer()
words = wt.tokenize(f.read())


markov_dict = {}
for x in range(0, len(words) - 1):
    markov_dict.setdefault(words[x], []).append(words[x + 1])
# print(markov_dict)


def find_tails(head):
    try:
        tail_list = markov_dict[head]
    except KeyError:
        print("Key Error. The requested word is not in the model. Please input another word.")
    else:
        freq = dict(Counter(tail_list))
        for tail in freq:
            print(f"Tail: {tail}    Count: {freq[tail]}")


user_in = input()
while user_in != "exit":
    print(f"Head: {user_in}")
    find_tails(user_in)
    user_in = input()
