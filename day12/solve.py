# parse input adjacency matrix
adjacency = {}
for line in open("input.txt", "r").readlines():
    e1, e2 = list(map(lambda x: x.strip(), line.split("-")))
    if e1 not in adjacency.keys():
        adjacency[e1] = []
    if e2 not in adjacency.keys():
        adjacency[e2] = []
    if e2 not in adjacency[e1] and e2 != "start":
        adjacency[e1].append(e2)
    if e1 not in adjacency[e2] and e1 != "start":
        adjacency[e2].append(e1)

### Exercise 1 ##

def find_all_paths(adjacency, current_node, visited):
    new_path = visited + [current_node]
    if current_node == 'end':
        return [new_path]

    paths = []
    for node in adjacency[current_node]:
        if node != 'start':
            if node not in visited or node.isupper():
                paths += find_all_paths(adjacency, node, new_path)

    return paths

paths = find_all_paths(adjacency, "start", [])
print("[+] Exercise 1:")
print("\t- Number of paths:", len(paths))
### ########## ###



### Exercise 2 ###

def find_all_paths(adjacency, current_node, visited):
    new_path = visited + [current_node]
    if current_node == 'end':
        return [new_path]

    paths = []
    for node in adjacency[current_node]:
        if node != 'start':
            if node.isupper():
                paths += find_all_paths(adjacency, node, new_path)
            else:
                hasTwo = False
                for n in new_path:
                    if n.islower() and new_path.count(n) > 1:
                        hasTwo = True
                        break
                if (not hasTwo) or (hasTwo and node not in new_path):
                    paths += find_all_paths(adjacency, node, new_path)

    return paths

paths = find_all_paths(adjacency, "start", [])
print("[+] Exercise 2:")
print("\t- Number of paths:", len(paths))
### ########## ###