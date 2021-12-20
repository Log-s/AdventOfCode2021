class Octopus:

    flashes = 0

    def __init__(self, grid, x, y):
        self.flashed = False
        self.x = x
        self.y = y
        self.energy = grid[y][x]
        self.neighbours = []
    
    def populate_neighbours(self, grid):
        for y in range(-1, 2):
            for x in range(-1, 2):
                nx, ny = self.x+x, self.y+y
                if (nx != self.x or ny != self.y) and nx >= 0 and ny >= 0 and nx < len(grid[0]) and ny < len(grid):
                    self.neighbours.append(grid[ny][nx])

    def add_energy(self):
        if not self.flashed:
            self.energy += 1
            if self.energy > 9:
                Octopus.flashes += 1
                self.flashed = True
                self.energy = 0
                for n in self.neighbours:
                    n.add_energy()
    
    def unflash(self):
        self.flashed = False

    def __str__(self):
        s = ""
        s += f"Coordinates: {self.x},{self.y}\n"
        s += f"Energy: {self.energy}\tFlashed: {self.flashed}\n"
        s += f"Neighbours: {self.neighbours}\n"
        return s


### Exercise 1 ###
# Read grid
lines = open("input.txt", "r").readlines()
grid_int = []
for line in lines:
    grid_int.append([int(x) for x in line.strip()])

# Create new grid with Octopus objects
grid = []
for y in range(len(grid_int)):
    grid.append([])
    for x in range(len(grid_int[0])):
        grid[y].append(Octopus(grid_int, x, y))
# Populate each Otcopuse's neighbours list
for y in range(len(grid)):
    for x in range(len(grid[0])):
        grid[y][x].populate_neighbours(grid)

for step in range(100):
    # Each turn, increment energy of each object
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            grid[y][x].add_energy()

    # After each turn reset the flashed state
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            grid[y][x].unflash()

print("[+] Exercise 1:")
print("\t- Number of flashes:", Octopus.flashes)
### ########## ###



### Exercise 2 ###

# Create new grid with Octopus objects
grid = []
for y in range(len(grid_int)):
    grid.append([])
    for x in range(len(grid_int[0])):
        grid[y].append(Octopus(grid_int, x, y))
# Populate each Otcopuse's neighbours list
for y in range(len(grid)):
    for x in range(len(grid[0])):
        grid[y][x].populate_neighbours(grid)

is_synchronized = False
step = 0
while not is_synchronized:
    # Each turn, increment energy of each object
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            grid[y][x].add_energy()

    # After each turn reset the flashed state
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            grid[y][x].unflash()
    
    # Check if each element is synchronized at 0
    is_synchronized = True
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x].energy != 0:
                is_synchronized = False
    
    step += 1


print("[+] Exercise 2:")
print("\t- First synchronized step:", step)
### ########## ###