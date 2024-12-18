import numpy as np, queue as q, sys
np.set_printoptions(linewidth=1000)

maze = np.array([list(line) for line in open('maze.txt').read().split('\n')], np.dtype('U4'))
maze_b = maze.copy()

start_index = np.nonzero(maze == 'S')
start_index = (start_index[0][0].item(), start_index[1][0].item())
end_index = np.nonzero(maze == 'E')
end_index = (end_index[0][0].item(), end_index[1][0].item())

def get_next_points(index):
  points = []
  if maze[index[0]-1, index[1]] == '.' or maze[index[0]-1, index[1]] == 'E': # up
    points.append(((index[0]-1, index[1]), 0))
    maze[index[0]-1, index[1]] = 'X'
  if maze[index[0], index[1]+1] == '.' or maze[index[0], index[1]+1] == 'E': # right
    points.append(((index[0], index[1]+1), 1))
    maze[index[0], index[1]+1] = 'X'
  if maze[index[0]+1, index[1]] == '.' or maze[index[0]+1, index[1]] == 'E': # down
    points.append(((index[0]+1, index[1]), 2))
    maze[index[0]+1, index[1]] = 'X'
  if maze[index[0], index[1]-1] == '.' or maze[index[0], index[1]-1] == 'E': # left
    points.append(((index[0], index[1]-1), 3))
    maze[index[0], index[1]-1] = 'X'
  return points

def get_next_points_b(index, steps):
  points = []
  steps = str(steps).zfill(2)
  print(maze[index[0]-1, index[1]] == str(steps), index, steps, maze[index[0]-1, index[1]])
  if maze[index[0]-1, index[1]] == '.' or maze[index[0]-1, index[1]] == str(steps) or maze[index[0]-1, index[1]] == 'E': # up
    points.append(((index[0]-1, index[1]), 0))
    maze[index[0]-1, index[1]] = steps
  if maze[index[0], index[1]+1] == '.' or maze[index[0], index[1]+1] == str(steps) or maze[index[0], index[1]+1] == 'E': # right
    points.append(((index[0], index[1]+1), 1))
    maze[index[0], index[1]+1] = steps
  if maze[index[0]+1, index[1]] == '.' or maze[index[0]+1, index[1]] == str(steps) or maze[index[0]+1, index[1]] == 'E': # down
    points.append(((index[0]+1, index[1]), 2))
    maze[index[0]+1, index[1]] = steps
  if maze[index[0], index[1]-1] == '.' or maze[index[0], index[1]-1] == str(steps) or maze[index[0], index[1]-1] == 'E': # left
    points.append(((index[0], index[1]-1), 3))
    maze[index[0], index[1]-1] = steps
  return points

min_score = 0
# A* my beloved
frontier = q.PriorityQueue()
frontier.put((0, (start_index, 1))) # (score, (index, direction)) bc priority queue requires input as (score, data)
while not frontier.empty():
  current_index = frontier.get()
  if current_index[1][0] == end_index:
    min_score = current_index[0]
    break
  for point in get_next_points(current_index[1][0]):
    step_score = 1 + current_index[0] if point[1] == current_index[1][1] else 1001 + current_index[0]
    frontier.put((step_score, (point[0], point[1])))
print(min_score)

# dfs with depth limiting based on score
maze = maze_b
# frontier = q.LifoQueue()
# frontier.put((0, (start_index, 1, []))) # (score, (index, direction, [visited points]))
# best_path_points = {start_index}
# while not frontier.empty():
#   current_index = frontier.get()
#   if current_index[1][0] == end_index:
#     best_path_points.update(current_index[1][2])
#   elif current_index[0] > min_score:
#     continue
#   for point in get_next_points_b(current_index[1][0]):
#     if point[0] not in current_index[1][2]:
#       visited = current_index[1][2].copy()
#       visited.append(current_index[1][0])
#       step_score = 1 + current_index[0] if point[1] == current_index[1][1] else 1001 + current_index[0]
#       frontier.put((step_score, (point[0], point[1], visited)))
#   print(visited, frontier.qsize(), current_index[0])
# print(len(best_path_points)+1) # we accidentally don't count the end node as visited

frontier = q.PriorityQueue()
frontier.put((0, (start_index, 1, 1, []))) # (score, (index, direction)) bc priority queue requires input as (score, data)
best_path_points = {}
while not frontier.empty():
  current_index = frontier.get()
  if current_index[1][0] == end_index:
    print(current_index[1][3])
    best_path_points = set(current_index[1][3])
    break
  for point in get_next_points_b(current_index[1][0], current_index[1][2]):
    visited = current_index[1][3].copy()
    visited.append(current_index[1][0])
    step_score = 1 + current_index[0] if point[1] == current_index[1][1] else 1001 + current_index[0]
    frontier.put((step_score, (point[0], point[1], current_index[1][2] + 1, visited)))
  
with open('output_file.txt', 'w') as writer:
  for i in range(len(maze)):
    np.putmask(maze[i], maze[i] == '#', ['##'])
    np.putmask(maze[i], maze[i] == '.', ['..'])
    string = np.array2string(maze[i]) + '\n'
    writer.write(string)

print(len(best_path_points), best_path_points)
while not frontier.empty():
  current_index = frontier.get()
  if current_index[0] == min_score:
    print(current_index[1][3])
    best_path_points = best_path_points.union(set(current_index[1][3]))
  else:
    print(current_index[1][0])

print(len(best_path_points)+1)

# 546 low
# 665

+ 21 + 3