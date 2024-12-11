stones = [int(stone) for stone in open('stones.txt').read().split(' ')]

blink = 0
while blink < 75:
  next_stones = []
  print(blink)
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
print(len(stones))