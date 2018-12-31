from random import sample

# def testing(route):
#     best = route
#     improved = True
#     while improved:
#         improved = False
#         for i in range(1, len(route)-2):
#             for j in range(i+1, len(route)):
#                 if j-i == 1: continue # changes nothing, skip then
#                 new_route = route[:]
#                 new_route[i:j] = route[j-1:i-1:-1] # this is the 2woptSwap
#                 if cost(new_route) < cost(best):
#                         best = new_route
#                         improved = True
#         route = best
#     return best


route = ['a', 'b', 'c', 'd', 'e', 'f']
# for i in range(1, len(route)-1):
#     for j in range(i+1, len(route) +1):
#         new_route = route[:]
#         new_route[i:j] = route[j-1:i-1:-1]
#         print(new_route)
population_size = 10
# pop = [route[:1]+sample(route[1:-1], len(route)-2)+route[-1:] for _ in range(population_size)]
pop = [route[:1] + sample(route[1:], len(route) - 1) for _ in range(population_size)]
print(pop)