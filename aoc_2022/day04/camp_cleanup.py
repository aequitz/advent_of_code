'''
Day 4: Camp Cleanup

Austin Equitz
austin.equitz@gmail.com
'''

with open('assignments.txt', 'r') as fin: assignments = fin.read().splitlines()

# Part One
contained_sum = 0
for pairs in assignments:
    asmts = [list(map(int, x.split('-'))) for x in pairs.split(',')]
    first_range, second_range = [set(range(x[0], x[1] + 1)) for x  in asmts]

    is_subset = first_range.issubset(second_range) or second_range.issubset(first_range)

    if is_subset: contained_sum += 1

print(f'Pairs that have a subset: {contained_sum}')

# Part Two
contained_sum = 0
for pairs in assignments:
    asmts = [list(map(int, x.split('-'))) for x in pairs.split(',')]
    first_range, second_range = [set(range(x[0], x[1] + 1)) for x  in asmts]

    intersects = first_range.intersection(second_range)

    if intersects: contained_sum += 1

print(f'Pairs that have an intersection: {contained_sum}')
    
    