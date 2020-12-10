

nums = []
with open('1.in', 'r') as fp:
    for line in fp.readlines():
        nums.append(int(line))

for num in nums:
    for x in nums:
        for y in nums:
            if num + x + y == 2020:
                print(num*x*y)

