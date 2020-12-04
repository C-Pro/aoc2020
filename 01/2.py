with open("input.txt", "rt") as fi:
    lines=fi.read().splitlines()
    a = [int(l) for l in lines]
    a = sorted(a)

for i in range(len(a)):
    for j in range(i, len(a)):
        if a[i]+a[j] > 2020:
            break
        for k in range(j, len(a)):
            v = a[i] + a[j] + a[k]
            if v > 2020:
                break
            if v == 2020:
                print(a[i] * a[j] * a[k])
