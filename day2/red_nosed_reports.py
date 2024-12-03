lines = open('reports.txt').readlines()

def check_no_change(change_levels):
  return 0 in change_levels

def check_direction_change(change_levels):
  directions = [level > 0 for level in change_levels]
  return len(set(directions)) > 1

def check_large_gaps(change_levels):
  return len({level for level in change_levels if level > 3 or level < -3}) > 0

count_a = 0
for line in lines:
  report = list(map(int,line.strip().split(' ')))
  change_levels = set([report[i]-report[i+1] for i in range(len(report)-1)])
  if 0 in change_levels:
    continue
  if len(set([level > 0 for level in change_levels])) > 1:
    continue
  if len({level for level in change_levels if level > 3 or level < -3}) > 0:
    continue
  count_a +=1
print(count_a)

# I'm sure there's a way to shorten this so we don't iter over all change levels for failing levels
# but that seemed like a great way to waste a lotta time and introduce a lotta bugs so. no.
count_b = 0
for line in lines:
  report = list(map(int,line.strip().split(' ')))
  change_levels = [report[i]-report[i+1] for i in range(len(report)-1)]
  if  not (check_no_change(set(change_levels)) or check_direction_change(set(change_levels)) or check_large_gaps(set(change_levels))):
    count_b += 1
  else:
    for i in range(len(report)):
      test_report = report.copy()
      del test_report[i]
      test_change_levels = [test_report[i]-test_report[i+1] for i in range(len(test_report)-1)]
      if not (check_no_change(set(test_change_levels)) or check_direction_change(set(test_change_levels)) or check_large_gaps(set(test_change_levels))):
        count_b += 1
        break
print(count_b)