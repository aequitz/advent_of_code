'''
Finds the number of times that a number is greater
than the last number entry in a text file

Austin Equitz
austin.equitz@gmail.com
'''

import os
import numpy as np

rel_path = 'NumberList.txt'

# Reads in text file as list[int]
with open(os.path.join(os.path.dirname(__file__), rel_path), 'r') as fin: nums = [int(n.strip()) for n in fin.readlines()]

# Find rolling sum of 3 elements (part 2 of challenge - comment for part 1)
nums = np.convolve(nums,np.ones(3,dtype=int),'valid')

# Find the number of instances where the next index is greater than the previous index
count = sum(b>a for a,b in zip(nums,nums[1:]))

#Print count
print(count)