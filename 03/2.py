
cnt_tree = [0,0,0,0,0]

with open("input.txt", "rt") as fi:
    lines=fi.read().splitlines()
    linelen = len(lines[0])
    height = len(lines)

def cnt(ix, iy, lines, linelen):
    posx=0
    posy=0
    cnt_tree = 0
    for l in lines:
        ch = l[posx % linelen]
        if ch == "#":
            cnt_tree += 1
        posx +=ix
        posy +=iy
    return cnt_tree
with open("input.txt", "rt") as fi:
    lines=fi.read().splitlines()
    linelen = len(lines[0])
    height = len(lines)

def cnt(ix, iy, lines, linelen):
    posx=0
    posy=0
    cnt_tree = 0
    for i, l in enumerate(lines):
        if iy == 2 and i % 2 == 1:
            continue
        ch = l[posx % linelen]
        if ch == "#":
            cnt_tree += 1
        posx +=ix
        posy +=iy
    return cnt_tree


print(
    cnt(1,1, lines, linelen) *
    cnt(3,1, lines, linelen) *
    cnt(5,1, lines, linelen) *
    cnt(7,1, lines, linelen) *
    cnt(1,2, lines, linelen)
    )
