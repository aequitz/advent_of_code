'''
Day 2: Rock Paper Scissors

Austin Equitz
austin.equitz@gmail.com
'''

import re

MY_HAND_VALS = {
    'ROCK': 1,
    'PAPER': 2,
    'SCISSORS': 3
}
SCORES = {
    'WIN': 6,
    'LOSE': 0,
    'TIE': 3
}

with open('rps_matches.txt', 'r') as fin: rps_matches = fin.read().splitlines()

# Part One
total_score = 0
for match in rps_matches:
    match = re.sub('A |X', 'ROCK ', match)
    match = re.sub('B |Y', 'PAPER ', match)
    match = re.sub('C |Z', 'SCISSORS ', match)

    opp_hand, my_hand = match.split()
    hand_val = MY_HAND_VALS[my_hand]

    if my_hand == opp_hand: hand_result = 'TIE'

    elif my_hand == 'ROCK':
        if opp_hand == 'PAPER': hand_result = 'LOSE'
        elif opp_hand == 'SCISSORS': hand_result = 'WIN'

    elif my_hand == 'PAPER':
        if opp_hand == 'ROCK': hand_result = 'WIN'
        elif opp_hand == 'SCISSORS': hand_result = 'LOSE'

    elif my_hand == 'SCISSORS':
        if opp_hand == 'ROCK': hand_result = 'LOSE'
        elif opp_hand == 'PAPER': hand_result = 'WIN'

    score_val = SCORES[hand_result]
    total_score += hand_val + score_val

print(f'The total score is: {total_score}')

# Part Two
SCORE_LOOKUP = {
    'X': 0,
    'Y': 3,
    'Z': 6
}

total_score = 0
for match in rps_matches:
    match = re.sub('A ', 'ROCK ', match)
    match = re.sub('B ', 'PAPER ', match)
    match = re.sub('C ', 'SCISSORS ', match)

    opp_hand, hand_result = match.split()
    score_val = SCORE_LOOKUP[hand_result]

    # Force tie
    if hand_result == 'Y': my_hand = opp_hand

    # Force lose
    elif hand_result == 'X':
        if opp_hand == 'ROCK': my_hand = 'SCISSORS'
        elif opp_hand == 'PAPER': my_hand = 'ROCK'
        elif opp_hand == 'SCISSORS': my_hand = 'PAPER'

    # Force win
    elif hand_result == 'Z':
        if opp_hand == 'ROCK': my_hand = 'PAPER'
        elif opp_hand == 'PAPER': my_hand = 'SCISSORS'
        elif opp_hand == 'SCISSORS': my_hand = 'ROCK'

    else:
        print('Bad')
        print(match)
        break

    hand_val = MY_HAND_VALS[my_hand]
    total_score += hand_val + score_val

print(f'The total score is: {total_score}')