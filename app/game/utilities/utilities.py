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
