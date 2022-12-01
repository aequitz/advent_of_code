'''
Navigates the ship based off of the navigation steps provided

Austin Equitz
austin.equitz@gmail.com
'''

import os

rel_path = 'input2.txt'
file_path = os.path.join(os.path.dirname(__file__), rel_path)

# Reads in text file as list[str]
with open(file_path, 'r') as fin: nav_steps = [n.strip() for n in fin.readlines()]

# Split each list into two separate lists
directions,nums = zip(*(s.split(' ') for s in nav_steps))
nums = list(map(int, nums))

# Obtain the horizontal position and depth based on navigation steps provided
horz_pos = 0
depth = 0
aim = 0
for i in range(len(directions)):
    if directions[i] == 'forward':
        horz_pos += nums[i]
        depth += nums[i] * aim

    if directions[i] == 'up': aim -= nums[i]
    if directions[i] == 'down': aim += nums[i]

mult_ans = horz_pos * depth

print(horz_pos)
print(depth)
print(mult_ans)