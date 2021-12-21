from nltk.tokenize import regexp_tokenize
from nltk.tokenize import WhitespaceTokenizer
f = open(f'/Users/liudawei/PycharmProjects/Text Generator/Text Generator/task/test/corpus.txt', "r", encoding="utf-8")
wt = WhitespaceTokenizer()
words = wt.tokenize(f.read())
print(words)
uniq_words = set()
for x in words:
    uniq_words.add(x)
print("Corpus statistics")
print(f"All tokens: {len(words)}")
print(f"Unique tokens: {len(uniq_words)}")
user_in = input()
while user_in != "exit":
    try:
        n = int(user_in)
    except ValueError:
        print("Type Error. Please input an integer.")
    else:
        if int(n) < len(words):
            print(words[int(n)])
        else:
            print("Index Error. Please input an integer that is in the range of the corpus.")
    user_in = input()
