import os
calibration = open("AdventOfCode/aoc_2023/day01/calibration.txt")
calibration_sum = 0
numbers = "0123456789"
number_strings = [
    "one", "two", "three", "four", "five",
    "six", "seven", "eight", "nine", "1", "2",
    "3", "4", "5", "6", "7", "8", "9"
]

first_num_index = float('inf')
first_num_str_index = 0
last_num_index = -1
last_num_str_index = 0
first_num_str_idx_found = 0
last_num_str_idx_found = 0
first_num = ""
first_num_str = ""
last_num = ""
last_num_str = ""
line_sum = ""

def word_to_number(word):
    if word == "one":
        return "1"
    elif word == "two":
        return "2"
    elif word == "three":
        return "3"
    elif word == "four":
        return "4"
    elif word == "five":
        return "5"
    elif word == "six":
        return "6"
    elif word == "seven":
        return "7"
    elif word == "eight":
        return "8"
    elif word == "nine":
        return "9"
    else:
        return word

print("Sum of each line: ")

for line in calibration:
    line = line.strip()
    first_num_index = float('inf')
    last_num_index = 0
    first_num = "None"
    last_num = "None"

    print("Line:", line)

    for number_string in number_strings:
        first_num_str_idx_found = line.find(number_string)
        last_num_str_idx_found = line.rfind(number_string)

        if first_num_str_idx_found != -1:
            if first_num_str_idx_found < first_num_index:
                first_num_index = first_num_str_idx_found
                first_num = word_to_number(number_string)

        if last_num_str_idx_found != -1:
            if last_num_str_idx_found > last_num_index:
                last_num_index = last_num_str_idx_found
                last_num = word_to_number(number_string)

        if last_num == "None":
            last_num = first_num

    line_sum = first_num + last_num
    print(line_sum)
    calibration_sum += int(line_sum)

print("Sum of all lines:", calibration_sum)
calibration.close()
