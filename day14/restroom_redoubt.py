import re, math, numpy as np, sys
lines = open('robot_movements.txt').readlines()
np.set_printoptions(threshold=sys.maxsize, linewidth=100000)

# when i first looked at the problem i saw this shape and said to myself:
# "huh, they're both prime. i wonder if that'll be relevant"
# (spoilers, they were!)
grid_shape = (101, 103)
def calculate_next_position(position, velocity):
  x = (position[0] + velocity[0]) % grid_shape[0]
  y = (position[1] + velocity[1]) % grid_shape[1]
  return x, y

def get_safety_factor(positions):
  mids = (grid_shape[0]//2, grid_shape[1]//2)
  quads = [0,0,0,0]
  for robot in positions:
    if robot[0] < mids[0] and robot[1] < mids[1]: # quad 1
      quads[0] += 1
    elif robot[0] > mids[0] and robot[1] < mids[1]: # quad 2
      quads[1] += 1
    elif robot[0] > mids[0] and robot[1] > mids[1]: # quad 3
      quads[2] += 1
    elif robot[0] < mids[0] and robot[1] > mids[1]: # quad 4
      quads[3] += 1
  return math.prod(quads)

def print_easter_egg(positions):
  pretty_pictures = np.full((101, 103), '🎁')
  for i in range(len(positions)):
    pretty_pictures[positions[i]] = '🌲'
  for line in pretty_pictures:
      print(''.join(str(x) for x in line))
  
positions = []
velocities = []
for line in lines:
  info = re.match(r"p=(\d*,\d*) v=(-?\d*,-?\d*)", line)
  positions.append([int(i) for i in info.group(1).split(',')])
  velocities.append([int(i) for i in info.group(2).split(',')])

j = 0
while True:
  for i in range(len(positions)):
    positions[i] = calculate_next_position(positions[i], velocities[i])
  if j == 99:
    print(get_safety_factor(positions))
  j += 1
  # after looking through ~500 manual renders of the robots positioning, we start to notice a pattern
  # where there are vertical lines appearing every 103 iters and horizontal lines appearing every 101 iters
  # considering those are the size of the robots enclosure, we can do some trick math
  # and figure out where the lined patterns overlap
  if j % 103 == 78 and j % 101 == 8:
    print_easter_egg(positions)
    print(j)
    break