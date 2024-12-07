import numpy as np

equations = open('calibration_equations.txt').read().split('\n')

def check_operations(answer, input, ops):
  num = ops**(len(input)-1)-1
  while num >= 0:
    operations = str(np.base_repr(num, base=ops)).zfill(len(input)-1)
    num -= 1
    product = input[0]
    for i in range(len(operations)):
      if operations[i] == '0':
        product += input[i+1]
      elif operations[i] == '1':
        product *= input[i+1]
      else:
        product = int(str(product) + str(input[i+1]))
    if product == answer:
      return True
  return False

count = 0
part_b_equations = []
for equation in equations:
  answer = int(equation.split(':')[0])
  input = [int(x) for x in equation.split(' ')[1:]]
  if check_operations(answer, input, 2):
    count += answer
  else:
    part_b_equations.append((answer,input))
print(count)

for answer, input in part_b_equations:
  if check_operations(answer, input, 3):
    count += answer
print(count)