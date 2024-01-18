from itertools import cycle
import re

from math import lcm

with open('node_network.txt', 'r') as f:
    data = f.read().splitlines()

code = data.pop(0)
data = data[1:]
code = code.replace('L', '0').replace('R', '1')

data = [x.replace('=', ',') for x in data]
data = [re.sub('\s|\(|\)', '', x) for x in data]

print(f'Code: {code}')
print(f'Data: {data}')
data_dict = {}
for x in data:
    key, left, right = x.split(',')
    data_dict[key] = (left, right)

first_key = 'AAA'
last_key = 'ZZZ'

# key = first_key
# number_of_searches = 0
# for c in cycle(code):
#     number_of_searches += 1
#     key = data_dict[key][int(c)]

#     if key == last_key:
#         print(f'Found last key: {key}')
#         break


# print(f'Number of searches: {number_of_searches}')


starting_nodes = [x for x in data_dict.keys() if x[2] == 'A']


print(starting_nodes)
print(code)
all_total_searches = []

for node in starting_nodes:
    number_of_searches = 0
    current_node = node

    for c in cycle(code):
        number_of_searches += 1
        print(f'Number of searches: {number_of_searches}', end='\r')

        next_node = data_dict[current_node][int(c)]

        z_node_found = next_node[2] == 'Z'

        if z_node_found:
            print(f'Found Z node {next_node} for {current_node} in {number_of_searches} searches')
            all_total_searches.append(number_of_searches)
            break

        current_node = next_node

print(f'Number of searches for each node: {all_total_searches}')

print(f'LCM of all node searches: {lcm(*all_total_searches)}')
