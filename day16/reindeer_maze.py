import numpy as np, queue as q
maze = np.array([list(line) for line in open('maze.txt').read().split('\n')], np.dtype('U4'))

# get our start/end points and replace them with the empty space character
start_index = np.nonzero(maze == 'S')
start_index = (start_index[0][0].item(), start_index[1][0].item()) # if you remove this line, numpy gives a deprecation warning
maze[start_index] = '.'
end_index = np.nonzero(maze == 'E')
end_index = (end_index[0][0].item(), end_index[1][0].item()) # i love/h8 numpy
maze[end_index] = '.'

def get_next_points(index, steps):
  points = []
  mi = [(index[0]-1, index[1]), (index[0], index[1]+1), (index[0]+1, index[1]), (index[0], index[1]-1)] # t shape directions
  for i in range(len(mi)):
    # '.' means the index hasn't been visited yet, otherwise there should be a wall we don't turn into 
    # or a number corresponding to the step it was visited on. if our current step is less than the next index,
    # we still add it to the frontier bc A* may have searched further on a different index bc of the turn score heuristic
    if maze[mi[i]] == '.' or maze[mi[i]] != '#' and int(maze[mi[i]]) >= steps:
      points.append((mi[i], i))
      maze[mi[i]] = steps
  return points

min_score = 0
best_path_points = {}

frontier = q.PriorityQueue()
frontier.put((0, (start_index, 1, 1, []))) # (score, (index, direction, steps, visited))

# A* my beloved
while not frontier.empty():
  current_index = frontier.get()
  if current_index[1][0] == end_index:
    min_score = current_index[0]
    best_path_points = set(current_index[1][3])
    break
  for point in get_next_points(current_index[1][0], current_index[1][2]):
    visited = current_index[1][3].copy()
    visited.append(current_index[1][0])
    step_score = 1 + current_index[0] if point[1] == current_index[1][1] else 1001 + current_index[0]
    frontier.put((step_score, (point[0], point[1], current_index[1][2] + 1, visited)))

# the next n steps on the frontier should also be the end point, so we should check if their score is equal to the lowest
# if it is, its a valid path, and we add its visited point to the set of best path points. 
# Otherwise, min priority queue means anything after is too long, so we'll skip the rest
while not frontier.empty():
  current_index = frontier.get()
  if current_index[0] == min_score:
    best_path_points = best_path_points.union(set(current_index[1][3]))
  else:
    break

print(min_score)
print(len(best_path_points)+1)