from sys import argv, stderr

from graph import BruteForce, Greedy, TwoOpt
from node import Node


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
    if option == 'brute':
        print('BRUTE-FORCE')
        graph = BruteForce()
    elif option == 'greedy':    
        print('GREEDY')
        graph = Greedy()
    elif option == '2opt':
        print('2-Opt')
        graph = TwoOpt()

    graph.set_nodes(nodes)
    graph.print_result()

if __name__ == "__main__":
    main()
