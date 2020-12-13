import sys

filename = "input"
if len(sys.argv) > 1 and sys.argv[1] == "t":
    filename = "test_input"

lines = []
with open(filename, "r") as fp:
    for line in fp.readlines():
        lines.append(line)

acc = 0
visited = [0] * len(lines)

i = 0
while(visited[i] < 1):
    line = lines[i]
    visited[i] += 1
    ins = line.strip().split(" ")[0]
    amt = int(line.strip().split(" ")[1])
    if ins == "acc":
        acc += amt
        i += 1
    elif ins == "jmp":
        i += amt
    else:
        i += 1




print(acc)


