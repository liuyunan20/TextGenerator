import random
from nltk.tokenize import WhitespaceTokenizer
from collections import Counter
import re

f = open(f'/Users/liudawei/PycharmProjects/Text Generator/Text Generator/task/{input()}', "r", encoding="utf-8")
wt = WhitespaceTokenizer()
words = wt.tokenize(f.read())

markov_dict = {}
for x in range(0, len(words) - 2):
    markov_dict.setdefault(words[x] + ' ' + words[x + 1], []).append(words[x + 2])

for i in range(10):
    prev_word = random.choice(list(markov_dict.keys()))
    head = prev_word.split()
    while re.match('[A-Z]', prev_word) is None or re.search(r'[\.\?\!]$', head[0]):
        prev_word = random.choice(list(markov_dict.keys()))
        head = prev_word.split()
    sentence = [prev_word]
    while True:
        if len(sentence) >= 4 and re.search(r'[\.\?\!]$', sentence[-1]):
            break
        tail_list = markov_dict[prev_word]
        freq = dict(Counter(tail_list))
        cur_word = random.choices(list(freq.keys()), weights=tuple(freq.values()))
        sentence.append(cur_word[0])
        head = prev_word.split()
        prev_word = head[-1] + ' ' + sentence[-1]

    print(" ".join(sentence))
