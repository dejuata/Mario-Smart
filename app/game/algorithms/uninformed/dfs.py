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

def depth_first_search(mario):
  stack = [Node(mario.initial)]
  visited = set()
  count = 0

  while stack:
    node = stack.pop(0)
    visited.add(node.mario)
    if mario.goal_test(node.mario):
      return node, count
    else:
      children = node.expand(mario)
      for child in reversed(children):
        if child.mario not in visited:
          stack.insert(0, child)
          count += 1

