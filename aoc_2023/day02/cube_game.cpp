// Includes
#include <iostream>
#include <fstream>
#include <string>
#include <stdio.h>
#include <vector>

std::size_t max_red = 12;
std::size_t max_green = 13;
std::size_t max_blue = 14;

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

std::size_t first_number(std::string const &str)
{
    char const *digits = "0123456789";
    std::size_t const n = str.find_first_of(digits);
    std::string number_string;
    if (n != std::string::npos)
    {
        std::size_t const m = str.find_first_not_of(digits, n);
        number_string = str.substr(n, m != std::string::npos ? m - n : m);
        return std::stoi(number_string);
    }
    return 0;
}

int main()
{
    // Open file
    std::ifstream games("cube_games.txt");
    std::string line;
    std::size_t game_id_sum = 0;
    std::size_t power_cubes_sum = 0;

    // Parse each line
    while (std::getline(games, line))
    {
        // Split line by ":"
        std::vector<std::string> split_line = split_at_any(line, ":");
        std::string game_str = split_line[0];
        std::string game_cubes = split_line[1];

        // Get game ID (remove "Game ")
        std::size_t game_id = first_number(game_str);
        // std::cout << "Game ID: " << game_id << std::endl;
        // std::cout << "Game cubes: " << game_cubes << std::endl;

        // // Split each game by ";" or ","
        std::vector<std::string> game_cubes_split = split_at_any(game_cubes, ";,");

        bool isPossible = true;
        std::size_t most_red = 1;
        std::size_t most_green = 1;
        std::size_t most_blue = 1;
        for (const auto &cube_set : game_cubes_split)
        {
            // Get number of cubes
            std::size_t num_cubes = first_number(cube_set);

            // If red in color, make sure it doesn't exceed 12
            bool redExceeds = cube_set.find("red") != std::string::npos && num_cubes > max_red;
            // If green in color, make sure it doesn't exceed 13
            bool greenExceeds = cube_set.find("green") != std::string::npos && num_cubes > max_green;
            // If blue in color, make sure it doesn't exceed 14
            bool blueExceeds = cube_set.find("blue") != std::string::npos && num_cubes > max_blue;

            // Game is not possible for any of these conditions
            if (redExceeds || greenExceeds || blueExceeds)
            {
                std::cout << "Game " << game_id << " is not possible" << std::endl;
                isPossible = false;
            }

            // Update most red, green, and blue
            if (cube_set.find("red") != std::string::npos && num_cubes > most_red)
            {
                most_red = num_cubes;
            }
            if (cube_set.find("green") != std::string::npos && num_cubes > most_green)
            {
                most_green = num_cubes;
            }
            if (cube_set.find("blue") != std::string::npos && num_cubes > most_blue)
            {
                most_blue = num_cubes;
            }
        }

        // Add game ID to possible_games_sum
        if (isPossible)
        {
            game_id_sum += game_id;
        }

        // Add most red, green, and blue to power_cubes_sum
        power_cubes_sum += most_red * most_green * most_blue;
    }

    std::cout << "Sum of possible games: " << game_id_sum << std::endl;
    std::cout << "Sum of power cubes: " << power_cubes_sum << std::endl;
}
