import numpy as np

map, directions = open('goods_positioning_system.txt').read().split('\n\n')
map_b = np.array([list(a.replace('.', '..').replace('@', '@.').replace('#', '##').replace('O', '[]')) for a in map.split('\n')])
map = np.array([list(a) for a in map.split('\n')])

initial_index_a = np.nonzero(map == '@')
index_a = (initial_index_a[0][0].item(), initial_index_a[1][0].item())
initial_index_b = np.nonzero(map_b == '@')
index_b = (initial_index_b[0][0].item(), initial_index_b[1][0].item())

def move_boxes(direction, index):
  if direction == '^':
    if index[0] == 1 or map[index[0]-1, index[1]] == '#': # wall
      return index
    elif map[index[0]-1, index[1]] == '.': # empty space
      map[index] = '.'
      map[index[0]-1, index[1]] = '@'
      return (index[0]-1, index[1])
    else:
      for i in range(len(map[:index[0],index[1]])):
        if map[index[0]-i-1][index[1]] == '#':
          return index
        elif map[index[0]-i-1][index[1]] == '.':
          map[index] = '.'
          map[index[0]-1, index[1]] = '@'
          map[index[0]-i-1, index[1]] = 'O'
          return (index[0]-1, index[1])
  elif direction == '>':
    if index[1] == len(map)-1 or map[index[0], index[1]+1] == '#':
      return index
    elif map[index[0], index[1]+1] == '.':
      map[index] = '.'
      map[index[0], index[1]+1] = '@'
      return (index[0], index[1]+1)
    else:
      for i in range(len(map[index[0],index[1]:])):
        if map[index[0]][index[1]+i] == '#':
          return index
        elif map[index[0]][index[1]+i] == '.':
          map[index] = '.'
          map[index[0], index[1]+1] = '@'
          map[index[0], index[1]+i] = 'O'
          return (index[0], index[1]+1)
  elif direction == 'v':
    if index[0] == len(map[0])-1 or map[index[0]+1, index[1]] == '#':
      return index
    elif map[index[0]+1, index[1]] == '.':
      map[index] = '.'
      map[index[0]+1, index[1]] = '@'
      return (index[0]+1, index[1])
    else:
      for i in range(len(map[index[0]:,index[1]])):
        if map[index[0]+i][index[1]] == '#':
          return index
        elif map[index[0]+i][index[1]] == '.':
          map[index] = '.'
          map[index[0]+1, index[1]] = '@'
          map[index[0]+i, index[1]] = 'O'
          return (index[0]+1, index[1])
  else: # '<'
    if index[1] == 1 or map[index[0], index[1]-1] == '#':
      return index
    elif map[index[0], index[1]-1] == '.':
      map[index] = '.'
      map[index[0], index[1]-1] = '@'
      return (index[0], index[1]-1)
    else:
      for i in range(len(map[index[0],:index[1]])):
        if map[index[0]][index[1]-i-1] == '#':
          return index
        elif map[index[0]][index[1]-i-1] == '.':
          map[index] = '.'
          map[index[0], index[1]-1] = '@'
          map[index[0], index[1]-i-1] = 'O'
          return (index[0], index[1]-1)

def is_free_below(index):
  pair_index = ()
  if map_b[index] == '.':
    return True
  elif map_b[index] == '[':
    pair_index = (index[0], index[1]+1)
  else:
    pair_index = (index[0], index[1]-1)
  if map_b[index[0]+1, index[1]] == '#' or map_b[pair_index[0]+1, pair_index[1]] == '#': # either side of box is walled below
    return False
  elif map_b[index[0]+1, index[1]] == '.' and map_b[pair_index[0]+1, pair_index[1]] == '.': # both sides of box are free below
    return True
  else: # check if the next boxes above are free or blocked
    return is_free_below((index[0]+1, index[1])) and is_free_below((pair_index[0]+1, pair_index[1]))

def move_boxes_down(index):
  if map_b[index] == '.':
    return
  pair_index = ()
  if map_b[index] == '[':
    pair_index = (index[0], index[1]+1)
  else:
    pair_index = (index[0], index[1]-1)
  if map_b[index[0]+1, index[1]] == '.' and map_b[pair_index[0]+1, pair_index[1]] == '.':
    map_b[index[0]+1, index[1]] = map_b[index[0], index[1]]
    map_b[pair_index[0]+1, pair_index[1]] = map_b[pair_index[0], pair_index[1]]
    map_b[index] = '.'
    map_b[pair_index] = '.'
  else:
    move_boxes_down((index[0]+1, index[1]))
    move_boxes_down((pair_index[0]+1, pair_index[1]))
    map_b[index[0]+1, index[1]] = map_b[index[0], index[1]]
    map_b[pair_index[0]+1, pair_index[1]] = map_b[pair_index[0], pair_index[1]]
    map_b[index] = '.'
    map_b[pair_index] = '.'

