import sys

filename = "input"
if len(sys.argv) > 1 and sys.argv[1] == "t":
    filename = "test_input"

result = 1
lines = []
with open(filename, "r") as fp:
    for line in fp.readlines():
        lines.append(line)



# Build bag rules
bag_rules = {}
for line in lines:
    line = line.split(" contain ")
    color = line[0].split(" bags")[0]
    bag_rules[color] = {"color": [], "num": []}
    holds = line[1].strip().split(", ")
    if holds[0] != "no other bags.":
        for h in holds:
            rule = h.split(" bag")[0].split(" ")
            a = rule[0]
            b = " ".join(rule[1:])
            bag_rules[color]["color"].append(b)
            bag_rules[color]["num"].append(a)


# Bag type to find
mybag = "shiny gold"

# Find the total bags within mybag (dfs again?)
def dfs(rules, color, number):
    total = 1
    for i in range(len(rules[color]["color"])):
        total += dfs(rules, rules[color]["color"][i], int(rules[color]["num"][i]))
    return number * total 

result = dfs(bag_rules, mybag, 1)
    
print(result-1) # subtract original bag
