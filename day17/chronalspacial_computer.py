import re
registers, operations = open('program_info.txt').read().split('\n\n')

operations = [int(i) for i in operations[9:].split(',')]
registers = registers.split('\n')
register = {}
for r in registers:
  m = re.match(r'Register ([A-Za-z]+): (\d+)', r)
  register[m.group(1)] = int(m.group(2))

def get_combo(literal):
  match literal:
    case 4:
      return register['A']
    case 5:
      return register['B']
    case 6: 
      return register['C']
    case 7:
      print('Err - 7 is reserved')
    case _:
      return literal

i = 0
output = ''
while i < len(operations):
  match operations[i]:
    case 0:
      register['A'] = register['A'] // 2**get_combo(operations[i+1])
    case 1:
      register['B'] = register['B'] ^ operations[i+1]
    case 2:
      register['B'] = get_combo(operations[i+1]) % 8
    case 3:
      if register['A'] != 0:
        i = operations[i+1] - 2
    case 4:
      register['B'] = register['B'] ^ register['C']
    case 5:
      output += str(get_combo(operations[i+1]) % 8)
    case 6:
      register['B'] = register['A'] // 2**get_combo(operations[i+1])
    case 7:
      register['C'] = register['A'] // 2**get_combo(operations[i+1])
  i += 2
print(','.join(list(output)))