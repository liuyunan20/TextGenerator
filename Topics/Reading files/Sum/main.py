# read sums.txt
sums = open('sums.txt')
# sums_list = sums.readlines()
for line in sums:
#    line = line.rstrip()
    nums = line.split(' ')
    print(int(nums[0]) + int(nums[1]))
sums.close()
