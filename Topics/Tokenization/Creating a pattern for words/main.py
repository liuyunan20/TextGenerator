from nltk.tokenize import regexp_tokenize
text = input()
words = regexp_tokenize(text, '[A-z]+')
n = int(input())
print(words[n])
