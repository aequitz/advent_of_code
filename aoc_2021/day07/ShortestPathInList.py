'''
Find the number that provides the shortest
path for all numbers in a list. Find the
total path traveled by all numbers.

Austin Equitz
austin.equitz@gmail.com
'''

with open('SubmarineLocations.txt', 'r') as fin: loc_in = [int(n) for n in fin.read().split(',')]

'''
# Less Efficient: Tests all possible solutions
loc_in_range = range(min(loc_in), max(loc_in) + 1)
all_dist = [0] * len(loc_in_range)

for idx,num in enumerate(loc_in_range):
    for loc in loc_in:
        all_dist[idx] += sum(range(1, abs(loc - num) + 1))
print(min(all_dist))
'''

# More Efficient: Only tests average (+/- 1)
mean_loc = round(sum(loc_in) / len(loc_in))
mean_loc_range = range(mean_loc - 1, mean_loc + 2)
all_dist = [0] * len(mean_loc_range)

for idx,num in enumerate(mean_loc_range):
    for loc in loc_in:
        all_dist[idx] += sum(range(1, abs(loc - num) + 1))

# Print Results
print(min(all_dist))
print(all_dist)