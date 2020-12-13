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

to_find = result
for c in range(0, len(lines)):
    found = False
    total = int(lines[c])
    numbers = [total]
    i = c + 1
    while total < to_find:
        numbers.append(int(lines[i]))
        total += int(lines[i])
        if total == to_find:
            result = numbers
            found = True
            break
        i += 1
    if found:   
        break

minimum = 999999999999
maximum = -1 
for i in result:
    if i < minimum:
        minimum = i
    if i > maximum:
        maximum = i


result = minimum + maximum
print(result)