def is_free_above(index):
  pair_index = ()
  if map_b[index] == '.':
    return True
  elif map_b[index] == '[':
    pair_index = (index[0], index[1]+1)
  else:
    pair_index = (index[0], index[1]-1)
  if map_b[index[0]-1, index[1]] == '#' or map_b[pair_index[0]-1, pair_index[1]] == '#': # either side of box is walled below
    return False
  elif map_b[index[0]-1, index[1]] == '.' and map_b[pair_index[0]-1, pair_index[1]] == '.': # both sides of box are free below
    return True
  else: # check if the next boxes above are free or blocked
    return is_free_above((index[0]-1, index[1])) and is_free_above((pair_index[0]-1, pair_index[1]))

def move_boxes_up(index):
  if map_b[index] == '.':
    return
  pair_index = ()
  if map_b[index] == '[':
    pair_index = (index[0], index[1]+1)
  else:
    pair_index = (index[0], index[1]-1)
  if map_b[index[0]-1, index[1]] == '.' and map_b[pair_index[0]-1, pair_index[1]] == '.':
    map_b[index[0]-1, index[1]] = map_b[index[0], index[1]]
    map_b[pair_index[0]-1, pair_index[1]] = map_b[pair_index[0], pair_index[1]]
    map_b[index] = '.'
    map_b[pair_index] = '.'
  else:
    move_boxes_up((index[0]-1, index[1]))
    move_boxes_up((pair_index[0]-1, pair_index[1]))
    map_b[index[0]-1, index[1]] = map_b[index[0], index[1]]
    map_b[pair_index[0]-1, pair_index[1]] = map_b[pair_index[0], pair_index[1]]
    map_b[index] = '.'
    map_b[pair_index] = '.'

def move_big_boxes(direction, index):
  if direction == '^':
    if index[0] == 1 or map_b[index[0]-1, index[1]] == '#':# wall
      return index
    elif map_b[index[0]-1, index[1]] == '.': # empty space
      map_b[index] = '.'
      map_b[index[0]-1, index[1]] = '@'
      return (index[0]-1, index[1])
    else: # boxes :(
      if not is_free_above((index[0]-1,index[1])):
        return index
      else:
        move_boxes_up((index[0]-1, index[1]))
        map_b[index] = '.'
        map_b[index[0]-1, index[1]] = '@'
        return (index[0]-1, index[1])
  elif direction == '>': # handled (mostly) the same as part a
    if index[1] == 1 or map_b[index[0], index[1]+1] == '#':
      return index
    elif map_b[index[0], index[1]+1] == '.':
      map_b[index] = '.'
      map_b[index[0], index[1]+1] = '@'
      return (index[0], index[1]+1)
    else:
      for i in range(len(map_b[index[0],index[1]:])):
        if map_b[index[0]][index[1]+i] == '#':
          return index
        elif map_b[index[0]][index[1]+i] == '.':
          holder = map_b[index[0], index[1]:index[1]+i].copy()
          np.put(map_b[index[0]], range(index[1]+1, index[1]+i+1), holder)
          map_b[index] = '.'
          map_b[index[0], index[1]+1] = '@'
          return (index[0], index[1]+1)
  elif direction == 'v':
    if index[0] == len(map_b[0])-1 or map_b[index[0]+1, index[1]] == '#':# wall
      return index
    elif map_b[index[0]+1, index[1]] == '.': # empty space
      map_b[index] = '.'
      map_b[index[0]+1, index[1]] = '@'
      return (index[0]+1, index[1])
    else: # boxes :(
      if not is_free_below((index[0]+1,index[1])):
        return index
      else:
        move_boxes_down((index[0]+1, index[1]))
        map_b[index] = '.'
        map_b[index[0]+1, index[1]] = '@'
        return (index[0]+1, index[1])
  else: # '<'
    if index[1] == 1 or map_b[index[0], index[1]-1] == '#':
      return index
    elif map_b[index[0], index[1]-1] == '.':
      map_b[index] = '.'
      map_b[index[0], index[1]-1] = '@'
      return (index[0], index[1]-1)
    else:
      for i in range(len(map_b[index[0],:index[1]])):
        if map_b[index[0]][index[1]-i-1] == '#':
          return index
        elif map_b[index[0]][index[1]-i-1] == '.':
          holder = map_b[index[0], index[1]-i:index[1]].copy()
          np.put(map_b[index[0]], range(index[1]-i-1, index[1]-1), holder)
          map_b[index] = '.'
          map_b[index[0], index[1]-1] = '@'
          return (index[0], index[1]-1)

directions = directions.replace('\n', '') # live laugh love debugging \n
for direction in directions:
  index_a = move_boxes(direction, index_a)
  index_b = move_big_boxes(direction, index_b)

small_box_coordinates = 0
boxes = np.nonzero(map == 'O')
for i in range(len(boxes[0])):
  small_box_coordinates += boxes[0][i]* 100 + boxes[1][i]
print(small_box_coordinates)

large_box_coordinates = 0
boxes = np.nonzero(map_b == '[')
for i in range(len(boxes[0])):
  large_box_coordinates += boxes[0][i]* 100 + boxes[1][i]
print(large_box_coordinates)