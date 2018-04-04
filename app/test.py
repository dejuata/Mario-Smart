from game.algorithms.uninformed import bfs, dfs, ucs
from game.algorithms.informed import avara, a_start
from game.agent.mario import MarioSmart
from game.agent.node import Node
from time import time
try:
    import Queue
except ImportError:
    # Python 3
    import queue as Queue

level1 = [
  [ 1,1,1,1,1,1,1,1,1,1,1,1],
  [ 1,0,3,0,0,0,0,1,1,0,1,1],
  [ 1,4,1,1,1,1,0,1,0,0,0,1],
  [ 1,4,0,0,1,0,0,1,0,1,0,1],
  [ 1,0,1,0,1,0,0,4,0,1,0,1],
  [ 1,4,4,4,3,0,1,1,0,0,5,1],
  [ 1,2,1,0,0,1,1,1,4,1,0,1],
  [ 1,0,1,1,0,0,3,1,4,1,0,1],
  [ 1,0,0,1,1,1,0,4,4,1,0,1],
  [ 1,1,0,0,0,1,0,1,4,0,0,1],
  [ 1,1,1,1,0,0,0,1,0,1,1,1],
  [ 1,1,1,1,1,1,1,1,1,1,1,1]
]

level2 = [
  [ 1,1,1,1,1,1,1,1,1,1,1,1],
  [ 1,0,0,0,1,4,4,4,0,1,1,1],
  [ 1,0,1,0,4,4,1,1,0,0,0,1],
  [ 1,5,1,0,1,0,1,3,4,1,1,1],
  [ 1,1,1,0,1,0,4,4,0,0,1,1],
  [ 1,0,4,4,4,1,0,0,1,0,1,1],
  [ 1,0,3,1,4,1,1,1,1,0,1,1],
  [ 1,0,4,1,4,4,0,0,0,2,0,1],
  [ 1,0,0,1,1,1,0,1,1,1,0,1],
  [ 1,1,0,0,0,1,0,0,0,0,0,1],
  [ 1,1,1,0,0,0,0,0,1,1,1,1],
  [ 1,1,1,1,1,1,1,1,1,1,1,1]
]

level3 = [
  [ 1,1,1,1,1,1,1,1,1,1,1,1],
  [ 1,2,0,0,0,0,0,4,4,0,0,1],
  [ 1,1,0,1,1,1,1,0,1,1,0,1],
  [ 1,4,4,4,1,0,0,4,0,1,0,1],
  [ 1,0,1,0,1,4,1,1,1,1,0,1],
  [ 1,0,4,4,4,0,0,0,3,0,0,1],
  [ 1,1,0,1,0,1,1,1,1,4,0,1],
  [ 1,4,0,1,4,4,4,0,1,4,0,1],
  [ 1,0,1,1,1,1,9,0,0,4,4,1],
  [ 1,0,1,9,0,1,4,1,1,1,1,1],
  [ 1,0,4,4,4,0,0,8,5,1,1,1],
  [ 1,1,1,1,1,1,1,1,1,1,1,1]
]

initial_state = [
  [1, 1, 1, 1, 1, 1],
  [1, 0, 3, 0, 0, 1],
  [1, 4, 4, 1, 4, 1],
  [1, 2, 0, 0, 5, 1],
  [1, 0, 1, 4, 0, 1],
  [1, 1, 1, 1, 1, 1]
]

mario = MarioSmart(level1)


# Busqueda por amplitud
# result = bfs.breadth_first_search(mario, True)
# print(result[0].solution())


# # Busqueda por profundidad
# el orden de los operadores afecta el resultado
# si el agente captura una flor, el estado cambia, ya que es inmune ante los enemigos,
# por lo tanto puede devolverse, ya que el nodo que expande es diferente al anterior
result1 = dfs.depth_first_search(mario)
print(result1[0].solution())


# # # Busqueda por costo uniforme
# result2 = ucs.uniform_cost_search(mario, True)
# print(result2[0].solution(), result2[0].path_cost)

# # Busqueda avara
# result3 = avara.avara_search(mario, True)
# print(result3[0].solution())

# # Busqueda A*
# result4 = a_start.a_start_search(mario, True)
# print(result4[0].solution())
