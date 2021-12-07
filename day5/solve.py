def parseCoordinates(i):
    tmp = i.split(" -> ")
    start = tuple(list(map(int, tmp[0].split(','))))
    end = tuple(list(map(int, tmp[1].split(','))))
    return (start, end)

# parse input
toParse = [x.strip() for x in open("input.txt", "r").readlines()]
coords = list(map(parseCoordinates, toParse))


def constructGrid(coords):
    # Get max X and Y
    x_max = 0
    y_max = 0
    for coord in coords:
        for x,y in coord:
            if x > x_max:
                x_max = x
            if y > y_max:
                y_max = y
    # Create grid and fill with "0"
    return [[0 for x in range(x_max+1)] for y in range(y_max+1)]


### Exercise 1 ###
# Construct empty grid
grid = constructGrid(coords)
# Fill grid with lines
for coord in coords:
    x1, y1, x2, y2 = coord[0][0], coord[0][1], coord[1][0], coord[1][1]
    # Column
    if x1 == x2:
        sign = 1 if y2-y1 > 0 else -1
        for y in range(y1, y2+1 if sign == 1 else y2-1, sign):
            grid[y][x1] += 1
    # Line
    if y1 == y2:
        sign = 1 if x2-x1 > 0 else -1
        for x in range(x1,  x2+1 if sign == 1 else x2-1, sign):
            grid[y1][x] += 1
# Count line overlaps
overlaps = 0
for line in grid:
    for element in line:
        if element >= 2:
            overlaps += 1
print("[+] Exercise 1:")
print("\t- Number of overlaps:", overlaps)
### ########## ###

print()

### Exercise 2 ###
# Construct empty grid
grid = constructGrid(coords)

# Count line overlaps
overlaps = 0
for line in grid:
    for element in line:
        if element >= 2:
            overlaps += 1
print("[+] Exercise 2:")
print("\t- Number of overlaps:", overlaps)
### ########## ###