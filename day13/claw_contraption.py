import re, numpy as np

nums = re.findall(r'\d+', open('button_behavior.txt').read())
games = [nums[i:i+6] for i in range(0,len(nums),6)] # arrays of 6 in format [x1 y1 x2 y2 x= y=]

prize_a = 0
prize_b = 0
for game in games:
  coeff_arr = np.linalg.inv(np.array([[game[0], game[2]], [game[1], game[3]]], dtype=int)) # [[x1 x2], [y1 y2]]

  answ_arr = np.reshape(np.array([game[4:]], dtype=int), (2,1))
  var_arr = np.round(np.matmul(coeff_arr, answ_arr), 4)
  if var_arr[0][0].is_integer() and var_arr[1][0].is_integer():
    prize_a += 3*int(var_arr[0][0]) + int(var_arr[1][0])

  long_answ_arr = np.add(answ_arr, [10000000000000])
  long_var_arr = np.round(np.matmul(coeff_arr, long_answ_arr), 2) # floating point errors i hate you
  if long_var_arr[0][0].is_integer() and long_var_arr[1][0].is_integer():
    prize_b += 3*int(long_var_arr[0][0]) + int(long_var_arr[1][0])

print(prize_a)
print(prize_b)