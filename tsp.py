from node import Node
from graph import Dummy, BFS


def parse_map():
    cities = []
    with open('city.txt', 'r') as map_file:
        content = map_file.readlines()
    for i in content:
        i = i.split(',')
        cities.append((i[0], float(i[1]), float(i[2])))
    return cities


def main():
    cities = parse_map()
    graph = Dummy(cities)
    graph.print_result()


if __name__ == "__main__":
    main()
