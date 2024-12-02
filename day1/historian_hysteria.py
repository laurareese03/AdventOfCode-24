lines = open('locations.txt').readlines()

locations_a = []
locations_b = []
total_distance = 0

for line in lines:
  line = line.strip().split('   ')
  locations_a.append(int(line[0]))
  locations_b.append(int(line[-1]))

locations_a.sort()
locations_b.sort()

for i in range(len(locations_a)):
  total_distance += abs(locations_a[i] - locations_b[i])

# part a
print(total_distance)

similarity_score = 0
for location in locations_a:
  similarity_score += location * locations_b.count(location)

# part b
print(similarity_score)