


result = "NYE"
lines = []
with open("input", "r") as fp:
    for line in fp.readlines():
        lines.append(line.strip())


col = result =0
for line in lines:
    if line[col % len(line)] == "#":
        result += 1
    col += 3

print(result)


