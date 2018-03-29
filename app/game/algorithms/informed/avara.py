#!/usr/bin/python
# -*- coding: utf-8 -*-
# Basado en diapostivas Tema5.pdf del curso de Introducción de IA
from agent.node import Node
try:
    import Queue
except ImportError:
    # Python 3
    import queue as Queue

def avara_search(mario):
  queue = Queue.PriorityQueue()
  node = Node(mario.initial)
  h = mario.h(node)
  queue.put((h, node))
  visited = set()
  count = 0

  while queue:
    heuristic, node = queue.get_nowait()
    visited.add(node.mario)
    if  mario.goal_test(node.mario):
      return node, count
    else:
      for child in node.expand(mario):
        if child.mario not in visited:
          queue.put((mario.h(child), child))
          count += 1

  return None
