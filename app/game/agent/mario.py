#!/usr/bin/python
# -*- coding: utf-8 -*-
# Basado en https://www.cs.us.es/cursos/iati-2012/
from copy import deepcopy
from game.utilities.utilities import find_position


class MarioSmart(object):

  def __init__(self, initial, goal=None):
    self.initial = initial
    self.goal = goal
    self.princess = find_position(self.initial, 5)

  def actions(self, state, mario):
    """
    Return the actions that can be executed in the given state
    """
    possible_actions = ['up', 'down', 'left', 'right']

    x = mario[1]
    y = mario[0]

    # check the free roads
    # UP
    if self.check_position(state=state, x=x, y=y-1) == 1:
      possible_actions.remove('up')
    # DOWN
    if self.check_position(state=state, x=x, y=y+1) == 1:
      possible_actions.remove('down')
    # LEFT
    if self.check_position(state=state, x=x-1, y=y) == 1:
      possible_actions.remove('left')
    # RIGHT
    if self.check_position(state=state, x=x+1, y=y) == 1:
      possible_actions.remove('right')

    return possible_actions

  def result_of_actions(self, state, action, mario):
    """
    Return the new state that results from executing the action in the given state
    """
    x, y = mario[1], mario[0]
    new_state = deepcopy(state[0])
    position = self.next_position(mario, action)
    old_position = self.initial[y][x]

    if old_position == 2:
      new_state[y][x] = 0
    elif state[1] or state[2]:
      new_state[y][x] = 0
    elif state[2] and old_position == 8:
      new_state[y][x] = 0
    else:
      new_state[y][x] = old_position

    new_state[position[0]][position[1]] = 2

    check = self.check_position(state=state[0], y=position[0], x=position[1])

    if  check == 3:
      return new_state, True

    if check == 9:
      return [new_state, True]

    return new_state

  def goal_test(self, mario):
    """
    Return True if the state is a goal
    """
    return self.princess == mario

  def path_cost(self, c, state, action, mario, inmune, start):
    """
    Return the cost of a solution path that arrives at state
    via action, assuming cost c to get up to state.
    """
    position = self.next_position(mario, action)
    check = self.check_position(state=state, y=position[0], x=position[1])
    cost = 1
    if check == 4 and not inmune and not start:
      cost = 7
    if check == 8 and not start:
      cost = 100

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
  def check_position(self, state, x, y):
    return state[y][x]

  @classmethod
  def next_position(self, mario, action):
    position = tuple()

    y = mario[0]
    x = mario[1]

    if action == 'up': position = (y - 1, x)
    elif action == 'down': position = (y + 1, x)
    elif action == 'left': position = (y, x - 1)
    elif action == 'right': position = (y, x + 1)
    else: position = (y, x)

    return position



