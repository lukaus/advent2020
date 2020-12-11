import sys

filename = "input"
if len(sys.argv) > 1 and sys.argv[1] == "t":
    filename = "test_input"

result = -1
lines = []
with open(filename, "r") as fp:
    for line in fp.readlines():
        lines.append(line)






print(result)


