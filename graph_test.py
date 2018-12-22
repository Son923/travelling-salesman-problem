from graph import TwoOpt

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

def test_2opt(nodes):
    graph = TwoOpt()
    graph.set_nodes()

def main_test():
    # Initiate
    cities, option = parse_map()
    nodes = [Node(city) for city in cities]
    # Testing
    print("TwoOpt test: ")
    test_2opt(nodes)
    
    pass

if __name__ == "__main__":
    main_test()

