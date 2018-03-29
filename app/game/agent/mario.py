#!/usr/bin/python
# -*- coding: utf-8 -*-
# Basado en https://www.cs.us.es/cursos/iati-2012/
import numpy as np
from copy import deepcopy


class MarioSmart(object):

  def __init__(self, initial, goal=None):
    self.initial = initial
    self.goal = goal
    self.princess = self.find_position(self.initial, 5)

  def actions(self, state, mario):
    """
    Return the actions that can be executed in the given state
    """
    possible_actions = ['Up', 'Down', 'Left', 'Right']

    x = mario[1]
    y = mario[0]

    # check the free roads
    # UP
    if self.check_position(state=state, x=x, y=y-1) == 1:
      possible_actions.remove('Up')
    # DOWN
    if self.check_position(state=state, x=x, y=y+1) == 1:
      possible_actions.remove('Down')
    # LEFT
    if self.check_position(state=state, x=x-1, y=y) == 1:
      possible_actions.remove('Left')
    # RIGHT
    if self.check_position(state=state, x=x+1, y=y) == 1:
      possible_actions.remove('Right')

    return possible_actions

  def result_of_actions(self, state, action, mario):
    """
    Return the new state that results from executing the action in the given state
    """
    x, y = mario[1], mario[0]
    new_state = deepcopy(state)
    position = self.next_position(mario, action)

    new_state[y][x] = 0

    new_state[position[0]][position[1]] = 2

    return new_state

  def goal_test(self, mario):
    """
    Return True if the state is a goal
    """
    return self.princess == mario

  def path_cost(self, c, state, action, mario):
    """
    Return the cost of a solution path that arrives at state
    via action, assuming cost c to get up to state.
    """
    x = mario[1]
    y = mario[0]
    position = self.next_position(mario, action)
    check = self.check_position(state=state, y=position[0], x=position[1])

    cost = 7 if check == 4 else 1

    return c + cost

  def h(self, node):
    """
    h(n) = Sum of the horizontal and vertical distances to reach the goal
    Manhattan distance
    """
    y1, x1 = node.mario
    y2, x2 = self.princess

    return abs(x2 - x1) + abs(y2 - y1)

  @classmethod
  def find_position(self, state, object):
    matriz = np.array(state)
    p = np.where(matriz==object)
    return (p[0][0], p[1][0])

  @classmethod
  def check_position(self, state, x, y):
    return state[y][x]

  @classmethod
  def next_position(self, mario, action):
    position = tuple()

    y = mario[0]
    x = mario[1]

    if action == 'Up': position = (y - 1, x)
    elif action == 'Down': position = (y + 1, x)
    elif action == 'Left': position = (y, x - 1)
    elif action == 'Right': position = (y, x + 1)
    else: position = (y, x)

    return position




