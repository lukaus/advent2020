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
deg = 90

for line in lines:
    ins = line[0]
    amt = int(line[1:])
    if ins == "N" or ins == "F" and deg % 360 == 0:
        ns -= amt
    if ins == "S" or ins == "F" and deg % 360 == 180:
        ns += amt
    if ins == "E" or ins == "F" and deg % 360 == 90:
        ew += amt
    if ins == "W" or ins == "F" and deg % 360 == 270:
        ew -= amt

    if ins == "L":
        deg -= amt
    if ins == "R":
        deg += amt


result = abs(ns) + abs(ew)
print(result)


