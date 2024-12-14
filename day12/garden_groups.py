import numpy as np, queue as q

garden_map = np.array([list(line) for line in open('garden_plots.txt').read().split('\n')])
visited_plants = np.zeros(garden_map.shape)

def get_total_sides(plant_shape):
  sides = 0
  for k in range(4):
    need_new_side = True
    for i in range(len(plant_shape)):
      for j in range(len(plant_shape[0])):
        if need_new_side and plant_shape[i][j] != '.':
          if i == 0 or plant_shape[i-1][j] == '.':
            sides += 1
            need_new_side = False
        elif plant_shape[i][j] == '.' or (i != 0 and plant_shape[i-1][j] != '.'):
          need_new_side = True
    plant_shape = np.rot90(plant_shape)
  return sides

def get_neighbor_plants(index):
  current_plant = garden_map[index]
  perimeter_price = 0
  neighbors = []
  if index[0] != 0 and garden_map[index[0]-1][index[1]] == current_plant: # up
    perimeter_price += 1
    if visited_plants[index[0]-1][index[1]] == 0: # up
      neighbors.append((index[0]-1, index[1]))
      visited_plants[(index[0]-1, index[1])] = 1
  if index[1] < len(garden_map[0])-1 and garden_map[index[0]][index[1]+1] == current_plant:
    perimeter_price += 1
    if visited_plants[index[0]][index[1]+1] == 0: # left
      neighbors.append((index[0], index[1]+1))
      visited_plants[(index[0], index[1]+1)] = 1
  if index[0] < len(garden_map)-1 and garden_map[index[0]+1][index[1]] == current_plant:
    perimeter_price += 1
    if visited_plants[index[0]+1][index[1]] == 0: # down
      neighbors.append((index[0]+1, index[1]))
      visited_plants[(index[0]+1, index[1])] = 1
  if index[1] != 0 and garden_map[index[0]][index[1]-1] == current_plant:
    perimeter_price += 1 
    if visited_plants[index[0]][index[1]-1] == 0: # right
      neighbors.append((index[0], index[1]-1))
      visited_plants[(index[0], index[1]-1)] = 1
  return neighbors, perimeter_price

def get_parameters(index):
  area = 0
  perimeter = 0
  frontier = q.Queue()
  frontier.put(index)
  visited_plants[index] = 1
  current_plant = garden_map[index]
  plant_graph = np.full(garden_map.shape, '.', dtype=str)
  plant_graph[index] = current_plant
  while not frontier.empty():
    current_index = frontier.get()
    neighbors, edges = get_neighbor_plants(current_index)
    for neighbor in neighbors:
      frontier.put(neighbor)
    area += 1
    perimeter += 4-edges
    plant_graph[current_index] = current_plant
  sides = get_total_sides(plant_graph)
  return area * perimeter, area * sides

price_a = 0
price_b = 0
for i in range(len(garden_map)):
  for j in range(len(garden_map[0])):
    if visited_plants[i][j] == 0:
      per_price, side_price = get_parameters((i,j))
      price_a += per_price
      price_b += side_price
print(price_a)
print(price_b)