import re
towels, target_designs = open('towels.txt').read().split('\n\n')

towels = sorted(towels.split(', '), key=len)
towels.reverse()
target_designs = target_designs.split('\n')

fail_strings = set() # is this... memoization?

def check_next_towel(word):
  if word == '':
    return True
  for towel in towels:
    match = re.match(towel, word)
    if match and word not in fail_strings and check_next_towel(word[match.end():]):
      return True
    elif match:
      fail_strings.add(word[match.end():])
  return False

count = 0
for design in target_designs:
  if check_next_towel(design):
    count += 1
print(count)
