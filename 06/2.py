from collections import Counter
cnt = 0
with open("input.txt", "rt") as fi:
    lines=fi.read().splitlines()
    s = Counter()
    nump = 0
    for l in lines:
        if len(l) == 0:
            for c, n in s.items():
                if n == nump:
                    cnt += 1
            s = Counter()
            nump=0
            continue
        for c in l:
            s.update(c)
        nump += 1

print(cnt)
