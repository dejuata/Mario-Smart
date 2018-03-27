#!/usr/bin/python
# -*- coding: utf-8 -*-
import collections

tree = {
 'H': ['A', 'B', 'C'],
 'A': ['D', 'E'],
 'B': ['F'],
 'C': ['G', 'J'],
 'D': ['K', 'L'],
 'E': [],
 'F': [],
 'G': [],
 'J': []
}
# Estado inicial
start = [
  [ 0,3,0,0,0,0,1,1,0,1],
  [ 4,1,1,1,1,0,1,0,0,0],
  [ 4,0,0,1,0,0,1,0,1,0],
  [ 0,1,0,1,0,0,4,0,1,0],
  [ 4,4,4,3,0,1,1,0,0,5],
  [ 2,1,0,0,1,1,1,4,1,0],
  [ 0,1,1,0,0,0,1,4,1,0],
  [ 0,0,1,1,1,0,4,4,1,0],
  [ 1,0,0,0,1,0,1,4,0,0],
  [ 1,1,1,0,0,0,1,0,1,1],
]


def breadth_first_search(tree, start, goal):
  # Nodo raiz
  queue = collections.deque([start])
  end = False

  while queue and not end:
    node = queue.popleft()
    print('nodo: ', node)
    if node == goal:
      end = True
      print('Es meta:', node)
    else:
      children = tree[node]
      print(children)
    for child in children:
      queue.append(child)
    print('cola: ', queue)

# bfs(tree, 'H', 'G')
# start[y][x]
print(start[5][0])
