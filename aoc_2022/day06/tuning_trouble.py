'''
Day 6: Tuning Trouble

Austin Equitz
austin.equitz@gmail.com
'''

with open('comms_signal.txt', 'r') as fin: signal = fin.read()

def findStartMarker(signal_content: str, marker_len: int) -> int:
    for start_idx in range(0, len(signal_content) - marker_len):
        # Get stop index based off of marker length
        stop_idx = start_idx + marker_len

        # Get data and unique characters
        data = signal_content[start_idx:stop_idx]
        unique_chars = set(data)

        # Stop when all characters are unique
        if len(unique_chars) == marker_len:
            return stop_idx

if __name__ == '__main__':
    # Part One
    part_one_data_idx = findStartMarker(signal, 4)
    print(f'The data start index for part one is: {part_one_data_idx}')

    # Part Two
    part_two_data_idx = findStartMarker(signal, 14)
    print(f'The data start index for part two is: {part_two_data_idx}')




