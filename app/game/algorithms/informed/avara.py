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

def avara_search(mario, back):
  start = time()
  queue = Queue.PriorityQueue()
  node = Node(mario.initial)
  h = mario.h(node)
  queue.put((h, node))
  visited = set()
  count = 0
  while queue:
    node=queue.get_nowait()[1]
    if mario.goal_test(node.mario):
      return node, count, time() - start
    if back:
      visited.add(node.state_to_tuple())
    for child in node.expand(mario):
      if child.state_to_tuple() not in visited:
        queue.put((mario.h(child), child))
        count += 1



