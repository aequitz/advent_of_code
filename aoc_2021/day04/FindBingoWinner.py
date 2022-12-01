'''
Play a game of bingo and determine
which bingo card will win first. Add
up all of the remaining numbers on the board
and multiply it by the number that was called
that allowed that card to win.

Austin Equitz
austin.equitz@gmail.com
'''

import os
import numpy as np

def markBingoNumber(bingo_cards: list[np.ndarray], bingo_num: str) -> list[np.ndarray]:
    for idx,card in enumerate(bingo_cards):
        bingo_cards[idx] = [['X' if n == bingo_num else n for n in s] for s in card]

    return bingo_cards

def checkBingoWin(bingo_cards: list[np.ndarray]) -> tuple:
    win_return = False
    cards = []
    indexes = []
    for idx,card in enumerate(bingo_cards):
        win = False
        # Check rows
        for row in card:
            if np.all(row == row[0]):
               win = True

        # Check columns
        card_transpose = card.T
        for column in card_transpose:
            if np.all(column == column[0]):
               win = True

        if win:
            win_return = True
            cards.append(card)
            indexes.append(idx)

    return win_return,cards,indexes



if __name__ == '__main__':
    # File input
    rel_path = 'BingoCardAndNumbers.txt'
    file_path = os.path.join(os.path.dirname(__file__), rel_path)

    # Reads in text file as list[str]
    with open(file_path, 'r') as fin: bingo_in = fin.read().split('\n\n')

    # Get bingo numbers
    bingo_nums = bingo_in[0].split(',')

    # Form bingo cards into numpy array of 2d numpy arrays
    bingo_cards_2d = [n.split() for n in bingo_in[1:]]
    bingo_cards_3d = []
    for card in bingo_cards_2d: bingo_cards_3d = bingo_cards_3d + [np.reshape(card, (5, 5))]
    bingo_cards_3d = np.array(bingo_cards_3d)

    # Play bingo
    for num in bingo_nums:
        bingo_cards_3d = markBingoNumber(bingo_cards_3d, num)

        win,winning_cards,wcard_idxs = checkBingoWin(bingo_cards_3d)

        if win:
            winning_card_current = winning_cards[len(winning_cards)-1]
            winning_num = num
            bingo_cards_3d = np.delete(bingo_cards_3d, wcard_idxs, axis=0)
            # Uncomment for part one
            # winning_card_current = winning_cards[0]
            # break
        
    winning_card_1d = np.reshape(winning_card_current, 25)
    remaining_numbers = list(map(int, [x for x in winning_card_1d if not 'X' in x]))
    print(winning_card_current)
    print(remaining_numbers)
    print(winning_num)
    print(np.sum(remaining_numbers) * int(winning_num))