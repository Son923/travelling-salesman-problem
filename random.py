from itertools import permutations


nodes = ['a', 'b', 'c', 'd', 'e']
paths = list(permutations(nodes[1:]))
all_paths = []
for path in paths:
    copy_path = list(path)
    copy_path.insert(0, nodes[0])
    all_paths.append(tuple(copy_path))
print(all_paths)

# all_paths = list(permutations(self.get_nodes()[1:])).insert(0, self.get_nodes()[0])