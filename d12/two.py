import sys

filename = "input"
if len(sys.argv) > 1 and sys.argv[1] == "t":
    filename = "test_input"

result = 0
lines = []
with open(filename, "r") as fp:
    for line in fp.readlines():
        lines.append(line)

ew = 0
ns= 0
waypoint = [10, -1] # ew ns
quadrant = 1

for line in lines:
    ins = line[0]
    amt = int(line[1:])
    if ins == "N":
        waypoint[1] -= amt
    if ins == "S":
        waypoint[1] += amt
    if ins == "E":
        waypoint[0] += amt
    if ins == "W":
        waypoint[0] -= amt


    if ins == "R":
        while amt > 0:
            swap = waypoint[0]
            waypoint[0] = -1 * waypoint[1]
            waypoint[1] = swap
            amt -= 90

    
    if ins == "L":
        while amt > 0:
            swap = waypoint[0]
            waypoint[0] = waypoint[1]
            waypoint[1] = -1 * swap

            amt -= 90


    if ins == "F":
        ew += (amt * waypoint[0])#ew
        ns += (amt * waypoint[1])#ns


result = abs(ns) + abs(ew)
print(result)


