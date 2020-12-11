import sys

filename = "input"
if len(sys.argv) > 1 and sys.argv[1] == "t":
    filename = "test_input"

result = 0
lines = []
with open(filename, "r") as fp:
    for line in fp.readlines():
        lines.append(line)


ans = [0]*26
for line in lines:
    line = line.strip()
    if line == "":
        total = 0
        for i in range(len(ans)):
            if ans[i] == 1:
                total += 1
            ans[i] = 0
        result += total

    for char in line:
        idx = ord(char) - 97
        ans[idx] = 1

total = 0
for i in range(len(ans)):
    if ans[i] == 1:
        total += 1
    ans[i] = 0
result += total








print(f"{result}")


