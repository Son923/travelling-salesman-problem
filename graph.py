from abc import ABC, abstractmethod
from itertools import permutations
from random import sample, uniform, random, shuffle
from time import time
from math import sqrt

from node import Node


class Graph(ABC):
    def __init__(self):
        self.__nodes = []

    @abstractmethod
    def find_shortest_path(self):
        pass

    def set_nodes(self, nodes):
        self.__nodes = nodes

    def get_nodes(self):
        return self.__nodes

    def get_matrix(self):
        nodes = self.get_nodes()
        matrix = [[None]]
        matrix[0].extend(nodes)
        for node in nodes:
            next_row = [node]
            for dest in matrix[0][1:]:
                next_row.append(self.distance(node, dest))
            matrix.append(next_row)
        return matrix

    def print_result(self, path):
        final_path = path
        total_distance = self.total_distance(final_path)

        display_path = []
        for node in final_path:
            display_path.append(node.get_name())

        print(display_path)
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


# DONE (only worked with 10 cities)
class BruteForce(Graph):
    def __init__(self):
        super().__init__()

    def find_shortest_path(self):
        all_paths = self.permutation()
        path = min(all_paths, key=lambda path: self.total_distance(path))
        return path

    def permutation(self):
        nodes = self.get_nodes()
        paths = list(permutations(self.get_nodes()[1:]))
        all_paths = []
        for path in paths:
            copy_path = list(path)
            copy_path.insert(0, nodes[0])
            all_paths.append(tuple(copy_path))
        return all_paths


# DONE (best so far)
class Greedy(Graph):
    def __init__(self):
        super().__init__()

    def find_shortest_path(self):
        nodes = self.get_nodes()
        start = nodes[0]
        path = [start]
        nodes.remove(start)
        while nodes:
            next_node = min(nodes, key=lambda node: self.distance(path[-1], node))
            path.append(next_node)
            nodes.remove(next_node)
        return path


# DONE (worst)
class TwoOpt(Graph):
    def __init__(self):
        super().__init__()

    def find_shortest_path(self):
        nodes = self.get_nodes()
        start = nodes[0]
        init_path = [start]
        nodes.remove(start)
        # greedy path as init_path
        while nodes:
            next_node = min(nodes, key=lambda node: self.distance(init_path[-1], node))
            init_path.append(next_node)
            nodes.remove(next_node)

        # 2opt
        best_path = init_path
        loop = True
        while loop:
            loop = False
            for i in range(1, len(init_path) - 1):
                for k in range(i + 1, len(init_path) + 1):
                    # if k-i == 1:
                    #     continue
                    new_path = self.swap_2opt(init_path, i, k)

                    new_total_distance = self.total_distance(new_path)
                    total_distance = self.total_distance(best_path)
                    if new_total_distance < total_distance:
                        best_path = new_path
                        loop = True
            init_path = best_path
        return best_path

    def swap_2opt(self, path, i, k):
        new_path = path
        new_path[i:k] = path[k - 1: i - 1: -1]
        return new_path


class BnB(Graph):
    def __init__(self):
        super().__init__()
    
    def find_shortest_path(self):
        pass

    def reduce_matrix(self):
        matrix = self.get_matrix()
        reduced_matrix = []

class Genetic(Graph):
    def __init__(self, side, verbose=False):
        super().__init__()

        self._parent = self.get_nodes()
        self._side = side

        self._mutate_rate = 0.07
        self._population_size = 60 if len(self._parent) > 10 else 10
        self._new_generation_size = self._population_size*2
        self._rounds = 200
        self._genlen = len(self._parent)
        self._verbose = verbose
        self._cached_distances = {}
        self._cached_fitness = {}

    def find_shortest_path(self):
    
        population = self.generate_population()
        fitest = min(population, key=self.fitness)

        total_time = time()
        for r in range(self._rounds):
            new_pop = []
            while len(new_pop) < self._new_generation_size:
                father = self.select(population)
                mother = self.select(population)
                child = self.crossover(father, mother)
                if child not in new_pop:
                    new_pop += [child]
                    continue
                for i in range(len(new_pop)):
                    if random() < self._mutate_rate:
                        new_pop[i] = self.mutate(new_pop[i])

            new_fittest = min(population, key=self.fitness)
            if self.fitness(fitest) > self.fitness(new_fittest):
                fitest = new_fittest
            if r % 50 == 0:
                print(r, self.fitness(min(population, key=self.fitness)))

            population = self.selection(new_pop)
            if fitest not in population:
                population += [fitest]

        self.result(population, fitest, total_time)
        return population

    def result(self, population, fitest, total_time):
        if self._verbose:
            for ind in sorted(population, key=self.fitness):
                print("Path: {}, Fitness: {:.3f}".format(ind, self.fitness(ind)))

            print("Cached-> Fitness:{}, Distances: {}".format(len(self._cached_fitness), 
                    len(self._cached_distances)))
        print("Execution Time: {:.3f}s".format(time() - total_time))
        print("Best path found: {}, fitness: {:.3f}".format(fitest, self.fitness(fitest)))

    def selection(self, new_pop):

        shuffle(new_pop)
        pop = []
        for _ in range(self._population_size):
            survivor = self.select(new_pop)
            new_pop.remove(survivor)
            pop += [survivor]
        return pop

    def select(self, pop):

        pop_total_fit = sum(1.0 / self.fitness(p) for p in pop)
        limit = uniform(0.0, pop_total_fit)
        c = 0
        for p in pop:
            c += 1 / self._cached_fitness[hash(tuple(p))]
            if c > limit:
                return p

    def fitness(self, child):

        h = hash(tuple(child))
        if h in self._cached_fitness.keys():
            return self._cached_fitness[h]

        distance = 0
        for i in range(len(child)-1):
            distance += self.point_distance(child[i], child[i+1])
        self._cached_fitness[h] = distance
        return distance

    @staticmethod
    def crossover(father, mother):
        
        child = [None]*len(father)
        rate = 0.5
        for gen in father:
            parent, other_parent = (father, mother) if random() > rate \
                else (mother, father)

            key = None
            for key, value in enumerate(parent):
                if value == gen:
                    break
            if not child[key]:
                child[key] = gen
                continue
            for key, value in enumerate(other_parent):
                if value == gen:
                    break
            if not child[key]:
                child[key] = gen
                continue

            for key, value in enumerate(child):
                if not value:
                    child[key] = gen
                    break
        return child

    @staticmethod
    def mutate(child):

        i1, i2 = sample(range(1, len(child)-1), 2)
        child[i1], child[i2] = child[i2], child[i1]
        return child

    def point_distance(self, p1, p2):

        nodes = hash((p1, p2))
        if nodes in self._cached_distances.keys():
            return self._cached_distances[nodes]
        d = sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)
        self._cached_distances[nodes] = d
        return d

    def generate_population(self):

        pop = [self._parent[:1]+sample(
            self._parent[1:-1], len(self._parent)-2)+self._parent[-1:]
               for _ in range(self._population_size)]
        for p in pop:
            h = hash(tuple(p))
            self._cached_fitness[h] = self.fitness(p)
        return pop
    
