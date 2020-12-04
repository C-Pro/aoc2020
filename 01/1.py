with open("input.txt", "rt") as fi:
    lines=fi.read().splitlines()
    a = [int(l) for l in lines]

for i in range(len(a)):
    for j in range(i, len(a)):
        if a[i] + a[j] == 2020:
            print(a[i] * a[j])
