from node import Node
from graph import Greedy, Dynamic, TwoOpt
from sys import argv, stderr


def parse_map():
    cities = []
    try:
        with open(argv[1], 'r') as map_file:
            content = map_file.readlines()
        for i in content:
            i = i.split(',')
            cities.append((i[0], float(i[1]), float(i[2])))
        option = argv[2]
        return cities, option
    except IndexError:
        stderr.write('Invalid file')
        exit()


def main():
    cities, option = parse_map()
    nodes = [Node(city) for city in cities]

    if option == 'greedy':    
        # Greedy
        print('GREEDY')
        graph = Greedy()
        graph.set_nodes(nodes)
        graph.print_result()
    elif option == 'dynamic':
        # Dynamic
        print('DYNAMIC')
        graph1 = Dynamic()
        graph1.set_nodes(nodes)
        graph1.min_distance(nodes[0])
    elif option == '2opt':
        print('2-Opt')
        graph2 = TwoOpt()
        graph2.set_nodes(nodes)
        graph2.print_result()

if __name__ == "__main__":
    main()
