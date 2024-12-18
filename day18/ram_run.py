import numpy as np, queue as q
map = np.full((71,71), '.')

bites = open('falling_bytes.txt').readlines()
for i in range(1024):
  bite = bites[i].split(',')
  map[int(bite[1]), int(bite[0])] = '#'

start_index = (0,0)
end_index = (70,70)

def get_next_points(index):
  points = []
  mi = [(index[0]-1, index[1]), (index[0], index[1]+1), (index[0]+1, index[1]), (index[0], index[1]-1)] # t shape directions
  for i in range(len(mi)):
    if mi[i][0] != -1 and mi[i][1] != -1 and mi[i][0] != len(map) and mi[i][1] != len(map[0]):
      if map[mi[i]] != 'X' and map[mi[i]] != '#':
        points.append(mi[i])
        map[mi[i]] = 'X'
  return points

frontier = q.Queue()
frontier.put((start_index, 0))
while not frontier.empty():
  current_index = frontier.get()
  if current_index[0] == end_index:
    print(current_index[1])
    break
  for point in get_next_points(current_index[0]):
    frontier.put((point, current_index[1] + 1))