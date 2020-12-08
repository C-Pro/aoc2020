import re

# drab plum bags contain 5 clear turquoise bags, 5 striped aqua bags, 4 dotted gold bags, 4 plaid chartreuse bags.

pat1 = re.compile(r"([\w\s]+)s? contain")
pat2 = re.compile(r"([0-9]+)?\s?([a-z\s]+)s?(,|\.)")

with open("input.txt", "rt") as fi:
    lines = fi.read().splitlines()

    d = {}
    cnt = 0
    for l in lines:
        b = []
        m = pat1.match(l)
        key = m.group(1).replace(" bags", " bag")

        if not l.endswith("contain no other bags."):
            pos = m.end()

            while True:
                s = pat2.search(l, pos)
                if s == None:
                    break
                b.append(s.group(2).replace(" bags", " bag"))
                pos = s.end()

        d[key] = b


def get_parents(children):
    ret = set([])
    for c in children:
        for k, v in d.items():
            if c in v:
                ret.add(k)
    if len(ret) == 0:
        return []
    return get_parents(list(ret)) + list(ret)


print(len(set(get_parents(["shiny gold bag"]))))
