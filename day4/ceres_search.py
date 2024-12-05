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

xmas_count = 0
vertical_count = 0
horizontal_count = 0
left_up_diag_count = 0
right_up_diag_count = 0
# nested for loops whoooooo
for i in range(np.shape(wordsearch)[0]):
  for j in range(len(wordsearch[0])):
    if wordsearch[i][j] == 'X' or wordsearch[i][j] == 'S':
      if check_up_diag(i,j):
        right_up_diag_count += 1
      if check_forward(i,j):
        horizontal_count += 1
      if check_down_diag(i,j):
        left_up_diag_count += 1
      if check_down(i,j):
        vertical_count += 1

print(horizontal_count+vertical_count+left_up_diag_count+right_up_diag_count)