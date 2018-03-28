#!/usr/bin/python
# -*- coding: utf-8 -*-
# Basado en diapostivas Tema5.pdf del curso de Introducción de IA
try:
    import Queue
except ImportError:
    # Python 3
    import queue as Queue

#(g(n), h(n), city)
tree = {
 'Sibiu': [(140, 366, 'Arad'), (151, 380, 'Oradea'), (80, 193, 'Rimnicu'), (99, 178, 'Fagaras')],
 'Arad': [(118, 329, 'Timisoara'), (75, 374, 'Zerind')],
 'Oradea': [(71, 374, 'Zerind')],
 'Rimnicu': [(97, 98, 'Pitesti'), (146, 160, 'Craiova')],
 'Fagaras': [(211, 0, 'Bucharest')],
 'Craiova':[(138, 98, 'Pitesti')],
 'Pitesti': [(138, 160, 'Craiova'),(101, 0, 'Bucharest')],
}

def a_start_search(tree, start, goal):
  queue = Queue.PriorityQueue()
  f = 0 + 253
  # f(n), g(n), city
  queue.put((f, 0, start))

  while True:
    f, cost, node = queue.get_nowait()
    print('Node: ', node)
    if node == goal:
      print('Goal:', f, node)
      break
    else:
      children = tree[node]
      for child in children:
        total_cost = cost + child[0]
        f = total_cost + child[1]
        print('Child: ', (f, total_cost, child[2]))
        queue.put((f, total_cost, child[2]))

# Test
a_start_search(tree, 'Sibiu', 'Bucharest')
