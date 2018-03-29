#!/usr/bin/python
# -*- coding: utf-8 -*-
# Basado en https://es.wikipedia.org/wiki/B%C3%BAsquedas_no_informadas
# y diapostivas Tema4.pdf del curso de Introducción de IA
from agent.node import Node
try:
    import Queue
except ImportError:
    import queue as Queue


def breadth_first_search(mario):
  queue = Queue.deque([Node(mario.initial)])
  visited = set()
  count = 0

  while queue:
    node = queue.popleft()
    visited.add(node.mario)
    if mario.goal_test(node.mario):
      return node, count
    else:
      for child in node.expand(mario):
        if child.mario not in visited:
          queue.append(child)
          count += 1

  return None




