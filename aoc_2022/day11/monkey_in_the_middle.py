'''
Day 11: Monkey in the Middle

Austin Equitz
austin.equitz@gmail.com
'''

import math

STARTING_ITEMS_STR = 'Starting items: '
MATH_OP_STR = 'Operation: new = '
DIVISIBLE_STR = 'Test: divisible by '
NEXT_MONKEY_STR = 'monkey '
DIVIDE_CONST = 3
NUM_ROUNDS = 20

with open('monkey_notes.txt', 'r') as fin: monkey_input = fin.read().split('\n\n')

monkey_notes = [line.split('\n') for line in monkey_input]
monkey_notes = [[line.strip() for line in monkey] for monkey in monkey_notes]

monkeys = []
for monkey in monkey_notes:
    monkey_dict = {}

    # Get monkey number
    monkey_dict['monkey_num'] = monkey[0][:-1]

    # Get initial items held by monkey
    items = monkey[1].replace(STARTING_ITEMS_STR, '').strip()
    monkey_dict['items'] = list(map(int, items.split(',')))
    monkey_dict['items_inspected'] = 0

    # Get math operation
    math_op = monkey[2].replace(MATH_OP_STR, '')
    monkey_dict['math_op'] = eval(f'lambda old: {math_op}')

    # Get divisible item number
    monkey_dict['div_num'] = int(monkey[3].replace(DIVISIBLE_STR, ''))

    # Get next monkeys based on true/false
    monkey_dict['true_monkey'] = int(monkey[4].split(NEXT_MONKEY_STR)[-1])
    monkey_dict['false_monkey'] = int(monkey[5].split(NEXT_MONKEY_STR)[-1])

    monkeys.append(monkey_dict)

for round in range(NUM_ROUNDS):
    # print(round)
    for monkey in monkeys:
        math_op = monkey['math_op']
        true_monkey = monkey['true_monkey']
        false_monkey = monkey['false_monkey']
        div_num = monkey['div_num']

        for item in monkey['items']:
            monkey['items_inspected'] += 1
            worry_level = math.floor(math_op(item) / DIVIDE_CONST)

            if worry_level % div_num == 0:
                monkeys[true_monkey]['items'].append(worry_level)

            else:
                monkeys[false_monkey]['items'].append(worry_level)

        monkey['items'] = []


items_inspected = [monkey['items_inspected'] for monkey in monkeys]
items_inspected.sort(reverse=True)
monkey_business = items_inspected[0] * items_inspected[1]

print(f'Monkey business after {NUM_ROUNDS} rounds: {monkey_business}')
