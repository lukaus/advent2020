import sys

filename = "input"
if len(sys.argv) > 1 and sys.argv[1] == "t":
    filename = "test_input"

result = 0
lines = []
with open(filename, "r") as fp:
    for line in fp.readlines():
        lines.append(line)


my_adapter = 0
for num in lines:
    num = int(num)
    if num > my_adapter:
        my_adapter = num

sequence = [0]
threes = 0
ones = 0
for a in lines:
    sequence.append( int(a.strip()))

sequence.sort()
sequence.append(my_adapter + 3)

for x in range(len(sequence)-1):
    if sequence[x+1] - sequence[x] == 3:

        threes += 1
    if sequence[x+1] - sequence[x] == 1:
        ones += 1


result = ones * threes
print(result)


