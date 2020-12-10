


valid = 0
with open("input", "r") as fp:
    for line in fp.readlines():
        rule, pwd = line.split(':')
        pwd = pwd.strip()
        minmax, char = rule.split(' ')
        minmax = minmax.strip()
        minmax = minmax.split('-')
        char = char.strip()
        count = 0
        for c in pwd:
            if c == char:
                count +=1
        if (pwd[int(minmax[0])-1] == char or pwd[int(minmax[1])-1] == char) and pwd[int(minmax[0])-1] != pwd[int(minmax[1])-1]:
            valid +=1

print (valid)
