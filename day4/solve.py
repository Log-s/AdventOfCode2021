inputs = open("input.txt", "r").read().split("\n\n")

# Load "random" inputs
randoms = list(map(int, inputs[0].split(",")))

# Load the grids
grids = []
for i in range(1, len(inputs)):
    parsed = [[] for x in range(5)]
    for i, n in enumerate([x for x in inputs[i].replace("\n", " ").split(" ") if x]):
        parsed[i//5].append(int(n))
    grids.append(parsed)
    
def mark(grid, number):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == number:
                grid[y][x] = -1

def isWon(grid):
    for line in grid:
        if sum(line) == -5:
            return True
    for i in range(5):
        if sum([x[i] for x in grid]) == -5:
            return True
    return False

def calculateScore(grid, number):
    s = 0
    for line in grid:
        for element in line:
            if element != -1:
                s += element
    return s * number


### Exercise 1 ###
won = False
for random in randoms:
    for grid in grids:
        mark(grid, random)
        if isWon(grid):
            score = calculateScore(grid, random)
            won = True
            break
    if won:
        break

print("[+] Exercise 1:")
print("\t- score:", score)
### ########## ###

print()

### Exercise 2 ###
won = False
solved = []
for random in randoms:
    for grid in grids:
        mark(grid, random)
        if isWon(grid) and grid not in solved:
            solved.append(grid)
            if len(solved) - len(grids) == 0:
                score = calculateScore(grid, random)
                won = True

print("[+] Exercise 2:")
print("\t- score:", score)
### ########## ###