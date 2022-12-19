'''
Day 10: Cathode-Ray Tube

Austin Equitz
austin.equitz@gmail.com
'''

import numpy as np

CRT_ROW_SIZE = 40

with open('program_instructions.txt', 'r') as fin: prog_instr = fin.read().splitlines()

signal_str_idx = 20
reg_x = 1
next_reg_add = 0
signal_str_sum = 0
cycles_complete = 0
crt_screen = []
sprite_positions = list(range(reg_x - 1, reg_x + 2))

for crt_position,instr in enumerate(prog_instr):
    # Determine
    if instr == 'noop':
        curr_reg_add = 0
        cycle_len = 1

    elif instr.startswith('addx'):
        curr_reg_add = int(instr.split()[1])
        cycle_len = 2

    # Part One - Determine signals strengths
    if cycles_complete >= signal_str_idx:
        signal_str = signal_str_idx * reg_x
        signal_str_sum += signal_str

        signal_str_idx += 40

    # Calculate X register, next value to add to register, and cycles complete
    reg_x += next_reg_add
    next_reg_add = curr_reg_add
    cycles_complete += cycle_len

    # Part Two - Draw the CRT screen
    curr_crt_row = (cycles_complete - 1) // CRT_ROW_SIZE

    sprite_pos_start = (reg_x - 1) + (curr_crt_row * CRT_ROW_SIZE)
    sprite_pos_end = (reg_x +2) + (curr_crt_row * CRT_ROW_SIZE)
    sprite_positions = list(range(sprite_pos_start, sprite_pos_end))

    for cycle in range(cycles_complete - cycle_len, cycles_complete):
        crt_screen.append('#' if cycle in sprite_positions else '.')

# Part One Output
print(f'The sum of all signal strength calculations: {signal_str_sum}')

# Part Two Output
print('Generated Cathode-Ray Tube screen:')

crt_screen = np.array(crt_screen).reshape(6, 40)
for row in crt_screen:
    print(''.join(row))
