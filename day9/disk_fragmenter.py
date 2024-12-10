disk_map = open('disk_map.txt').read()

components = list(disk_map)
blocks = []

for i in range(len(components)):
  if i % 2 == 0:
    blocks += [i//2]*int(components[i])
  else:
    blocks += ['.']*int(components[i])

# find all index of variable from
# https://stackoverflow.com/questions/6294179/how-to-find-all-occurrences-of-an-element-in-a-list
indices = [i for i, x in enumerate(blocks) if x == '.']
for index in indices:
  if index > len(blocks):
    break
  next_int = blocks.pop(-1)
  while next_int == '.':
    next_int = blocks.pop(-1)
  try:
    blocks[index] = next_int
  except:
    blocks.append(next_int) # in case we accidentally pop too far and remove the last index

checksum = 0
for i in range(len(blocks)):
  checksum += i * blocks[i]

print(checksum)