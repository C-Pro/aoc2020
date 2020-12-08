import re


with open("input.txt", "rt") as fi:
    lines = fi.read().splitlines()

    for i in range(len(lines)):

        acc = 0
        pos = 0
        visits = [0]*len(lines)
        cnt = 0

        while visits[pos] == 0:
            cmd, arg = lines[pos].split()
            if cmd in ("nop", "jmp"):
                if cnt == i:
                    if cmd == "nop":
                        cmd = "jmp"
                    else:
                        cmd = "nop"
                cnt += 1
            visits[pos] += 1
            if cmd == "nop":
                pos += 1
            elif cmd == "jmp":
                pos += int(arg)
            elif cmd == "acc":
                acc += int(arg)
                pos += 1

            if pos == len(lines):
                print(acc)
                break
