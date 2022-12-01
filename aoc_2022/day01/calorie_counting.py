'''
Day 1: Calorie Counting

Austin Equitz
austin.equitz@gmail.com
'''
import os

script_dir = os.path.dirname(__file__)
puzzle_input = os.path.join(script_dir, 'elves_and_calories.txt')

with open(puzzle_input, 'r') as fin: elf_cals = fin.read().split('\n\n')

# Part One - Find elf with most calories and report calories
each_elf_cals = [[eval(cal) for cal in elf.split()] for elf in elf_cals]
summed_elf_cals = [sum(cals) for cals in each_elf_cals]

max_cals = max(summed_elf_cals)
print(f'Most calories carried by elf: {max_cals}')

# Part Two - Find top 3 elves with most calories and report calories
sorted_sums = sorted(summed_elf_cals, reverse=True)
top_three_cals = sum(sorted_sums[0:3])
print(f'Sum of calories for top three elves: {top_three_cals}')
