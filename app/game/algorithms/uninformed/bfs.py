#!/usr/bin/python
# -*- coding: utf-8 -*-
# Basado en https://es.wikipedia.org/wiki/B%C3%BAsquedas_no_informadas
# y diapostivas Tema4.pdf del curso de Introducción de IA
from game.agent.node import Node
from time import time

try:
    import Queue
except ImportError:
    import queue as Queue


def breadth_first_search(mario, back):
  start = time()
  queue = Queue.deque([Node(mario.initial)])
  visited = set()
  count = 0
  while queue:
    node = queue.popleft()
    if back :
      visited.add(node.mario)
    if mario.goal_test(node.mario):
      end = time() - start
      return node, count, end
    for child in node.expand(mario):
      if child.mario not in visited:
        queue.append(child)
        count += 1
        print(count)





