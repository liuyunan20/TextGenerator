import re

name = input()
if bool(re.match('[B-N][aeiou]', name)):
    print('Suitable!')
