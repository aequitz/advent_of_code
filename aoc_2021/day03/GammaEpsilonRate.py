'''
Determine the most common binary number
for each binary positon. Create

Austin Equitz
austin.equitz@gmail.com
'''

import os
import collections
import difflib

def closestMatch(list_in: list[str], substring: str) -> str:
    for i in range(len(substring)):
        match_list = [s for s in list_in if substring[0:len(substring)-i] in s]
        
        if match_list != []:
            print(match_list)
            match = match_list[0]
            break

    return match

def rollingMostCommonMatch(list_in: list[str]) -> str:
    most_common_list = list_in

    for num in range(len(max(most_common_list, key=len))):
        index_list = [x[num] if num < len(x) else "" for x in most_common_list]

        common_list = collections.Counter(index_list).most_common()

        # Make 1 the most common if 0/1 are equally common
        if common_list[0][1] == common_list[-1][1] and common_list[0][0] != '1':
            common_list = [common_list[-1], common_list[0]]

        most_common = common_list[0][0]

        most_common_list = [x for x in most_common_list if x[num] == most_common in x]

        if len(most_common_list) == 1: break
    
    return most_common_list[0]

def rollingLeastCommonMatch(list_in: list[str]) -> str:
    least_common_list = list_in

    for num in range(len(max(least_common_list, key=len))):
        index_list = [x[num] if num < len(x) else "" for x in least_common_list]

        common_list = collections.Counter(index_list).most_common()

        # Make 0 the least common if 0/1 are equally common
        if common_list[0][1] == common_list[-1][1] and common_list[-1][0] != '0':
            common_list = [common_list[-1], common_list[0]]
            

        least_common = common_list[-1][0]

        least_common_list = [x for x in least_common_list if x[num] == least_common in x]

        if len(least_common_list) == 1: break
    
    return least_common_list[0]


def findCommonString(list_in: list[str]) -> tuple:
    most_common = ""
    least_common = ""
    for num in range(len(max(list_in, key=len))):
        index_list = [x[num] if num < len(x) else "" for x in list_in]

        common_list = collections.Counter(index_list).most_common()

        most_common = most_common + common_list[0][0]
        least_common = least_common + common_list[-1][0]

    return most_common,least_common

if __name__ == '__main__':
    rel_path = 'BinaryNumbers.txt'
    file_path = os.path.join(os.path.dirname(__file__), rel_path)

    # Reads in text file as list[str]
    with open(file_path, 'r') as fin: bin_nums = [n.strip() for n in fin.readlines()]

    # Part 1: Determine gamma_rate (most common for each index) and epsilon_rate (least common for each index)
    #         and multiply to get power_consumption
    gamma_rate,epsilon_rate = findCommonString(bin_nums)
    power_consumption = int(gamma_rate, 2) * int(epsilon_rate, 2)
    print('Gamma rate: ' + gamma_rate)
    print('Epsilon rate: ' + epsilon_rate)
    print('Power consumption: ' + str(power_consumption))

    # Part 2
    oxy_gen = rollingMostCommonMatch(bin_nums)
    co2_scrubber = rollingLeastCommonMatch(bin_nums)
    life_support_rating = int(oxy_gen, 2) * int(co2_scrubber, 2)
    print('Oxy Gen: ' + oxy_gen)
    print('CO2 Scrubber: ' + co2_scrubber)
    print('Life Support Rating: ' + str(life_support_rating))