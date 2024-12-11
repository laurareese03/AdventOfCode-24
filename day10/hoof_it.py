import numpy as np
map = np.array([list(line) for line in open('topographic_map.txt').read().split('\n')])
map = np.astype(map, int)
indices = np.nonzero(map == 0)

def check_surrounding_indexes(index, depth):
  valid_indexes = []
  if index[0] - 1 >= 0: # up
    if map[index[0]-1, index[1]] == depth:
      valid_indexes.append((index[0]-1, index[1]))
  if index[1] - 1 >= 0: # left
    if map[index[0], index[1]-1] == depth:
      valid_indexes.append((index[0], index[1]-1))
  if index[0] + 1 < len(map): # down
    if map[index[0]+1, index[1]] == depth:
      valid_indexes.append((index[0]+1, index[1]))
  if index[1] + 1 < len(map[0]): # right
    if map[index[0], index[1]+1] == depth:
      valid_indexes.append((index[0], index[1]+1))
  return valid_indexes

def count_score(index):
  depth = 1
  next_step_indexes = [index]
  while depth <= 9:
    holder = []
    for next_step in next_step_indexes:
      holder += check_surrounding_indexes(next_step, depth)
    next_step_indexes = list(set(holder))
    depth += 1
  return len(next_step_indexes)

def count_rating(index):
  depth = 1
  next_step_indexes = [index]
  while depth <= 9:
    holder = []
    for next_step in next_step_indexes:
      holder += check_surrounding_indexes(next_step, depth)
    next_step_indexes = holder
    depth += 1
  return len(next_step_indexes)

score = 0
rating = 0
for i in range(len(indices[0])):
  score += count_score((int(indices[0][i]),int(indices[1][i])))
  rating += count_rating((int(indices[0][i]),int(indices[1][i])))

# part a
print(score)
# part b
print(rating)