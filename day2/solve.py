# Load inputs
instructions = [x.split(" ") for x in open("input.txt", "r").readlines()]


### Exercise 1 ###
h = d = 0
for i in instructions:
    match i[0]:
        case "forward": h += int(i[1])
        case "down" : d += int(i[1])
        case "up" : d -= int(i[1])
    

print("[+] Exercise 1:")
print("\t- horizontal:", h)
print("\t- depth:", d)
print("\t- anwser:", d*h)
### ########## ###

print()

### Exercise 2 ###
h = d = a = 0
for i in instructions:
    match i[0]:
        case "forward":
            h += int(i[1])
            d += a * int(i[1])
        case "down" : a += int(i[1])
        case "up" : a -= int(i[1])
    

print("[+] Exercise 2:")
print("\t- horizontal:", h)
print("\t- depth:", d)
print("\t- anwser:", d*h)
### ########## ###
