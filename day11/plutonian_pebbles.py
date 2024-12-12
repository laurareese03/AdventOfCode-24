stones = [int(stone) for stone in open('build_stones.txt').read().split(' ')]

math_count = 0

blink = 0
while blink < 25:
  next_stones = []
  for i in range(len(stones)):
    if stones[i] == 0:
      next_stones.append(1)
    elif len(str(stones[i])) % 2 == 0:
      next_stones.append(int(str(stones[i])[:len(str(stones[i]))//2]))
      next_stones.append(int(str(stones[i])[len(str(stones[i]))//2:]))
    else:
      next_stones.append(stones[i] * 2024)
  stones = next_stones
  blink += 1
  if blink == 25:
    print(len(stones))

def handle_known_stones(stone_types):
  holder = dict.fromkeys(stone_types.keys(), 0)
  for stone in stone_types:
    if stone == 0:
      holder[1] += stone_types[stone]
    elif len(str(stone)) % 2 == 0:
      holder[int(str(stone)[:len(str(stone))//2])] += stone_types[stone]
      holder[int(str(stone)[len(str(stone))//2:])] += stone_types[stone]
    else:
      holder[stone * 2024] += stone_types[stone]
  return holder

def handle_unknown_stones(unknown_stones, stone_types):
  holder_unknown = []
  for stone in unknown_stones:
      if len(str(stone)) % 2 == 0:
        left = int(str(stone)[:len(str(stone))//2])
        right = int(str(stone)[len(str(stone))//2:])
        if left in stone_types.keys():
          stone_types[left] += 1
        else:
          holder_unknown.append(left)
        if right in stone_types.keys():
          stone_types[right] += 1
        else: 
          holder_unknown.append(right)
      else:
        holder_unknown.append(stone*2024)
  return holder_unknown, stone_types

unique_stones = set(stones)
stone_types = dict.fromkeys(unique_stones, 0)
stone_types[0] = 1
stone_types[1] = 1
unknown_stones = [int(stone) for stone in open('stones.txt').read().split(' ') if int(stone) > 1]
print(unknown_stones)
# unknown_stones = unknown_stones.remove(1)
# unknown_stones = unknown_stones.remove(0)
for i in range(75):
  print(i)
  stone_types = handle_known_stones(stone_types)
  unknown_stones, stone_types = handle_unknown_stones(unknown_stones, stone_types)

count = 0
for stone in stone_types:
  count += stone_types[stone]
count += len(unknown_stones)
print(count)