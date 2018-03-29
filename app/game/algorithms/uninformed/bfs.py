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

  # Nose si a este se le puede agregar los
  # nodos visitados para evitar que se devuelva
  visited = set()
  while queue :
    node = queue.popleft()
    visited.add(node.mario)
    if mario.goal_test(node.mario):
      return node
    else:
      for child in node.expand(mario):
        if child.mario not in visited:
          queue.append(child)

  return None




