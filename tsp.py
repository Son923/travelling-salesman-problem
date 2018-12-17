from node import Node
from graph import Graph

def main():

    cities = parse_map()
    graph = Graph(cities, {'algo': 'bfs'})
    graph.print_result()
    

def parse_map():
    cities = []
    with open('city.txt', 'r') as map_file:
        content = map_file.read().split('\n')
    for i in content:
        i = i.split(',')
        cities.append((i[0], float(i[1]), float(i[2])))
    return cities

if __name__ == "__main__":
    main()


