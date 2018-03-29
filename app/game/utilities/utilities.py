
from time import time

def format_data(str):
  """
  Gives the required format to load a game scene
  """
  tmp = [a.split(' ') for a in str.split('\n')][:-1]

  # insert limits left - right
  for row in tmp:
    row.insert(0,'1')
    row.append('1')
  # insert limits up - down
  limit = ['1']*len(tmp[0])
  tmp.insert(0, limit)
  tmp.append(limit)

  # join the arr
  tmp = ['[{}]'.format(','.join(row)) for row in tmp]
  return '[{}]'.format(',\n'.join(tmp))

def flat_slice(lst):
  """
  Flatten a list
  """
  lst = list(lst)
  for i, _ in enumerate(lst):
    while (hasattr(lst[i], "__iter__") and not isinstance(lst[i], basestring)):
      lst[i:i + 1] = lst[i]
  return lst

