import re


with open("input.txt", "rt") as fi:
    lines = fi.read().splitlines()

    acc = 0
    pos = 0
    visits = [0]*len(lines)

    while visits[pos] == 0:
        cmd, arg = lines[pos].split()
        visits[pos] += 1
        if cmd == "nop":
            None
        elif cmd == "jmp":
            pos += int(arg)
            continue
        elif cmd == "acc":
            acc += int(arg)
        pos += 1

    print(acc)
