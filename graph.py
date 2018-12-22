from abc import ABC, abstractmethod
from itertools import permutations

from node import Node


class Graph(ABC):
    def __init__(self):
        self.__nodes = []

    @abstractmethod
    def find_shortest_path(self):
        pass
    
    def set_nodes(self, nodes):
        self.__nodes = nodes
    
    def get_nodes(self):
        return self.__nodes

    def print_result(self, path):
        final_path = path
        total_distance = self.total_distance(final_path)
        
        display_path = []
        for node in final_path:
            display_path.append(node.get_name())

        print(display_path)
        print('Total distance: ' + str(total_distance))

    def distance(self, node1, node2):
        pos1 = node1.get_pos()
        pos2 = node2.get_pos()
        return ((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2) ** 0.5

    def total_distance(self, path):
        total_distance = 0
        for index, node in enumerate(path[:-1]):
            total_distance += self.distance(node, path[index + 1])
        return total_distance

# DONE
class BruteForce(Graph):
    def __init__(self):
        super().__init__()
    
    def find_shortest_path(self):
        all_paths = self.permutation()
        path = min(all_paths, key=lambda path: self.total_distance(path))
        return path

    def permutation(self):
        nodes = self.get_nodes()
        paths = list(permutations(self.get_nodes()[1:]))
        all_paths = []
        for path in paths:
            copy_path = list(path)
            copy_path.insert(0, nodes[0])
            all_paths.append(tuple(copy_path))   
        return all_paths

# DONE
class Greedy(Graph):
    def __init__(self):
        super().__init__()
    
    def find_shortest_path(self):
        nodes = self.get_nodes()
        start = nodes[0]
        path = [start]
        nodes.remove(start)
        while nodes:
            next_node = min(nodes, key=lambda node: self.distance(path[-1], node))
            path.append(next_node)
            nodes.remove(next_node)
        return path


class TwoOpt(Graph):
    def __init__(self):
        super().__init__()
    
    def find_shortest_path(self):
        nodes = self.get_nodes()
        start = nodes[0]
        init_path = [start]
        display_path = []
        nodes.remove(start)
        # greedy path as init_path
        while nodes:
            next_node = min(nodes, key=lambda node: self.distance(init_path[-1], node))
            init_path.append(next_node)
            nodes.remove(next_node)
        
        # 2opt
        loop = True
        while loop:
            best_path = init_path
            total_distance = self.total_distance(best_path)
            for i in range(len(best_path) - 1):
                for k in range(i + 1, len(best_path)):
                    new_path = self.swap_2opt(best_path, i, k)
                    new_total_distance = self.total_distance(new_path)
                    if new_total_distance < total_distance:
                        best_path = new_path 
            if init_path != best_path:
                init_path = best_path
            else:
                loop = False
        return best_path
    
    def swap_2opt(self, path, i, k):
        copy_path = path[i:k]
        copy_path.reverse()
        new_path = []

        new_path.extend(path[0:i-1])
        new_path.extend(copy_path)
        new_path.extend(path[k + 1:])
        return new_path
