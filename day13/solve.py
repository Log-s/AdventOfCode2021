import copy

# Parse input
c, f = open("input.txt", "r").read().split("\n\n")
coordinates =  [tuple(map(int, x.split(","))) for x in c.split("\n")]
folds = [(x.split('=')[0][-1], int(x.split('=')[1])) for x in f.split("\n")]

# Fill grid
max_x = max([x for x,y in coordinates])
max_y = max([y for x,y in coordinates]) 
grid = [[0] * (max_x+1) for i in range(max_y+1)]

for x,y in coordinates:
    grid[y][x] = 1

save_grid = copy.deepcopy(grid)

### Exercise 1 ##
def fold(direction, line, grid):
    new_grid = None
    match direction:
        case "x":
            # Create new grid
            new_grid = [[0] * (len(grid[0]) - line - 1) for i in range(len(grid))]

            for y in range(len(grid)):
                for x in range(len(grid[0])):
                    # If the fold is in the left part
                    if line <= int(len(grid[0])/2):
                        if x < line:
                            new_grid[y][x] += grid[y][x]
                        elif x > line:
                            new_grid[y][line-x] += grid[y][x]
                    # If the fold is in the right part
                    else:
                        if x < line:
                            new_grid[y][x-line] += grid[y][x]
                        elif x > line:
                            new_grid[y][line-x] += grid[y][x]

        case "y":
            # Create new grid
            new_grid = [[0] * len(grid[0]) for i in range(len(grid) - line - 1)]

            for y in range(len(grid)):
                for x in range(len(grid[0])):
                    # If the fold is in the upper part
                    if line <= int(len(grid)/2):
                        if y < line:
                            new_grid[y][x] += grid[y][x]
                        elif y > line:
                            new_grid[line-y][x] += grid[y][x]
                    # If the fold is in the lower part
                    else:
                        if y < line:
                            new_grid[y-line][x] += grid[y][x]
                        elif y > line:
                            new_grid[line-y][x] += grid[y][x]
    return new_grid

d, l = folds[0]
grid = fold(d, l, grid)

nb_of_points = 0
for line in grid:
    nb_of_points += len([e for e in line if e > 0])
    
print("[+] Exercise 1:")
print("\t- Number of points:", nb_of_points)
### ########## ###



### Exercise 2 ###

# Loop on every fold instruction
grid = save_grid
for d, l in folds:
    grid = fold(d, l, grid)

# Transform 2d array to readable text
passcode = ""
for line in grid:
    passcode += "\n" + "".join(["#" if e > 0 else " " for e in line])

print("[+] Exercise 2:")
print("\t- Passcode:", passcode)
### ########## ###