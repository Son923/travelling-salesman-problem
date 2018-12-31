from sys import argv, stderr
from timeit import default_timer

from graph import BruteForce, Greedy, TwoOpt, Genetic
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


def create_obj_graph(option, size):
    if option == 'brute':
        print('BRUTE-FORCE')
        graph = BruteForce()
    elif option == 'greedy':
        print('GREEDY')
        graph = Greedy()
    elif option == '2opt':
        print('2-Opt')
        graph = TwoOpt()
    elif option == 'genetic':
        print('Genetic')
        graph = Genetic(size)
    return graph

def main():
    cities, option = parse_map()
    nodes = [Node(city) for city in cities]
    size = len(nodes)

    graph = create_obj_graph(option, size)
    graph.set_nodes(nodes)
    # graph.get_matrix()
    final_path = graph.find_shortest_path()
    graph.print_result(final_path)


if __name__ == "__main__":
    start_time = default_timer()

    main()

    end_time = default_timer()
    print('Process time: %s' % (end_time - start_time))
