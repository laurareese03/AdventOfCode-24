import numpy as np, queue as q

garden_map = np.array([list(line) for line in open('garden_plots.txt').read().split('\n')])
visited_plants = np.zeros(garden_map.shape)

def get_neighbor_plants(index):
  current_plant = garden_map[index]
  perimeter_count = 0
  neighbors = []
  if index[0] != 0 and garden_map[index[0]-1][index[1]] == current_plant: # up
    perimeter_count += 1
    if visited_plants[index[0]-1][index[1]] == 0: # up
      neighbors.append((index[0]-1, index[1]))
      visited_plants[(index[0]-1, index[1])] = 1
  if index[1] < len(garden_map[0])-1 and garden_map[index[0]][index[1]+1] == current_plant:
    perimeter_count += 1
    if visited_plants[index[0]][index[1]+1] == 0: # left
      neighbors.append((index[0], index[1]+1))
      visited_plants[(index[0], index[1]+1)] = 1
  if index[0] < len(garden_map)-1 and garden_map[index[0]+1][index[1]] == current_plant:
    perimeter_count += 1
    if visited_plants[index[0]+1][index[1]] == 0: # down
      neighbors.append((index[0]+1, index[1]))
      visited_plants[(index[0]+1, index[1])] = 1
  if index[1] != 0 and garden_map[index[0]][index[1]-1] == current_plant:
    perimeter_count += 1 
    if visited_plants[index[0]][index[1]-1] == 0: # right
      neighbors.append((index[0], index[1]-1))
      visited_plants[(index[0], index[1]-1)] = 1
  return neighbors, perimeter_count

def get_parameters(index):
  area = 0
  perimeter = 0
  frontier = q.Queue()
  frontier.put(index)
  visited_plants[index] = 1
  while not frontier.empty():
    current_index = frontier.get()
    neighbors, edges = get_neighbor_plants(current_index)
    for neighbor in neighbors:
      frontier.put(neighbor)
    area += 1
    perimeter += 4-edges

  return area * perimeter

count = 0
for i in range(len(garden_map)):
  for j in range(len(garden_map[0])):
    if visited_plants[i][j] == 0:
      count += get_parameters((i,j))
print(count)