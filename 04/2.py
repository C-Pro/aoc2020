import re

pat = re.compile(r"(\w+):([^\s]+)")

req = set(["byr", "iyr", "eyr", "hgt",
           "hcl", "ecl", "pid"])
# cid


with open("input.txt", "rt") as fi:
    lines = fi.read().splitlines()

    cnt = 0
    psprt = set([])
    fail = False

    for l in lines:
        pos = 0
        while True:
            m = pat.search(l, pos)
            if m == None:
                break
            pos = m.end()
            fld = m.group(1)
            val = m.group(2)

            try:  # handle conversion exceptions
                if fld == "byr":
                    if int(val) < 1920 or int(val) > 2002:
                        fail = True

                if fld == "iyr":
                    if int(val) < 2010 or int(val) > 2020:
                        fail = True

                if fld == "eyr":
                    if int(val) < 2020 or int(val) > 2030:
                        fail = True

                if fld == "hgt":
                    m = re.match("([0-9]{2,3})(cm|in)", val)
                    if m == None:
                        fail = True
                    else:
                        h = int(m.group(1))
                        if m.group(2) == "cm":
                            if h < 150 or h > 193:
                                fail = True
                        if m.group(2) == "in":
                            if h < 59 or h > 76:
                                fail = True

                if fld == "hcl":
                    m = re.fullmatch("#[a-f0-9]{6}", val)
                    if m == None:
                        fail = True

                if fld == "ecl":
                    m = re.fullmatch("amb|blu|brn|gry|grn|hzl|oth", val)
                    if m == None:
                        fail = True

                if fld == "pid":
                    m = re.fullmatch("[0-9]{9}", val)
                    if m == None:
                        fail = True

            except:
                fail = True

            if fail:
                psprt = set([])
                break

            psprt.add(fld)

        if l == "":
            # print(req.difference(psprt))
            if len(req.difference(psprt)) == 0:
                cnt += 1
            psprt = set([])
            fail = False

print(cnt)
