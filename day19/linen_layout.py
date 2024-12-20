import re
towels, target_designs = open('towels.txt').read().split('\n\n')

towels = sorted(towels.split(', '), key=len)
towels.reverse()
target_designs = target_designs.split('\n')

def check_next_towel(word, valid_strings):
  word_count = 0
  if word == '':
    return 1
  for towel in towels:
    match = re.match(towel, word)
    if match and word[match.end():] in valid_strings.keys():
      word_count += valid_strings[word[match.end():]]
    elif match and word not in fail_strings:
      word_count += check_next_towel(word[match.end():], valid_strings)
    elif match:
      fail_strings.add(word[match.end():])
    if match:
      valid_strings[word] = word_count
  return word_count

fail_strings = set() # is this... memoization?
valid_lines = 0
valid_counts = 0
for design in target_designs:
  valid = check_next_towel(design, {})
  valid_counts += valid
  valid_lines += int(valid != 0)

print(valid_lines)
print(valid_counts)