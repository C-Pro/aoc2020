import re

a = []

with open("input.txt", "rt") as fi:
    lines=fi.read().splitlines()
    for l in lines:
        m = re.match(r"([0-9]+)-([0-9]+) ([a-z]{1}): ([a-z]+)", l)
        a.append((int(m.group(1)),int(m.group(2)),m.group(3),m.group(4))) 


cnt_valid = 0
for x in a:
    try:
        cnt_letter = 0
        if x[3][x[0]-1] == x[2]:
            cnt_letter += 1
        if x[3][x[1]-1] == x[2]:
            cnt_letter += 1
        if cnt_letter == 1:
            cnt_valid +=1
    except:
        print(x)

print(cnt_valid)
