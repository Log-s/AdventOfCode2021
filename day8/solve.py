# parse input
lines = open("input.txt", "r").read().strip().split("\n")
patterns = []
outputs = []
for line in lines:
    s = line.split("|")
    patterns.append(s[0].strip())
    outputs.append(s[1].strip())

### Exercise 1 ###

# Count unique patterns
nb = 0
for output in outputs:
    for display in output.split(" "):
        if len(display) in [2, 3, 4, 7]:
            nb += 1

print("[+] Exercise 1:")
print("\t- Number of 1, 4, 7, 8:", nb)
### ########## ###

print()

### Exercise 2 ###
result = 0
for index in range(len(patterns)):
    numbers = {0: '', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}
    t = patterns[index].split(" ")
    t = ["".join(sorted(x)) for x in t]
    stack_5 = []
    stack_6 = []
    for p in t:
        match len(p):
            case 2:
                numbers[1] = p
            case 3:
                numbers[7] = p    
            case 4:
                numbers[4] = p
            case 5:
                stack_5.append(p)
            case 6:
                stack_6.append(p)
            case 7:
                numbers[8] = p
    
    # Find 6 by checking which length 6 digit doesn't contain all of digit 1
    for e in stack_6:
        if len(set(e).symmetric_difference(set(numbers[1]))) == len(e):
            numbers[6] = e
            stack_6.remove(e)
    
    # Find 3 by checking which length 5 digit contains all of digit 1
    for e in stack_5:
        if len(set(e).symmetric_difference(set(numbers[1]))) == len(e) - len(numbers[1]):
            numbers[3] = e
            stack_5.remove(e)

    # Find the middle segment by looking for the segment that is everywhere except in 1 and 7
    middle = ""
    for l in "abcdefg":
        not_present = []
        if l not in numbers[1] and l not in numbers[7]:
            for e in t:
                if e not in [numbers[1], numbers[7]] and l not in e:
                    not_present.append(e)
        if len(not_present) == 1 and len(not_present[0]) == 6:
            middle = l
    # Use the presence of the middle segment to determine 0 and 9
    #print(middle, stack_6, t)
    for e in stack_6:
        if middle not in e:
            numbers[0] = e
        else:
            numbers[9] = e

    # Find the top right segment -> it's the unused segment in 6
    top_right = ""
    for l in "abcdefg":
        if l not in numbers[6]:
            top_right = l

    # In the two length 5 remaining, the one containing the top right segment is 2, the other one is 5
    for e in stack_5:
        if top_right in e:
            numbers[2] = e
        else:
            numbers[5] = e

    # Read output:
    n = ""
    for digit in outputs[index].split(" "):
        n += str(list(numbers.keys())[list(numbers.values()).index("".join(sorted(digit)))])
    
    result += int(n)

#fgaecd
print("[+] Exercise 2:")
print("\t- Sum of decoded outputs:", result)
### ########## ###