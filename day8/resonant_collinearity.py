import numpy as np, sys
np.set_printoptions(threshold=sys.maxsize, linewidth=1000)

inp = open('antenna.txt').read()

grid = np.array([list(i) for i in inp.split('\n')])
anti = set()

antenna_type = set(list(inp))
antenna_type.remove('.')
antenna_type.remove('\n')

def get_line_distance(p1, p2):
  return p2[0] - p1[0], p2[1] - p1[1]

for antennas in antenna_type:
  posts = np.nonzero(grid == antennas)
  grid2 = np.full([len(grid), len(grid[0])], '.', dtype=str)
  current_ant_points = set()
  for i in range(len(posts[0])-1):
    for j in range(i+1,len(posts[0])):
      vert, horz = get_line_distance((posts[0][i], posts[1][i]), (posts[0][j], posts[1][j]))
      print(vert, horz)
      if vert % 3 == 0 and horz % 3 == 0:
        print('here')
      if posts[0][j] + vert < len(grid) and posts[0][j] + vert >= 0 and posts[1][j] + horz < len(grid[0]) and posts[1][j] + horz >= 0:
        current_ant_points.add(((posts[0][j] + vert).item(), (posts[1][j] + horz).item()))
      if posts[0][i] - vert >= 0 and posts[0][i] - vert < len(grid) and posts[1][i] - horz >= 0 and posts[1][i] - horz < len(grid):
        print(posts[0][i] - vert,posts[1][i] - horz, 'check negs')
        current_ant_points.add(((posts[0][i] - vert).item(), (posts[1][i] - horz).item()))

  anti = anti.union(current_ant_points)

print(len(anti))
