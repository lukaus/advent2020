import sys

filename = "input"
if len(sys.argv) > 1 and sys.argv[1] == "t":
    filename = "test_input"

result = 0
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
bag_types = set()
bag_types.add("shiny gold")

# Find all bag types that eventually contain mybag
def dfs(rules, color, to_find, found):
    for c in rules[color]["color"]:
        dfs(rules, c, to_find, found)
        if c in found:
            found.add(color)
    if to_find in rules[color]["color"]:
        found.add(color)

        

for color in bag_rules.keys():
    dfs(bag_rules, color, mybag, bag_types)


result = len(bag_types)-1
print(result)
