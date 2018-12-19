from node import Node
from graph import Greedy, Dynamic
from sys import argv, stderr


def parse_map():
    cities = []
    try:
        with open(argv[1], 'r') as map_file:
            content = map_file.readlines()
        for i in content:
            i = i.split(',')
            cities.append((i[0], float(i[1]), float(i[2])))
        return cities
    except IndexError:
        print('No file')
        stderr.write('Invalid file')
        exit()


def main():
    cities = parse_map()
    nodes = [Node(city) for city in cities]

    # Greedy
    print('GREEDY')
    graph = Greedy(nodes)
    # graph.set_nodes(nodes)
    graph.print_result()

    # graph1 = Dynamic()
    # graph1.set_nodes(nodes)
    # graph1.min_distance(nodes[0])
 

if __name__ == "__main__":
    main()
