import copy


# Load inputs
binaries = [x.strip() for x in open("input.txt", "r").readlines()]


### Exercise 1 ###
gamma = epsilon = 0
nb_ones = [0 for x in range(12)]
for bits in binaries:
    for i, bit in enumerate(bits):
        if bit == "1":
            nb_ones[i] += 1

gamma = "".join(["1" if nb > len(binaries)/2 else "0" for nb in nb_ones])
epsilon = "".join(["1" if bit == "0" else "0" for bit in gamma])

gamma_int = int(gamma, 2)
epsilon_int = int(epsilon, 2)

print("[+] Exercise 1:")
print("\t- gamma:", gamma, "=", gamma_int)
print("\t- epsilon:", epsilon, "=", epsilon_int)
print("\t- power consumption:", gamma_int*epsilon_int)
### ########## ###

print()

### Exercise 2 ###
tmp = copy.deepcopy(binaries)

for i in range(len(binaries[0])):
    nb_ones = 0
    for bits in binaries:
        if bits[i] == "1":
                nb_ones += 1
    binaries = [x for x in binaries if (nb_ones >= len(binaries)/2 and x[i] == "1") or (nb_ones < len(binaries)/2 and x[i] == "0")]
    if len(binaries) == 1:
        oxygene = binaries[0]
        break

binaries = tmp

for i in range(len(binaries[0])):
    nb_ones = 0
    for bits in binaries:
        if bits[i] == "1":
                nb_ones += 1
    binaries = [x for x in binaries if (nb_ones < len(binaries)/2 and x[i] == "1") or (nb_ones >= len(binaries)/2 and x[i] == "0")]
    if len(binaries) == 1:
        co2 = binaries[0]
        break

oxygene_int = int(oxygene, 2)
co2_int = int(co2, 2)

print("[+] Exercise 2:")
print("\t- Oxygene:", oxygene, "=", oxygene_int)
print("\t- CO2:", co2, "=", co2_int)
print("\t- Life support:", oxygene_int*co2_int)
### ########## ###
