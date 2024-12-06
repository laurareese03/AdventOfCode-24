lines = open('page_ordering.txt').read().split('\n\n')
page_orders = lines[0].split('\n')
pages = lines[1].split('\n')

orderings = {}

for order in page_orders:
  comp = order.split('|')
  try:
    orderings[comp[1]].append(comp[0])
  except:
    orderings[comp[1]] = [comp[0]]

# assumes one exact order of page combos -> real input looks a lil scarier like we might need 2+ cycles
exact_order = []
for i in range(len(orderings)):
  for order in orderings:
    if len(orderings[order])  == len(exact_order) + 1:
      exact_order.append(order)
for order in orderings:
  if len(orderings[order]) == 1 and orderings[order][0] not in exact_order:
      exact_order.insert(0, orderings[order][0])

# we can probably assuming no pages are repeating! I'm dumb!
page_total = 0
for page in pages:
  page = page.split(',')
  intersection = [x for x in exact_order if x in page]
  if page == intersection:
    page_total += int(page[len(page)//2])
print(page_total)