from collections import Counter
str_in = input()
word_list = str_in.lower().split()
word_counter = Counter(word_list)
print(sorted(word_counter.elements()))
