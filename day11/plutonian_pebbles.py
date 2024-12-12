def build_known_stones():
  stones = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  blink = 0
  while blink < 13:
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
  return set(stones)

def handle_known_stones(known_stones):
  holder = dict.fromkeys(known_stones.keys(), 0)
  for stone in known_stones:
    if stone == 0:
      holder[1] += known_stones[stone]
    elif len(str(stone)) % 2 == 0:
      holder[int(str(stone)[:len(str(stone))//2])] += known_stones[stone]
      holder[int(str(stone)[len(str(stone))//2:])] += known_stones[stone]
    else:
      holder[stone * 2024] += known_stones[stone]
  return holder

def handle_unknown_stones(unknown_stones, known_stones):
  holder_unknown = []
  for stone in unknown_stones:
      if len(str(stone)) % 2 == 0:
        left = int(str(stone)[:len(str(stone))//2])
        right = int(str(stone)[len(str(stone))//2:])
        if left in known_stones.keys():
          known_stones[left] += 1
        else:
          holder_unknown.append(left)
        if right in known_stones.keys():
          known_stones[right] += 1
        else: 
          holder_unknown.append(right)
      else:
        holder_unknown.append(stone*2024)
  return holder_unknown, known_stones

def get_count(known, unknown):
  return sum(known.values()) + len(unknown)

unique_stones = build_known_stones()
known_stones = dict.fromkeys(unique_stones, 0)
known_stones[0] = 1
known_stones[1] = 1
unknown_stones = [int(stone) for stone in open('stones.txt').read().split(' ') if int(stone) > 1]
for i in range(75):
  known_stones = handle_known_stones(known_stones)
  unknown_stones, known_stones = handle_unknown_stones(unknown_stones, known_stones)

  # part a
  if i == 24:
    print(get_count(known_stones, unknown_stones))

# part b
print(get_count(known_stones, unknown_stones))