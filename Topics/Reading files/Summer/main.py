#  write your code here
my_file = open('./data/dataset/input.txt', 'r')
i = 0
words = my_file.readlines()
for word in words:
    if word == 'summer\n':
        i += 1
print(i)

