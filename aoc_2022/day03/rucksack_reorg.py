'''
Day 3: Rucksack Reorganization

Austin Equitz
austin.equitz@gmail.com
'''

import string

LETTER_VALS = [x for x in string.ascii_letters]

with open('rucksacks.txt', 'r') as fin: rucksacks = fin.read().splitlines()

# Part One
total_score = 0
for cmpts in rucksacks:
    mid_point = len(cmpts) // 2
    first_cmpt = {x for x in cmpts[:mid_point]}
    second_cmpt = {x for x in cmpts[mid_point:]}

    similar_letters = first_cmpt.intersection(second_cmpt)

    total_score += sum([LETTER_VALS.index(x) + 1 for x in similar_letters])

print(f'The sum of the priorities is: {total_score}')

# Part Two
total_score = 0
for groups in list(zip(*(iter(rucksacks),) * 3)):
    badge = set(groups[0]).intersection(groups[1], groups[2])

    total_score += sum([LETTER_VALS.index(x) + 1 for x in badge])

print(f'The sum of the priorites based on badges is: {total_score}')

