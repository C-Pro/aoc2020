import re



with open("input.txt", "rt") as fi:
    lines = fi.read().splitlines()

    pos = 25

    while pos < len(lines):
        num = int(lines[pos])
        found = False
        for i in range(pos - 25, pos-1):
            for j in range(i+1, pos):
                if int(lines[i]) + int(lines[j]) == num:
                    found = True
                    break
        if not found:
            print(num)
            exit()
        pos += 1
