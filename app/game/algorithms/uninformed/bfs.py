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
  try:
    while queue:
      node = queue.popleft()
      if mario.goal_test(node.mario):
        return node, count,  time() - start
      if back :
        visited.add(node.state_to_tuple())
      for child in node.expand(mario):
        if child.state_to_tuple() not in visited:
          queue.append(child)
          count += 1
  except:
    return None, count, time() - start






