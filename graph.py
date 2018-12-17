# https://codereview.stackexchange.com/questions/148399/graph-and-node-classes-with-bfs-and-dfs-functions

from node import Node

class Graph:
    def __init__(self, city_list, options):
        self.__algo = options['algo']
        self.__nodes = [Node(city) for city in city_list]
        print(self.__nodes)

    def find_shortest_path(self, algo):
        return getattr(self, algo)(self.__nodes)
    
    def print_result(self):
        print(self.find_shortest_path(self.__algo))
    
    def bfs(self, nodes):
        return 'bfs'
        pass
    
    def dfs(self, nodes):
        return 'dfs'
        pass
