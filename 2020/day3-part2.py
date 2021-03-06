# https://adventofcode.com/2020/day/3
with open("day3-input.txt", "r") as f:
    map = f.read().splitlines()

# Generate vertical array where each item on each line gets added
map_data = {}
v = 0
for item in map:
    h = 0
    for i in item:
        map_data.setdefault(v, {})[h] = i
        h += 1
    v += 1

def trees(right, down):
    d = down
    r = right
    trees = 0
    while d < 323:
        if r > 30:
            r = r - 31
        if map_data[d][r] == "#":
            trees += 1
        r += right
        d += down

    return trees


print(trees(1, 1) * trees(3, 1) * trees(5, 1) * trees(7, 1) * trees(1, 2))
