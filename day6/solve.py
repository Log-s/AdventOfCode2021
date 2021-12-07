### Exercise 1 ###
# Read initial state
fishs = list(map(int, open("input.txt", "r").read().strip().split(",")))

# naive version
for day in range(80):
    new = 0
    for i in range(len(fishs)):
        fishs[i] -= 1
        if fishs[i] == -1:
            fishs[i] = 6
            new +=1
    for i in range(new):
        fishs.append(8)

print("[+] Exercise 1:")
print("\t- Number of fishs:", len(fishs))
### ########## ###

print()

### Exercise 2 ###
# Read initial state
initial_state = list(map(int, open("input.txt", "r").read().strip().split(",")))

# convert to small tab
fishs = [0 for x in range(9)]
for value in initial_state:
    fishs[value] += 1

# Smart version
for day in range(256):
    tmp = [0 for x in range(9)]
    for i in range(8, -1, -1):
        if i == 0:
            tmp[6] += fishs[0]
            tmp[8] += fishs[0]
        tmp[i-1] = fishs[i]
    fishs = tmp

print("[+] Exercise 2:")
print("\t- Number of fishs:", sum(fishs))
### ########## ###