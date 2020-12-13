import sys

filename = "input"
if len(sys.argv) > 1 and sys.argv[1] == "t":
    filename = "test_input"

lines = []
with open(filename, "r") as fp:
    for line in fp.readlines():
        lines.append(line)

def solve(instructions):
    acc = 0
    visited = [0] * len(instructions)
    i = 0
    while(visited[i] < 1):
        #print(i, end=" ")
        line = instructions[i]
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
        if i >= len(instructions):
            print(acc)
            return


# Permutate
cur_index = 0
for line in lines:
    if line.strip().split(" ")[0] == "jmp":
        to_try = lines.copy()
        to_try[cur_index] = "nop" + " " + line.strip().split(" ")[1] + "\n"
        solve(to_try)
    
    elif line.strip().split(" ")[0] == "nop":
        to_try = lines.copy()
        to_try[cur_index] = "jmp" + " " + line.strip().split(" ")[1] + "\n"
        solve(to_try)
    cur_index += 1




