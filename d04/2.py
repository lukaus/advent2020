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


ecls = ["amb","blu","brn","gry","grn","hzl","oth"]

result = 0
for line in lines:
    if line.strip() == "":
        result += validate_passport()
    fields = line.split(" ")
    for field in fields:
        field = field.split(":")
        if field[0] == "byr":
            val = int(field[1])
            if val >= 1920 and val <= 2002:
                byr = True

        if field[0] == "iyr":
            val = int(field[1])
            if val >= 2010 and val <= 2020:
                iyr = True

        if field[0] == "eyr":
            val = int(field[1])
            if val >= 2020 and val <= 2030:
                eyr = True

        if field[0] == "hgt":
            val = field[1].strip()
            if val.strip().endswith("in") or val.strip().endswith("cm"):
                if val.endswith("in"):
                    val = int(val.strip().split("in")[0])
                    if val >= 59 and val <= 76:
                        hgt = True
                else:
                    val = int(val.strip().split("cm")[0])
                    if val >= 150 and val <= 193:
                        hgt = True

        if field[0] == "hcl":
            val = field[1]
            if val[0] == "#":
                val = val.split("#")[1].strip()
                if len(val) == 6:
                    for ch in val:
                        ch = ord(ch)
                        if ch >= 48 and ch <= 57 or ch >= 97 and ch <= 102:
                            hcl = True

        if field[0] == "ecl":
            val = field[1].strip()
            if val in ecls:
                ecl = True

        if field[0] == "pid":
            val = field[1].strip()
            if val.isdigit() and len(val) == 9:
                pid = True

result += validate_passport()
print(result)


