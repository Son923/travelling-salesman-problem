from node import Node
from abc import ABC, abstractmethod


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

    def print_result(self):
        result = self.find_shortest_path()
        total_distance = self.total_distance(result[0])
        print(result[1])
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
class Greedy(Graph):
    def __init__(self):
        super().__init__()
    
    def find_shortest_path(self):
        nodes = self.get_nodes()
        start = nodes[0]
        path = [start]
        display_path = []
        nodes.remove(start)
        while nodes:
            next_node = min(nodes, key=lambda node: self.distance(path[-1], node))
            path.append(next_node)
            nodes.remove(next_node)
        for node in path:
            display_path.append(node.get_name())
        return (path, display_path)


class Dynamic(Graph):
    def __init__(self):
        super().__init__()
    
    def find_shortest_path(self):
        start = self.nodes
        path = [start]
        display_path = []
        self.nodes.remove(start)
    
    def min_distance(self, node):
        pass        


class TwoOpt(Graph):
    def __init__(self):
        super().__init__()
    
    def find_shortest_path(self):
        nodes = self.get_nodes()
        start = nodes[0]
        path = [start]
        display_path = []
        nodes.remove(start)
        # This is from greedy
        while nodes:
            next_node = min(nodes, key=lambda node: self.distance(path[-1], node))
            path.append(next_node)
            nodes.remove(next_node)
        # 2opt
        loop = True
        while True:
            for i in range(len(path)):
                for k in range(1,len(path) + 1):
                    new_path = self.swap_2opt(path, i, k)
                    new_total_distance = self.total_distance(new_path)
                    if new_total_distance < total_distance:
                        path = new_path
                        loop = False
        # return
        for node in path:
            display_path.append(node.get_name())
        return (path, display_path)
    
    def swap_2opt(self, path, i, k):
        new_path = []
        new_path.extend(path[0:i-1])
        new_path.extend(path[i:k].reverse())
        new_path.extend(path[k + 1:])
        return new_path
