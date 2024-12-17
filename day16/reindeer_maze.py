import numpy as np, queue as q

maze = np.array([list(line) for line in open('maze.txt').read().split('\n')])
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
  if maze[index[0], index[1]+1] == '.' or maze[index[0], index[1]+1] == '.': # right
    points.append(((index[0], index[1]+1), 1))
    maze[index[0], index[1]+1] = 'X'
  if maze[index[0]+1, index[1]] == '.' or maze[index[0]+1, index[1]] == '.': # down
    points.append(((index[0]+1, index[1]), 2))
    maze[index[0]+1, index[1]] = 'X'
  if maze[index[0], index[1]-1] == '.' or maze[index[0], index[1]-1] == '.': # left
    points.append(((index[0], index[1]-1), 3))
    maze[index[0], index[1]-1] = 'X'
  return points

frontier = q.PriorityQueue()
frontier.put((0, (start_index, 1))) # (score, (index, direction)) bc priority queue requires input as (score, data)
while not frontier.empty():
  current_index = frontier.get()
  if current_index[1][0] == end_index:
    print(current_index[0])
    break
  for point in get_next_points(current_index[1][0]):
    step_score = 1 + current_index[0] if point[1] == current_index[1][1] else 1001 + current_index[0]
    frontier.put((step_score, (point[0], point[1])))
