import random
from nltk.tokenize import WhitespaceTokenizer
from collections import Counter
f = open(f'/Users/liudawei/PycharmProjects/Text Generator/Text Generator/task/{input()}', "r", encoding="utf-8")
wt = WhitespaceTokenizer()
words = wt.tokenize(f.read())

markov_dict = {}
for x in range(0, len(words) - 1):
    markov_dict.setdefault(words[x], []).append(words[x + 1])

for i in range(10):
    prev_word = random.choice(words)
    sentence = [prev_word]
    for n in range(9):
        tail_list = markov_dict[prev_word]
        freq = dict(Counter(tail_list))
        cur_word = random.choices(list(freq.keys()), weights=tuple(freq.values()))
        sentence.append(cur_word[0])
        prev_word = cur_word[0]
    print(" ".join(sentence))
