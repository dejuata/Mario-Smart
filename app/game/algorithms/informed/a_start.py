#!/usr/bin/python
# -*- coding: utf-8 -*-
# Basado en diapostivas Tema5.pdf del curso de Introducción de IA
from game.agent.node import Node
from time import time

try:
    import Queue
except ImportError:
    # Python 3
    import queue as Queue

def a_start_search(mario):
  start = time()
  queue = Queue.PriorityQueue()
  node = Node(mario.initial)
  f = node.path_cost + mario.h(node)
  queue.put((f, node))
  visited = set()
  count = 0

  while queue:
    f, node = queue.get_nowait()
    visited.add(node.mario)
    if mario.goal_test(node.mario):
      end = time() - start
      return node, count, end
    else:
      for child in node.expand(mario):
        if child.mario not in visited:
          f = child.path_cost + mario.h(child)
          queue.put((f, child))
          count += 1

  return None

