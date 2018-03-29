#!/usr/bin/python
# -*- coding: utf-8 -*-
# Basado en https://es.wikipedia.org/wiki/B%C3%BAsquedas_no_informadas
# y diapostivas Tema4.pdf del curso de Introducción de IA
try:
    import Queue
except ImportError:
    # Python 3
    import queue as Queue

tree = {
 'H': ['A', 'B', 'C'],
 'A': ['D', 'E'],
 'B': ['F'],
 'C': ['G', 'J'],
 'D': ['K', 'L'],
 'E': [],
 'F': [],
 'G': [],
 'J': [],
 'K': [],
 'L': []
}

tree1 = {
 'Sibiu': ['Rimnicu', 'Fagaras'],
 'Rimnicu': ['Craiova', 'Pitesti'],
 'Craiova': ['Rimnicu', 'Pitesti'],
 'Pitesti': ['Rimnicu', 'Craiova', 'Bucharest'],
 'Fagaras': ['Sibiu', 'Bucharest'],
 'Bucharest': []
}

def breadth_first_search(tree, start, goal1, goal2=None):
  queue = Queue.deque([start])

  while queue:
    node = queue.popleft()
    print('Node: ', node)
    if node == goal1 or node == goal2:
      print('Goal:', node)
      break
    else:
      children = tree[node]
      print('Children: ', children)
      for child in children:
        queue.append(child)
        # print('Queue: ', queue)

# Test
# breadth_first_search(tree, 'H', 'L', 'G')
breadth_first_search(tree1, 'Sibiu', 'Bucharest')
