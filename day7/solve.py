# Read input positions
positions = list(map(int, open("input.txt", "r").read().strip().split(",")))

### Exercise 1 ###
costs = []
for i in range(max(positions)):
    costs.append(0)
    for position in positions:
        costs[i] += abs(position - i)

print("[+] Exercise 1:")
print("\t- Minimal fuel cost:", min(costs))
### ########## ###

print()

### Exercise 2 ###
costs = []
for i in range(max(positions)):
    costs.append(0)
    for position in positions:
        costs[i] += sum(range((abs(position-i)+1)))

print("[+] Exercise 2:")
print("\t- Minimal fuel cost:", min(costs))
### ########## ###