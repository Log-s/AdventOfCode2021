# parse input
to_parse = open("input.txt", "r").readlines()
grid = []
for line in to_parse:
    grid.append([int(x) for x in line.strip()])

### Exercise 1 ###
# Detect low points
low_points = []
for y in range(len(grid)):
    for x in range(len(grid[0])):
        is_min = True
        if x > 0 and grid[y][x-1] <= grid[y][x]:
            is_min = False
        if x < len(grid[0])-1 and grid[y][x+1] <= grid[y][x]:
            is_min = False
        if y > 0 and grid[y-1][x] <= grid[y][x]:
            is_min = False
        if y < len(grid)-1 and grid[y+1][x] <= grid[y][x]:
            is_min = False
        if is_min:
            low_points.append((x, y))

# Count dangerosity
s = 0
for point in low_points:
    s += grid[point[1]][point[0]] + 1

print("[+] Exercise 1:")
print("\t- Dangerosity of low points:", s)
### ########## ###

print()

### Exercise 2 ###
def count_bassin_size(start_point, bassin):
    x = start_point[0]
    y = start_point[1]
    bassin.append(start_point)
    if x > 0 and grid[y][x-1] > grid[y][x] and grid[y][x-1] != 9 and (x-1, y) not in bassin:
        count_bassin_size((x-1, y), bassin)
    if x < len(grid[0])-1 and grid[y][x+1] > grid[y][x] and grid[y][x+1] != 9 and (x+1, y) not in bassin:
        count_bassin_size((x+1, y), bassin)
    if y > 0 and grid[y-1][x] > grid[y][x] and grid[y-1][x] != 9 and (x, y-1) not in bassin:
        count_bassin_size((x, y-1), bassin)
    if y < len(grid)-1 and grid[y+1][x] > grid[y][x] and grid[y+1][x] != 9 and (x, y+1) not in bassin:
        count_bassin_size((x, y+1), bassin)
    return len(bassin)

# Get all sizes
sizes = []
for point in low_points:
    sizes.append(count_bassin_size(point, []))

# Get three largest
sizes.sort()
result = sizes[-1] * sizes[-2] * sizes[-3]

print("[+] Exercise 2:")
print("\t- Size of the three largest bassins:", result)
### ########## ###