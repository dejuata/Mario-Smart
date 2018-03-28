#!/usr/bin/python
# -*- coding: utf-8 -*-
# Basado en diapostivas Tema5.pdf del curso de Introducción de IA
try:
    import Queue
except ImportError:
    # Python 3
    import queue as Queue

tree = {
 'Arad': [(253, 'Sibiu'), (329, 'Timisoara'), (374, 'Zerind')],
 'Sibiu': [(366, 'Arad'), (380, 'Oradea'), (193, 'Rimnicu'), (178, 'Fagaras')],
 'Timisoara': [(366, 'Arad'), (244, 'Lugoj')],
 'Zerind': [(366, 'Arad'), (380, 'Oradea')],
 'Oradea': [(374, 'Zerind'), (253, 'Sibiu')],
 'Rimnicu': [(253, 'Sibiu'), (98, 'Pitesti'), (160, 'Craiova')],
 'Pitesti': [(193, 'Rimnicu'), (160, 'Craiova'),(0, 'Bucharest')],
 'Fagaras': [(253, 'Sibiu'),(0, 'Bucharest')]
}

def avara_search(tree, start, h):
  queue = Queue.PriorityQueue()
  queue.put((h, start))

  while True:
    heuristic, node = queue.get_nowait()
    print('Node: ', node)
    if heuristic == 0:
      print('Goal:', node)
      break
    else:
      children = tree[node]
      for child in children:
        print('Child: ', child)
        queue.put(child)

# Test
avara_search(tree, 'Arad', 366)
