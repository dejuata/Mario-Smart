#!/usr/bin/python
# -*- coding: utf-8 -*-
# Basado en http://cyluun.github.io/blog/uninformed-search-algorithms-in-python
# y diapostivas Tema4.pdf del curso de Introducción de IA
try:
    import Queue
except ImportError:
    # Python 3
    import queue as Queue

tree = {
 'Sibiu': [(80, 'Rimnicu'), (99, 'Fagaras')],
 'Rimnicu': [(97, 'Pitesti'), (146, 'Craiova')],
 'Craiova': [(138, 'Pitesti')],
 'Pitesti': [(138, 'Craiova'), (101, 'Bucharest')],
 'Fagaras': [(211, 'Bucharest')]
}

def uniform_cost_search(tree, start, goal):
  queue = Queue.PriorityQueue()
  queue.put((0, start))
  end = False

  while not end:
    cost, node = queue.get_nowait()
    print('Node: ', node)
    if node == goal:
      end = True
      print('Goal:', node)
    else:
      children = tree[node]
      for child in children:
        total_cost = cost + child[0]
        print('Child: ', (total_cost, child[1]))
        queue.put((total_cost, child[1]))



# Test
uniform_cost_search(tree, 'Sibiu', 'Bucharest')
