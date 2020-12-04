import re

a = []

with open("input.txt", "rt") as fi:
    lines=fi.read().splitlines()
    for l in lines:
        m = re.match(r"([0-9]+)-([0-9]+) ([a-z]{1}): ([a-z]+)", l)
        a.append((int(m.group(1)),int(m.group(2)),m.group(3),m.group(4))) 


cnt_valid = 0
for x in a:
    cnt_letter = 0
    for i in range(len(x[3])):
        if x[3][i] == x[2]:
            cnt_letter += 1
    if cnt_letter >= x[0] and cnt_letter <= x[1]:
        cnt_valid +=1

print(cnt_valid)
