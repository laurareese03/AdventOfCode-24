import numpy as np

lines = open('lab_layout.txt').read().split('\n')

lab = []
for line in lines:
  lab.append(list(line))

lab = np.array(lab)
index = np.where(lab == '^')
index = (index[0][0], index[1][0])
while True:
  path = lab[:,index[1]]
  future = path[-(len(path)-index[0]+1)::-1]
  ha = ''.join(str(x) for x in future)
  new_index = ha.find('#')
  if new_index == -1:
    lab[index[0]::-1, index[1]] = 'X'
    break
  lab[index[0]:index[0]-new_index-1:-1, index[1]] = 'X'
  index = (len(lab)-(index[1]+1), index[0]-new_index)
  lab = np.rot90(lab)

print((lab == 'X').sum())