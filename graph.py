from node import Node
from abc import ABC, abstractmethod


class Graph(ABC):
    def __init__(self):
        self.nodes = []

    @abstractmethod
    def find_shortest_path(self):
        pass
    
    def set_nodes(self, nodes):
        self.nodes = nodes

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
        start = self.nodes[0]
        path = [start]
        display_path = []
        self.nodes.remove(start)
        while self.nodes:
            next_node = min(self.nodes, key=lambda node: self.distance(path[-1], node))
            path.append(next_node)
            self.nodes.remove(next_node)
        for node in path:
            display_path.append(node.name)
        return (path, display_path)


class HeuristicGreedy(Graph):
    def __init__(self):
        super().__init__()

    def find_shortest_path(self):
        start = self.nodes[0]
        path = [start]
        display_path = []
        self.nodes.remove(start)
        while self.nodes:
            next_node = min(self.nodes, key=lambda node: self.distance(path[-1], node))
            path.append(next_node)
            self.nodes.remove(next_node)
        for node in path:
            display_path.append(node.name)
        return (path, display_path)

    def heuristic(self, node1, node2):
        pos1 = node1.get_pos()
        pos2 = node2.get_pos()
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


class Dynamic(Graph):
    def __init__(self):
        super().__init__()
    
    def find_shortest_path(self):
        start = self.nodes
        path = [start]
        display_path = []
        self.nodes.remove(start)
    
    def min_distance(self, node):
        nodes = self.nodes.remove(node)
        print(nodes)
        print(self.nodes)
        


