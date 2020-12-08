cnt = 0
with open("input.txt", "rt") as fi:
    lines=fi.read().splitlines()
    s = set([])
    for l in lines:
        if len(l) == 0:
            cnt += len(s)
            s = set([])
            continue
        for c in l:
            s.add(c)

print(cnt)
