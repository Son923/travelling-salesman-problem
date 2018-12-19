
lst = ['a', 'b', 'c', 'd', 'e', 'f']

def swap_2opt(path, i, k):       
        new_path = []
        new_path.extend(path[0:i-1])
        new_path.extend(path[i:k].reverse())
        new_path.extend(path[k + 1:])
        return new_path

def total_distance(self, path):
        total_distance = 0
        for index, node in enumerate(path[:-1]):
            total_distance += self.distance(node, path[index + 1])
        return total_distance

for i in range(len(lst)):
    for k in range(len(lst)):
        new_path = swap_2opt(path, i, k)
        new_total_distance = total_distance(new_path)
        if new_total_distance < total_distance:
            path = new_path
