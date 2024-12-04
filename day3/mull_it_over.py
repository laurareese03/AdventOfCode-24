import re

memory = open('memory.txt').read().replace('\n', '')

mults = re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)', memory)

total = 0
for mult in mults:
  vals = mult[4:-1].split(',')
  total += int(vals[0]) * int(vals[1])
print(total)

total = 0
# use find indexes for do's + don'ts, AND for mults, find valid ranges then calc the mults in those ranges
on_intervals = re.findall(r'((^|do\(\)).*?(don\'t\(\)|$))', memory)
for interval in on_intervals:
  mults = re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)', interval[0])
  for mult in mults:
    vals = mult[4:-1].split(',')
    total += int(vals[0]) * int(vals[1])
print(total)