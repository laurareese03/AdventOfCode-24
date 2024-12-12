# not actually sure if its quicker to limit known stones to just the core 54 values
# but its certainly easier to understand and debug so. it stays.
# (its probably quicker)
def build_known_stones():
  stones = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  common_stones = set()
  for stone in stones:
    if len(str(stone)) % 2 == 0:
      left, right = int(str(stone)[:len(str(stone))//2]), int(str(stone)[len(str(stone))//2:])
      if left not in common_stones:
        stones.append(left)
        common_stones.add(left)
      if right not in common_stones:
        stones.append(right)
        common_stones.add(right)
    else:
      if stone * 2024 not in common_stones:
        stones.append(stone * 2024)
        common_stones.add(stone * 2024)
  return dict.fromkeys(common_stones, 0)

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
    # we don't have to worry about the 0 bc it should already be in known_stones
    if len(str(stone)) % 2 == 0:
      s = str(stone)
      left, right = int(s[:len(s)//2]), int(str(stone)[len(s)//2:])
      if left in known_stones.keys():
        known_stones[left] += 1
      else:
        holder_unknown.append(left)
      if right in known_stones.keys():
        known_stones[right] += 1
      else: 
        holder_unknown.append(right)
    else:
      # we don't have to check presense in known_stones bc they would already be moved
      holder_unknown.append(stone*2024)
  return holder_unknown, known_stones

def get_count(known, unknown):
  return sum(known.values()) + len(unknown)

# build our dictionary of common rocks and list of unusual ones to get started
known_stones = build_known_stones()
unknown_stones = [int(stone) for stone in open('stones.txt').read().split(' ')]
for stone in unknown_stones:
  if stone in known_stones.keys():
    known_stones[stone] += 1
    unknown_stones.remove(stone)

# don't blink, don't even blink, blink and you're dead
for blink in range(75):
  known_stones = handle_known_stones(known_stones)
  unknown_stones, known_stones = handle_unknown_stones(unknown_stones, known_stones)
  # part a
  if blink == 24:
    print(get_count(known_stones, unknown_stones))
# part b
print(get_count(known_stones, unknown_stones))