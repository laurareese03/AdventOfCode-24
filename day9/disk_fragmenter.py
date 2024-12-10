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

blocks = []
# reset blocks
for i in range(len(components)):
  if i % 2 == 0:
    blocks.append([i//2]*int(components[i]))
  else:
    blocks.append(['.']*int(components[i]))

# using a while loop here bc inserting files and empty space messes with indexing
i = len(blocks)-1
while i > 0:
  for j in range(i):
    if blocks[i] and blocks[j].count('.') >= len(blocks[i]) and blocks[i].count('.') == 0:
      new_space = ['.']*(len(blocks[j])-len(blocks[i]))
      # move files to new location and replace former location with empty space
      blocks[j] = blocks[i]
      blocks[i] = ['.']*len(blocks[i])
      # if there's still space left at the current location, add it to the block info, and readjust indexing
      if new_space != []:
        blocks.insert(j+1, new_space)
        i +=1
      break
  i -= 1

checksum = 0
list_1d = []
# convert nested lists into 1d list
for i in range(len(blocks)):
  list_1d += blocks[i]

for i in range(len(list_1d)):
  if list_1d[i] != '.':
    checksum += int(list_1d[i]) * i
print(checksum)
