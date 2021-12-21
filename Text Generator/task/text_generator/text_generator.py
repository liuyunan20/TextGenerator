from nltk.tokenize import regexp_tokenize
from nltk.tokenize import WhitespaceTokenizer
f = open(f'/Users/liudawei/PycharmProjects/Text Generator/Text Generator/task/{input()}', "r", encoding="utf-8")
wt = WhitespaceTokenizer()
words = wt.tokenize(f.read())
bigrams = []
for x in range(0, len(words) - 1):
    bigrams.append([words[x], words[x + 1]])

print(f"Number of bigrams: {len(bigrams)}")

user_in = input()
while user_in != "exit":
    try:
        n = int(user_in)
    except ValueError:
        print("Type Error. Please input an integer.")
    else:
        if int(n) < len(bigrams):
            print(f"Head: {bigrams[int(n)][0]} Tail: {bigrams[int(n)][1]}")
        else:
            print("Index Error. Please input an integer that is in the range of the corpus.")
    user_in = input()
