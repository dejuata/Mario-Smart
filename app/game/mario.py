#!/usr/bin/python
# -*- coding: utf-8 -*-
# Basado en https://www.cs.us.es/cursos/iati-2012/
import numpy as np
from copy import copy, deepcopy
from utilities.utilities import flat_slice


class MarioSmart(object):

  def __init__(self, initial, goal=None):
    self.initial = initial
    self.goal = goal
    self.inmune = False

  def actions(self, state):
    """
    Return the actions that can be executed in the given state
    """
    possible_actions = ['UP', 'DOWN', 'LEFT', 'RIGHT']
    # [y, x]
    mario = self.find_position(state, 2)

    x = mario[1]
    y = mario[0]

    # check the free roads
    # UP
    if self.check_position(state=state, x=x, y=y-1) == 1:
      possible_actions.remove('UP')
    # DOWN
    if self.check_position(state=state, x=x, y=y+1) == 1:
      possible_actions.remove('DOWN')
    # LEFT
    if self.check_position(state=state, x=x-1, y=y) == 1:
      possible_actions.remove('LEFT')
    # RIGHT
    if self.check_position(state=state, x=x+1, y=y) == 1:
      possible_actions.remove('RIGHT')

    return possible_actions

  def result_of_actions(self, state, action):
    """
    Return the new state that results from executing the action in the given state
    """
    mario = self.find_position(state, 2)
    x = mario[1]
    y = mario[0]
    new_state = deepcopy(state)

    position = self.next_position(y=y, x=x, action=action)

    new_state[y][x] = 0
    new_state[position[0]][position[1]] = 2
    # print(id(state), id(new_state))
    # print(state, new_state)
    return new_state

  def goal_test(self, state):
    """
    Return True if the state is a goal
    """
    return state == self.goal

  def path_cost(self, c, state1, action, state2):
    """
    Return the cost of a solution path that arrives at state2 from
    state1 via action, assuming cost c to get up to state1.
    """
    mario = self.find_position(state1, 2)
    x = mario[1]
    y = mario[0]
    position = self.next_position(y=y, x=x, action=action)
    check = self.check_position(state=state1, y=position[0], x=position[1])

    self.inmune = True if check == 3 else False

    cost = 1
    if self.inmune:
      cost = 1
    elif check == 4:
      cost = 7

    return c + cost

  @classmethod
  def find_position(self, state, object):
    matriz = np.array(state)
    position = list(map(list, np.where(matriz==object)))
    return flat_slice(position)

  @classmethod
  def check_position(self, state, x, y):
    return state[y][x]

  @classmethod
  def next_position(self, y, x, action):
    position = list()

    if action == 'UP':
      position = [y - 1, x]
    elif action == 'DOWN':
      position = [y + 1, x]
    elif action == 'LEFT':
      position = [y, x - 1]
    elif action == 'RIGHT':
      position = [y, x + 1]

    return position
