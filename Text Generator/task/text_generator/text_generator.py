from nltk.tokenize import regexp_tokenize
from nltk.tokenize import WhitespaceTokenizer
from collections import Counter
f = open(f'/Users/liudawei/PycharmProjects/Text Generator/Text Generator/task/{input()}', "r", encoding="utf-8")
wt = WhitespaceTokenizer()
words = wt.tokenize(f.read())

bigrams = []
for x in range(0, len(words) - 1):
    bigrams.append([words[x], words[x + 1]])

uniq_words = set()
for x in words:
    uniq_words.add(x)
# print(uniq_words)
markov_dict = {}
for x in uniq_words:
    for bigram in bigrams:
        if x == bigram[0]:
            markov_dict.setdefault(x, []).append(bigram[1])
print(markov_dict)

def find_tails(head):
    tail_list = markov_dict[head]
    if tail_list is None:
        print("Key Error. The requested word is not in the model. Please input another word.")
    else:
        freq = dict(Counter(tail_list))
        for tail in freq:
            print(f"Tail: {tail}    Count: {freq[tail]}")


user_in = input()
while user_in != "exit":
    find_tails(user_in)
    user_in = input()
