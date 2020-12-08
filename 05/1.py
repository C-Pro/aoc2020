def conv_row(s):
    return int(s.replace("F","0").replace("B","1"), 2)

def conv_col(s):
    return int(s.replace("L","0").replace("R","1"), 2)

assert(conv_row("BFFFBBF") == 70)
assert(conv_row("FFFBBBF") == 14)
assert(conv_row("BBFFBBF") == 102)

assert(conv_col("RRR") == 7)
assert(conv_col("RLL") == 4)

max_id = 0
with open("input.txt", "rt") as fi:
    lines=fi.read().splitlines()

    for l in lines:
        row = conv_row(l[:7])
        col = conv_col(l[7:])
        id = row * 8 + col
        if id > max_id:
            max_id = id


print(max_id)
