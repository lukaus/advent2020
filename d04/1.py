import sys

filename = "input"
if len(sys.argv) > 1 and sys.argv[1] == "t":
    filename = "test_input"

result = -1
lines = []
with open(filename, "r") as fp:
    for line in fp.readlines():
        lines.append(line)

byr = iyr = eyr = hgt = hcl = ecl = pid = False


def validate_passport():
    global byr, iyr, eyr, hgt, hcl, ecl, pid
    valid = False
    if (byr and iyr and eyr and hgt and hcl and ecl and pid) == True:
        valid = True
    byr = iyr = eyr = hgt = hcl = ecl = pid = False
    if valid:
        return 1 
    return 0


result = 0
for line in lines:
    if line.strip() == "":
        result += validate_passport()
    fields = line.split(" ")
    for field in fields:
        field = field.split(":")
        if field[0] == "byr":
            byr = True
        if field[0] == "iyr":
            iyr = True
        if field[0] == "eyr":
            eyr = True
        if field[0] == "hgt":
            hgt = True
        if field[0] == "hcl":
            hcl = True
        if field[0] == "ecl":
            ecl = True
        if field[0] == "pid":
            pid = True

result += validate_passport()
print(result)


