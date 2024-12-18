import numpy as np, queue as q
map = np.full((71,71), '.')

bites = open('falling_bytes.txt').read().split('\n')
for i in range(1024):
  bite = bites[i].split(',')
  map[int(bite[1]), int(bite[0])] = '#'
map_holder = map.copy()

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

def get_shortest_path():
  frontier = q.Queue()
  frontier.put((start_index, 0))
  while not frontier.empty():
    current_index = frontier.get()
    if current_index[0] == end_index:
      return current_index[1]
    for point in get_next_points(current_index[0]):
      frontier.put((point, current_index[1] + 1))
  return -1
# part a
print(get_shortest_path())

for i in range(1024, len(bites)):
  map = map_holder
  bite = bites[i].split(',')
  map[int(bite[1]), int(bite[0])] = '#'
  map_holder = map.copy()
  if get_shortest_path() == -1:
    # part b
    print(bites[i])
    break