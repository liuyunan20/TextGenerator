# put your python code here
i = int(input())
nums = []
while i <= 100:
    if i >= 10:
        nums.append(i)
    i = int(input())

for x in nums:
    print(x)
