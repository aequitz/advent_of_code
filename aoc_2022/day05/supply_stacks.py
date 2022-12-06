'''
Day 4: Camp Cleanup

Austin Equitz
austin.equitz@gmail.com
'''

import itertools
import re

with open('rearrangement_info.txt', 'r') as fin: rearrangement_info = fin.read()

initial_stack, procedures = rearrangement_info.split('\n\n')
print(initial_stack)

original_stacks = []
for line in initial_stack.splitlines():
    split_idxs = list(range(0, len(line) + 2, 4))
    parts = [line[split_idxs[i]:split_idxs[i+1]] for i in range(len(split_idxs) - 1)]
    parts = [x.strip() for x in parts]

    original_stacks.append(parts)
    print(parts)

# Remove column numbers
original_stacks.pop(-1)

# Part One
# Transpose the stacks for easier manipulation and remove blank elements
transposed_stacks = list(map(list, itertools.zip_longest(*original_stacks, fillvalue='')))
transposed_stacks = [[elmt for elmt in stack if elmt] for stack in transposed_stacks]

for procedure in procedures.splitlines():
    details = re.findall(r'(move|from|to) ([0-9]+)', procedure)
    move_qty, start, end = [int(x[1]) for x in details]

    start -= 1
    end -= 1

    # Get moving crates in reverse order and move them in stack
    moving_crates = transposed_stacks[start][0:move_qty][::-1]
    del transposed_stacks[start][0:move_qty]
    transposed_stacks[end][0:0] = moving_crates

final_string = ''.join([re.sub(r'[^A-Z]+', '', x[0]) for x in transposed_stacks])
print(f'The top crates for the singe-crate crane: {final_string}')

# Part Two
# Transpose the stacks for easier manipulation and remove blank elements
transposed_stacks = list(map(list, itertools.zip_longest(*original_stacks, fillvalue='')))
transposed_stacks = [[elmt for elmt in stack if elmt] for stack in transposed_stacks]

for procedure in procedures.splitlines():
    details = re.findall(r'(move|from|to) ([0-9]+)', procedure)
    move_qty, start, end = [int(x[1]) for x in details]

    start -= 1
    end -= 1

    # Get moving crates and move them in stack
    moving_crates = transposed_stacks[start][0:move_qty]
    del transposed_stacks[start][0:move_qty]
    transposed_stacks[end][0:0] = moving_crates

final_string = ''.join([re.sub(r'[^A-Z]+', '', x[0]) for x in transposed_stacks])
print(f'The top crates for the multi-crate crane: {final_string}')

