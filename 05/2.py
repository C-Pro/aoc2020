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
min_id = 100500
seats = set({})
with open("input.txt", "rt") as fi:
    lines=fi.read().splitlines()

    for l in lines:
        row = conv_row(l[:7])
        col = conv_col(l[7:])
        id = row * 8 + col
        if id > max_id:
            max_id = id
        if id < min_id:
            min_id = id
        seats.add(id)

for i in range(min_id, max_id):
    if i not in seats:
        print(i)
        exit(0)

print("not found")
exit(1)
