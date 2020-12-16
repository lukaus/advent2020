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
for a in lines:
    sequence.append( int(a.strip()))

sequence.sort()
sequence.append(my_adapter + 3)
# Sequence now contains 0 ... sorted others ... Max + 3

# I guess I'll make a queue that does a DFS down to the final adapter, then multiplies by the number of posible next adapters on the way out

def dfs(val, seq):
    me = 0
    if val + 1 in seq:
        me += 1
        me *= dfs(val+1, seq)

    if val + 2 in seq:
        me += 1
        me *= dfs(val+2, seq)

    if val + 3 in seq:
        me += 1
        me *= dfs(val+3, seq)

    print(f"{val} has possible {me}")
    return max(me, 1)

result = dfs(0, sequence)



print(result)



