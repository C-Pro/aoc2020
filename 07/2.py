import re

# drab plum bags contain 5 clear turquoise bags, 5 striped aqua bags, 4 dotted gold bags, 4 plaid chartreuse bags.

pat1 = re.compile(r"([\w\s]+)s? contain")
pat2 = re.compile(r"([0-9]+)?\s?([a-z\s]+)s?(,|\.)")

with open("input.txt", "rt") as fi:
    lines = fi.read().splitlines()

    d = {}
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
                cnt = 1
                if s.group(1):
                    cnt = int(s.group(1))
                b.append((cnt, s.group(2).replace(" bags", " bag")))
                pos = s.end()

        d[key] = b


def cnt_bags(bag):
    children = d[bag]
    s = 1
    if children is None or len(children) == 0:
        return s
    for (n, b) in children:
        #print(n, b)
        s += n * cnt_bags(b)
    return s


# count of bags INSIDE, so minus one shiny gold bag
print(cnt_bags("shiny gold bag")-1)
