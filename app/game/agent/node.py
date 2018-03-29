#!/usr/bin/python
# -*- coding: utf-8 -*-
# Basado en https://www.cs.us.es/cursos/iati-2012/
import numpy as np

class Node:
  """
  Un nodo se define como:
  • El estado del problema
  • Una referencia al nodo padre
  • El operador que se aplicó para generar el nodo
  • Profundidad del nodo
  • El costo de la ruta desde la raíz hasta el nodo
  """

  def __init__(self, state, parent=None, action=None, path_cost=0):
    self.state = state
    self.parent = parent
    self.action = action
    self.path_cost = path_cost
    self.depth = 0
    self.mario = self.find_mario(self.state)
    if parent:
      self.depth = parent.depth + 1

  def __repr__(self):
    return "<Node {}>".format(self.state)

  def __lt__(self, node):
    return self.state < node.state

  def expand(self, problem):
    """
    List of nodes generated by the possible actions applied to the initial state
    """
    return [self.child_node(problem, action) for action in problem.actions(self.state, self.mario)]

  def child_node(self, problem, action):
    """
    Successor of a node by an applicable action
    """
    next_node = problem.result_of_actions(self.state, action, self.mario)
    return Node(
      state=next_node,
      parent=self,
      action=action,
      path_cost = problem.path_cost(
        c = self.path_cost,
        state = self.state,
        action = action,
        mario = self.mario,
      )
    )

  def solution(self):
    """
    Return the sequence of actions to go from the root to this node.
    """
    return [node.action for node in self.path()[1:]]

  def path(self):
    """
    Return a list of nodes forming the path from the root to this node.
    """
    node, path_back = self, []
    while node:
        path_back.append(node)
        node = node.parent
    return list(reversed(path_back))

  def __eq__(self, other):
    return isinstance(other, Node) and self.state == other.state

  def find_mario(self, state):
    matriz = np.array(state)
    p = np.where(matriz==2)
    return(p[0][0], p[1][0])


