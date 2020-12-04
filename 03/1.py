with open("input.txt", "rt") as fi:
    lines=fi.read().splitlines()
    linelen = len(lines[0])
    height = len(lines)
    posx=0
    posy=0
    cnt_tree = 0
    for l in lines:
        ch = l[posx % linelen]
        if ch == "#":
            cnt_tree += 1
        posx +=3
        posy +=1


print(cnt_tree)
