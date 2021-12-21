# read sums.txt
sums = open('sums.txt')
for line in sums:
    nums = line.split(' ')
    print(int(nums[0]) + int(nums[1]))
sums.close()
