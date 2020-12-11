import sys

filename = "input"
if len(sys.argv) > 1 and sys.argv[1] == "t":
    filename = "test_input"

result = "NYE"
lines = []
with open(filename, "r") as fp:
    for line in fp.readlines():
        lines.append(line.strip())

slopes = [[1,1],[3,1],[5,1],[7, 1],[1,2]]
tree_count = []
for i in range(len(slopes)):
    row = col = 0
    tree_count.append(0)
    for line in lines:
        char = line[col % len(line)]
        print(f"{slopes[i]}: row {row} col {col}; {row % slopes[i][1]} : {char}")
        if row % slopes[i][1] == 0:
            if char == "#":
                tree_count[i] += 1
            col += slopes[i][0]
        row += 1

result = 1
print(tree_count)
for trees in tree_count:
    result = result * trees
print(result)


