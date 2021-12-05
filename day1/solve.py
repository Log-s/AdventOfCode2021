# Load inputs
depths = [int(x) for x in open("input.txt", "r").readlines()]


### Exercise 1 ###
increases = 0

for i in range(1, len(depths)):
    if depths[i] > depths[i-1]:
        increases += 1

print("[+] Exercise 1:",increases)
### ########## ###

print()

### Exercise 1 ###
increases = 0
last = sum([depths[0], depths[1], depths[2]])

for i in range(1, len(depths)-2):
    s = sum([depths[i], depths[i+1], depths[i+2]])
    if s > last:
        increases += 1
    last = s

print("[+] Exercise 2:",increases)
### ########## ###