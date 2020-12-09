import re

TARGET=57195069

with open("input.txt", "rt") as fi:
    lines = fi.read().splitlines()

    pos = 0
    while pos < len(lines):
        sum = 0
        nmin = TARGET
        nmax = 0
        offset=0
        while sum < TARGET:
            num=int(lines[pos+offset])
            sum+=num
            if num > nmax:
                nmax = num
            if num < nmin:
                nmin = num
            offset += 1
        if sum == TARGET:
            print(nmax+nmin)
            exit()
        pos += 1

print("not found")
