// #include "../helper_functions.h"
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <cstddef>
#include <cmath>

// Declare variables
std::ifstream scratch_cards("scratch_cards.txt");
std::size_t scratch_off_sum = 0;
std::string line;
std::vector<std::string> winning_numbers;

// Helper functions
std::vector<std::string> split_at_any(const std::string input, const std::string delimiters)
{
    std::vector<std::string> result;
    std::size_t last_pos = 0;
    for (std::size_t i = 0; i < input.size(); ++i)
    {
        if (delimiters.find(input[i]) != delimiters.npos)
        {
            result.push_back(input.substr(last_pos, i - last_pos));
            ++i;
            last_pos = i;
        }
    }
    result.push_back(input.substr(last_pos, last_pos - input.size()));

    return result;
}

std::vector<std::size_t> extract_numbers(std::string input)
{
    std::vector<std::size_t> numbers;
    std::istringstream iss(input);
    std::size_t number;

    // Read each number separated by spaces and store them in the vector
    while (iss >> number)
    {
        numbers.push_back(number);
    }

    return numbers;
}

int main()
{
    // Read each line
    while (std::getline(scratch_cards, line))
    {
        std::vector<std::string> split_line = split_at_any(line, ":|");
        std::string winning_numbers_str = split_line[1];
        std::string scratch_off_numbers_str = split_line[2];
        std::vector<std::size_t> winning_numbers = extract_numbers(winning_numbers_str);
        std::vector<std::size_t> scratch_off_numbers = extract_numbers(scratch_off_numbers_str);

        std::double_t numbers_won = 0;
        for (std::size_t scratch_off_number : scratch_off_numbers)
        {
            for (std::size_t winning_number : winning_numbers)
            {
                if (scratch_off_number == winning_number)
                {
                    std::cout << "Scratch off number: " << scratch_off_number << " won!" << std::endl;
                    numbers_won++;
                }
            }
        }
        std::cout << "Numbers won: " << numbers_won << std::endl;
        if (numbers_won > 0)
        {
            numbers_won = std::pow(2, numbers_won - 1);
        }
        std::cout << "Points from line: " << scratch_off_sum << std::endl;
        scratch_off_sum += numbers_won;
    }
    std::cout << "Scratch off sum: " << scratch_off_sum << std::endl;
}
