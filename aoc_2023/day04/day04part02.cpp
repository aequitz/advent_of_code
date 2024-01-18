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
std::vector<std::string> all_lines;
std::size_t total_cards = 0;
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
    // Import data to string vector
    // Read each line
    while (std::getline(scratch_cards, line))
    {
        all_lines.push_back(line);
    }

    // Create vector for counting total cards won for each hand
    std::vector<size_t> cards_per_hand(all_lines.size(), 1);

    for (std::size_t line_idx = 0; line_idx < all_lines.size(); ++line_idx)
    {
        // Perform number extraction
        std::string line = all_lines[line_idx];
        std::vector<std::string> split_line = split_at_any(line, ":|");
        std::string winning_numbers_str = split_line[1];
        std::string scratch_off_numbers_str = split_line[2];
        std::vector<std::size_t> winning_numbers = extract_numbers(winning_numbers_str);
        std::vector<std::size_t> scratch_off_numbers = extract_numbers(scratch_off_numbers_str);

        // Initialize variables used for counting
        std::double_t numbers_won = 0;
        std::size_t cards_this_hand = cards_per_hand[line_idx];

        // Count numbers won
        for (std::size_t scratch_off_number : scratch_off_numbers)
        {
            for (std::size_t winning_number : winning_numbers)
            {
                if (scratch_off_number == winning_number)
                {
                    // std::cout << "Scratch off number: " << scratch_off_number << " won!" << std::endl;
                    numbers_won++;
                }
            }
        }
        std::cout << "Numbers won for hand " << line_idx + 1 << ": " << numbers_won << std::endl;

        // Add cards to succeeding hands
        for (std::size_t i = 1; i <= numbers_won; ++i)
        {
            cards_per_hand[line_idx + i] += cards_this_hand;
        }

        // Add cards for this hand to total cards
        std::cout << "Total cards for hand " << line_idx + 1 << ": " << cards_this_hand << std::endl;
        total_cards += cards_this_hand;
    }
    std::cout << "Total cards: " << total_cards << std::endl;
}
