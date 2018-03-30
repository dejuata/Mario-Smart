from game.algorithms.uninformed import bfs, dfs, ucs
from game.algorithms.informed import avara, a_start
from game.agent.mario import MarioSmart
from game.agent.node import Node
from time import time

level1 = [
  [ 1,1,1,1,1,1,1,1,1,1,1,1],
  [ 1,0,3,0,0,0,0,1,1,0,1,1],
  [ 1,4,1,1,1,1,0,1,0,0,0,1],
  [ 1,4,0,0,1,0,0,1,0,1,0,1],
  [ 1,0,1,0,1,0,0,4,0,1,0,1],
  [ 1,4,4,4,3,0,1,1,0,0,5,1],
  [ 1,2,1,0,0,1,1,1,4,1,0,1],
  [ 1,0,1,1,0,0,0,1,4,1,0,1],
  [ 1,0,0,1,1,1,0,4,4,1,0,1],
  [ 1,1,0,0,0,1,0,1,4,0,0,1],
  [ 1,1,1,1,0,0,0,1,0,1,1,1],
  [ 1,1,1,1,1,1,1,1,1,1,1,1]
]

level2 = [
  [ 1,1,1,1,1,1,1,1,1,1,1,1],
  [ 1,0,0,0,1,0,0,0,0,1,1,1],
  [ 1,0,1,0,4,0,1,1,0,0,0,1],
  [ 1,5,1,0,1,0,1,3,0,1,1,1],
  [ 1,1,1,0,1,0,4,4,0,0,1,1],
  [ 1,0,4,4,0,1,0,0,1,0,0,1],
  [ 1,0,0,1,4,1,1,1,1,0,1,1],
  [ 1,0,0,1,4,0,0,0,0,2,0,1],
  [ 1,0,3,1,1,1,0,0,1,1,0,1],
  [ 1,1,0,0,0,1,0,0,0,0,0,1],
  [ 1,1,0,0,0,0,0,0,1,1,1,1],
  [ 1,1,1,1,1,1,1,1,1,1,1,1]
]

level3 = [
  [ 1,1,1,1,1,1,1,1,1,1,1,1],
  [ 1,2,3,4,0,4,0,0,0,0,4,1],
  [ 1,1,4,1,1,1,1,3,1,1,0,1],
  [ 1,0,4,0,1,4,0,0,0,1,0,1],
  [ 1,4,1,0,1,4,1,1,1,1,0,1],
  [ 1,0,4,4,4,3,0,0,0,0,4,1],
  [ 1,1,4,1,4,1,1,1,1,4,4,1],
  [ 1,0,0,1,4,4,0,0,1,4,0,1],
  [ 1,4,1,1,1,1,0,0,4,0,0,1],
  [ 1,0,1,0,0,1,0,1,1,1,1,1],
  [ 1,4,0,0,0,0,0,4,5,1,1,1],
  [ 1,1,1,1,1,1,1,1,1,1,1,1]
]

initial_state = [
  [1, 1, 1, 1, 1],
  [1, 4, 5, 4, 1],
  [1, 4, 1, 3, 1],
  [1, 3, 2, 4, 1],
  [1, 1, 1, 1, 1]
]


mario = MarioSmart(initial_state)

# Busqueda por amplitud
# start = time()
result = ucs.uniform_cost_search(mario)
print(result[0].solution(), result[0].path_cost)
# end = time() - start
# compute = "{:.10f} s".format(end)

# print('Mov: {} Depth: {} Nodos: {} Computo: {}'.format(result[0].solution(), result[0].depth, result[1], compute))

# # Busqueda por profundidad
# el orden de los operadores afecta el resultado
# start = time()
# result1 = dfs.depth_first_search(mario)
# end = time() - start
# compute = "{:.10f} s".format(end)

# print('Mov: {} Depth: {} Nodos: {} Computo: {}'.format(result1[0].solution(), result1[0].depth, result1[1], compute))

# # # Busqueda por costo uniforme
# start = time()
# result2 = ucs.uniform_cost_search(mario)
# end = time() - start
# compute = "{:.10f} s".format(end)

# print('Mov: {} Depth: {} Nodos: {} Computo: {}'.format(result2[0].solution(), result2[0].depth, result2[1], compute))

# # Busqueda avara
# start = time()
# result3 = avara.avara_search(mario)
# end = time() - start
# compute = "{:.10f} s".format(end)

# print('Mov: {} Depth: {} Nodos: {} Computo: {}'.format(result3[0].solution(), result3[0].depth, result3[1], compute))

# # Busqueda A*
# start = time()
# result4 = a_start.a_start_search(mario)
# end = time() - start
# compute = "{:.10f} s".format(end)

# print('Mov: {} Depth: {} Nodos: {} Computo: {}'.format(result4[0].solution(), result4[0].depth, result4[1], compute))
