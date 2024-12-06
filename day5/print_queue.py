lines = open('page_ordering.txt').read().split('\n\n')
page_orders = lines[0].split('\n')
pages = lines[1].split('\n')

# orderings dict tracts all pages that should be smaller than the current page
orderings = {'13': []}
for order in page_orders:
  comp = order.split('|')
  try:
    orderings[comp[0]].append(comp[1])
  except:
    orderings[comp[0]] = [comp[1]]

part_b_pages = []
# brute forcing because the orders in a cycle! wtf!
page_total = 0
complete = True
for page in pages:
  complete = True
  page = page.split(',')
  for i in range(len(page)):
    if len(set(page[:i]).intersection(set(orderings[page[i]]))) != 0:
      complete = False
      part_b_pages.append(page)
      break
  if complete: page_total += int(page[(len(page)-1)//2])
# part a
print(page_total)

sorted_page_total = 0
for page in part_b_pages:
  page_orderings = {}
  for p in page:
    page_orderings[p] = set(page).intersection(set(orderings[p]))
    
  # lifted almost exactly from my initial attempt at part a lol
  # sometimes being goofy pays off!
  exact_order = []
  for i in range(len(page_orderings)):
    for order in page_orderings:
      if len(page_orderings[order])  == len(exact_order) + 1:
        exact_order.append(order)
  for order in page_orderings:
    if len(page_orderings[order]) == 1 and page_orderings[order] not in exact_order:
        exact_order.insert(0, str(list(page_orderings[order])[0]))
  sorted_page_total += int(exact_order[(len(exact_order)-1)//2])

# part b
print(sorted_page_total)