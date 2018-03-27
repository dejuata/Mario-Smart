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

def depth_first_search(tree, start, goal1, goal2=None):
  visited = set()
  stack = [start]
  end = False

  while stack and not end:
    node = stack.pop(0)
    if node not in visited:
      visited.add(node)
    print('Node: ', node)
    if node == goal1 or node == goal2:
      end = True
      print('Goal:', node)
    else:
      children = tree[node]
      print('Children: ', children)
      for child in reversed(children):
        if child not in visited:
          stack.insert(0, child)
      # print('Stack: ', stack)

# Test
# depth_first_search(tree, 'H', 'L', 'G')
depth_first_search(tree1, 'Sibiu', 'Bucharest')
