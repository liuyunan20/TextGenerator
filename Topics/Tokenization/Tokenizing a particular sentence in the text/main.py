from nltk.tokenize import regexp_tokenize
from nltk.tokenize import sent_tokenize
text = input()
sentences = sent_tokenize(text)
n = int(input())
print(regexp_tokenize(sentences[n], "[A-z']+"))
