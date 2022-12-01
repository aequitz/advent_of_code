'''
Decode the alphabetic inputs for
the seven segment display.

Austin Equitz
austin.equitz@gmail.com
'''
def decodeNumber(num_code: str, sig_pattern: list[str]) -> str:
    # Determine patterns for constant numbers
    one = next(x for x in sig_pattern if len(x) == 2)
    four = next(x for x in sig_pattern if len(x) == 4)
    seven = next(x for x in sig_pattern if len(x) == 3)
    eight = next(x for x in sig_pattern if len(x) == 7)

    # Determine if num_code contains some or all of some constant numbers
    contains_one = all(x in num_code for x in list(one))
    contains_four = all(x in num_code for x in list(four))
    contains_half_one = sum([x in num_code for x in list(one)]) == 1
    contains_most_four = sum([x in num_code for x in list(four)]) == 3

    # Constant numbers will have a unique code length
    if len(num_code) == 2: decoded_num = "1"
    if len(num_code) == 4: decoded_num = "4"
    if len(num_code) == 3: decoded_num = "7"
    if len(num_code) == 7: decoded_num = "8"

    # Determine number if length is 6
    if len(num_code) == 6:
        if contains_four:
            decoded_num = "9"
        elif contains_one:
            decoded_num = "0"
        else:
            decoded_num = "6"

    # Determine number if length is 5
    if len(num_code) == 5:
        if contains_half_one and contains_most_four:
            decoded_num = "5"
        elif contains_one:
            decoded_num = "3"
        else:
            decoded_num = "2"

    return decoded_num

if __name__ == '__main__':
    # Open file and create list(list(str))
    with open('DisplayInput.txt', 'r') as fin: d_input = [n.split('|') for n in fin.read().split('\n')]

    # Split each list into separate lists and trim whitespace
    sig_pattern_list,output_list = map(list, zip(*d_input))
    sig_pattern_list = [n.strip().split(' ') for n in sig_pattern_list]
    output_list = [n.strip().split(' ') for n in output_list]

    # Part 1: Determine the amount of unique number segments in the output list
    ones = [item for sublist in output_list for item in sublist if len(item) == 2]
    fours = [item for sublist in output_list for item in sublist if len(item) == 4]
    sevens = [item for sublist in output_list for item in sublist if len(item) == 3]
    eights = [item for sublist in output_list for item in sublist if len(item) == 7]

    print('Sum of Unique Number Segments: ' + str(len(ones + fours + sevens + eights)))

    # Part 2: Decode each output value and sum them all
    output_vals = [""] * len(output_list)
    for idx,val in enumerate(output_list):
        for num_code in val:
            output_vals[idx] += decodeNumber(num_code, sig_pattern_list[idx])

    print('Output Values:\n' + str(output_vals))    
    print('Sum of Output Values: ' + str(sum(int(x) for x in output_vals)))