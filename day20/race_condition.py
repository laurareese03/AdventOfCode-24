import numpy as np, queue as q
maze = np.array([list(i) for i in open('racetrack.txt').read().split('\n')])

start_index = np.nonzero(maze == 'S')
start_index = (start_index[0][0].item(), start_index[1][0].item())
maze[start_index] = '.'
end_index = np.nonzero(maze == 'E')
end_index = (end_index[0][0].item(), end_index[1][0].item())
maze[end_index] = '.'

path = []
# get a list of all points we hit during a full race
def build_path(start_index, end_index):
  frontier = q.Queue()
  frontier.put(start_index)
  visited = []
  while not frontier.empty():
    curr = frontier.get()
    visited.append(curr)
    if curr == end_index:
      return visited
    next_points = [(curr[0]+1, curr[1]), (curr[0]-1, curr[1]), (curr[0], curr[1]-1), (curr[0], curr[1]+1)]
    for i in range(len(next_points)):
      if maze[next_points[i]] == '.' and next_points[i] not in visited:
        frontier.put(next_points[i])

longest_path = build_path(start_index, end_index)

count = 0
directions = [(0,1), (0,-1), (1,0), (-1,0)] # we definitely don't need to check them all but I can't think rn
for i in range(len(longest_path)):
  step = longest_path[i]
  for direction in directions:
    two_step = (step[0]+2*direction[0], step[1]+2*direction[1])
    two_step_valid = np.all(((0,0) <= two_step) & (two_step < maze.shape)) # check if 2 steps away is in 
    if maze[step[0]+direction[0], step[1]+direction[1]] == '#' and two_step_valid:
      index = -1
      try:
        index = longest_path[i:].index(two_step)
        if index-2 >= 100:
          count += 1
      except ValueError: # why does index have to error if the element isn't in the list??
        index = -1
print(count)

# b
# find all future points that are within 20 blocks of the current point?
# they have to be exclusively connected by walls though so that reduces the number at lease?