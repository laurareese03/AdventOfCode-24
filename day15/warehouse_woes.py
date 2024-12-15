import numpy as np

map, directions = open('goods_positioning_system.txt').read().split('\n\n')
map = np.array([list(a) for a in map.split('\n')])

initial_index = np.nonzero(map == '@')
index = (initial_index[0][0].item(), initial_index[1][0].item())

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
        print(map[index[0],:index[1]])
        if map[index[0]][index[1]-i-1] == '#':
          return index
        elif map[index[0]][index[1]-i-1] == '.':
          map[index] = '.'
          map[index[0], index[1]-1] = '@'
          map[index[0], index[1]-i-1] = 'O'
          return (index[0], index[1]-1)

directions = directions.replace('\n', '') # live laugh love debugging \n
for direction in directions:
  index = move_boxes(direction, index)

coordinates = 0
boxes = np.nonzero(map == 'O')
for i in range(len(boxes[0])):
  coordinates += boxes[0][i]* 100 + boxes[1][i]

print(coordinates)