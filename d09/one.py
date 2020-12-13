import sys

filename = "input"
preamble = 25
if len(sys.argv) > 1 and sys.argv[1] == "t":
    filename = "test_input"
    preamble = 5

result = 0
lines = []
with open(filename, "r") as fp:
    for line in fp.readlines():
        lines.append(line)


nums = [-1] * preamble
# Load preamble
for i in range(0, preamble):
    nums[i] = int(lines[i].strip())


for i in range(preamble, len(lines)):
    # Check if valid
    valid = False
    num = int(lines[i])
    for x in nums:
        for y in nums:
            if x != y:
                if x + y == num:
                    valid = True
    if valid == False:
        result = num
        break
    else:
        nums.pop(0)
        nums.append(num)




print(result)


