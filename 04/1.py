import re

pat = re.compile(r"(\w+):")

req = set(["byr","iyr", "eyr", "hgt",
"hcl","ecl","pid"])
#cid


with open("input.txt", "rt") as fi:
    lines=fi.read().splitlines()

    psprt = set([])
    cnt = 0
    for l in lines:
        ss = pat.findall(l)
        for s in ss:
            psprt.add(s)
        if l == "":
            if len(req.difference(psprt)) == 0:
                cnt += 1
            psprt = set([])


print(cnt)
