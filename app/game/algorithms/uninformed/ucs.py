#!/usr/bin/python
# -*- coding: utf-8 -*-
# Basado en http://cyluun.github.io/blog/uninformed-search-algorithms-in-python
# y diapostivas Tema4.pdf del curso de Introducción de IA
from agent.node import Node
try:
    import Queue
except ImportError:
    # Python 3
    import queue as Queue


def uniform_cost_search(mario):
  queue = Queue.PriorityQueue()
  queue.put((0, Node(mario.initial)))
  visited = set()
  count = 0

  while queue:
    cost, node = queue.get_nowait()
    visited.add(node.mario)
    if mario.goal_test(node.mario):
      return node, count
    else:
      for child in node.expand(mario):
        if child.mario not in visited:
          queue.put((child.path_cost, child))
          count += 1

  return None

