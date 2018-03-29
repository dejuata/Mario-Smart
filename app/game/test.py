from algorithms.uninformed import bfs, dfs
from agent.mario import MarioSmart
from agent.node import Node
from utilities.utilities import flat_slice
state = [
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

initial_state = [
  [1, 1, 1, 1, 1],
  [1, 4, 5, 4, 1],
  [1, 4, 1, 4, 1],
  [1, 0, 2, 3, 1],
  [1, 1, 1, 1, 1]
]


mario = MarioSmart(initial_state)
result = bfs.breadth_first_search(mario)
print(result.solution())


# hijos = node.expand(mario)
# for hijo in hijos:
#   print(mario.goal_test(hijo.mario))

# hijos1 = [hijo.expand(mario) for hijo in hijos]
# hijos1 = flat_slice(hijos1)
# for hijo in hijos1:
#   print(mario.goal_test(hijo.mario))


# el orden de los operadores afecta el resultado
# result1 = dfs.depth_first_search(mario)
# print(result1.solution(), result1.path_cost)

