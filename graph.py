from node import Node
from abc import ABC, abstractmethod


class Graph(ABC):
    def __init__(self, city_list):
        self.nodes = [Node(city) for city in city_list]

    @abstractmethod
    def find_shortest_path(self, nodes):
        pass
    
    def print_result(self):
        result = self.find_shortest_path(self.nodes)
        total_distance = self.total_distance(result[0])
        print(result[1])
        print('Total distance: ' + str(total_distance))

    def distance(self, node1, node2):
        pos1 = node1.get_position()
        pos2 = node2.get_position()
        return ((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2) ** 0.5

    def total_distance(self, path):
        total_distance = 0
        for index, node in enumerate(path[:-1]):
            total_distance += self.distance(node, path[index + 1])
        return total_distance


class Dummy(Graph):
    def __init__(self, city_list):
        super().__init__(city_list)
    
    def find_shortest_path(self, nodes):
        start = nodes[0]
        path = [start]
        display_path = []
        nodes.remove(start)
        while nodes:
            next_node = min(nodes, key=lambda node: self.distance(path[-1], node))
            path.append(next_node)
            nodes.remove(next_node)
        for node in path:
            display_path.append(node.name)
        return (path, display_path)


class BFS(Graph):
    def __init__(self, city_list):
        super().__init__(city_list)
    
    def find_shortest_path(self, nodes):
        start = nodes[0]
        path = [start]
        display_path = []
        nodes.remove(start)
        while nodes:
            next_node = min(nodes, key=lambda node: self.distance(path[-1], node))
            path.append(next_node)
            nodes.remove(next_node)
        for node in path:
            display_path.append(node.name)
        return (path, display_path)


class DFS(Graph):
    def __init__(self, city_list):
        super().__init__(city_list)
    
    def find_shortest_path(self, nodes):
        start = nodes[0]
        path = [start]
        display_path = []
        nodes.remove(start)
        while nodes:
            next_node = min(nodes, key=lambda node: self.distance(path[-1], node))
            path.append(next_node)
            nodes.remove(next_node)
        for node in path:
            display_path.append(node.name)
        return (path, display_path)
