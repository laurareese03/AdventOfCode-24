lines = open('page_ordering.txt').read().split('\n\n')
page_orders = lines[0].split('\n')
pages = lines[1].split('\n')

# orderings dict tracts all pages that should be larger than the current page
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
for page in pages:
  complete = True
  page = page.split(',')
  for i in range(len(page)):
    # for every index of the page list, 
    # check all previous pages against the current page's afters
    # if set is nonzero, we're out of order
    if len(set(page[:i]).intersection(set(orderings[page[i]]))) != 0:
      complete = False
      part_b_pages.append(page)
      break
  if complete: page_total += int(page[(len(page)-1)//2])
# part a
print(page_total)

sorted_page_total = 0
for page in part_b_pages:
  exact_order = [None]*len(page)
  for p in page:
    # total the number of pages greater than each page and add that page to the sorted array at that index
    index = len(set(page).intersection(set(orderings[p])))
    exact_order[index] = p
  sorted_page_total += int(exact_order[(len(exact_order)-1)//2])
# part b
print(sorted_page_total)