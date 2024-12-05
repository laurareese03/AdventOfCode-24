import numpy as np

wordsearch = open('word_search.txt').read().split('\n')

def check_up_diag(i,j):
  if i - 3 < 0 or j + 4 > len(wordsearch[0]):
    return False
  word = wordsearch[i][j] + wordsearch[i-1][j+1] + wordsearch[i-2][j+2] + wordsearch[i-3][j+3]
  if word == 'XMAS' or word == 'SAMX':
    return True
  return False

def check_forward(i,j):
  if j + 4 > len(wordsearch[0]):
    return False
  word = wordsearch[i][j] + wordsearch[i][j+1] + wordsearch[i][j+2] + wordsearch[i][j+3]
  if word == 'XMAS' or word == 'SAMX':
    return True
  return False

def check_down_diag(i,j):
  if i + 4 > np.shape(wordsearch)[0] or j + 4 > len(wordsearch[0]):
    return False
  word = wordsearch[i][j] + wordsearch[i+1][j+1] + wordsearch[i+2][j+2] + wordsearch[i+3][j+3]
  if word == 'XMAS' or word == 'SAMX':
    return True
  return False

def check_down(i,j):
  if i + 4 > np.shape(wordsearch)[0]:
    return False
  word = wordsearch[i][j] + wordsearch[i+1][j] + wordsearch[i+2][j] + wordsearch[i+3][j]
  if word == 'XMAS' or word == 'SAMX':
    return True
  return False

def check_x_mas(i,j):
  if i == 0 or i >= np.shape(wordsearch)[0] -1 or j == 0 or j >= len(wordsearch[0]) -1:
    return False
  word_one = wordsearch[i-1][j-1] + wordsearch[i+1][j+1]
  word_two = wordsearch[i+1][j-1] + wordsearch[i-1][j+1]
  if (word_one == 'MS' or word_one == 'SM') and (word_two == 'MS' or word_two == 'SM'):
    return True
  return False

xmas_count = 0
# nested for loops whoooooo
for i in range(np.shape(wordsearch)[0]):
  for j in range(len(wordsearch[0])):
    if wordsearch[i][j] == 'X' or wordsearch[i][j] == 'S':
      if check_up_diag(i,j):
        xmas_count += 1
      if check_forward(i,j):
        xmas_count += 1
      if check_down_diag(i,j):
        xmas_count += 1
      if check_down(i,j):
        xmas_count += 1
print(xmas_count)

# x-mas search :|
x_mas_count = 0
for i in range(np.shape(wordsearch)[0]):
  for j in range(len(wordsearch[0])):
    if wordsearch[i][j] == 'A' and check_x_mas(i,j):
        x_mas_count += 1
print(x_mas_count)