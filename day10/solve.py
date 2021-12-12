# Read all lines
lines = [x.strip() for x in open("input.txt", "r").readlines()]

### Exercise 1 ###
openers = "([{<"
closers = ")]}>"
points = [3, 57, 1197, 25137]
score = 0
for line in lines:
    opened = []
    for char in line:
        if char in openers:
            opened.append(char)
        else:
            if opened[-1] != openers[closers.index(char)]:
                # Illegal char
                score += points[closers.index(char)]
                break
            else:
                opened.pop()

print("[+] Exercise 1:")
print("\t- Score:", score)
### ########## ###

print()

### Exercise 2 ###
openers = "([{<"
closers = ")]}>"
scores = []
for line in lines:
    opened = []
    illegal = False
    for char in line:
        if char in openers:
            opened.append(char)
        else:
            if opened[-1] != openers[closers.index(char)]:
                # Illegal char
                illegal = True
                break
            else:
                opened.pop()
    if not illegal:
        scores.append(0)
        while len(opened) > 0:
            scores[-1] = scores[-1] * 5 + openers.index(opened[-1]) + 1
            opened.pop()

scores.sort()
score = scores[int(len(scores)/2)]

print("[+] Exercise 2:")
print("\t- Middle score:", score)
### ########## ###