lines = open('page_ordering.txt').read().split('\n\n')
page_orders = lines[0].split('\n')
pages = lines[1].split('\n')

# orderings dict tracts all pages that should be smaller than the current page
orderings = {}
for order in page_orders:
  comp = order.split('|')
  try:
    orderings[comp[0]].append(comp[1])
  except:
    orderings[comp[0]] = [comp[1]]

# brute forcing because the orders in a cycle! wtf!
page_total = 0
complete = True
for page in pages:
  complete = True
  page = page.split(',')
  for i in range(len(page)):
    if len(set(page[:i]).intersection(set(orderings[page[i]]))) != 0:
      complete = False
      break
  if complete: page_total += int(page[(len(page)-1)//2])
print(page_total)