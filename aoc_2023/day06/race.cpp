#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
#include <cstdlib>

std::vector<std::int64_t> extract_numbers(std::string input)
{
    std::vector<std::int64_t> numbers;
    std::istringstream iss(input);
    std::int64_t number;

    // Read each number separated by spaces and store them in the vector
    while (iss >> number)
    {
        numbers.push_back(number);
    }

    return numbers;
}

std::vector<std::string> read_lines(std::string file_path)
{
    std::ifstream file(file_path);
    std::vector<std::string> lines;
    std::string line;

    // Read each line
    while (std::getline(file, line))
    {
        lines.push_back(line);
    }

    return lines;
}

std::vector<std::string> split_at_any(const std::string input, const std::string delimiters)
{
    std::vector<std::string> result;
    std::int64_t last_pos = 0;
    for (std::int64_t i = 0; i < input.size(); ++i)
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

char *remove_from_string(char *string)
{
    // non_space_count to keep the frequency of non space characters
    int non_space_count = 0;

    // Traverse a string and if it is non space character then, place it at index non_space_count
    for (int i = 0; string[i] != '\0'; i++)
        if (string[i] != ' ')
        {
            string[non_space_count] = string[i];
            non_space_count++; // non_space_count incremented
        }

    // Finally placing final character at the string end
    string[non_space_count] = '\0';
    return string;
}

void calculate_race(std::vector<std::int64_t> times, std::vector<std::int64_t> distances)
{
    std::int64_t races_won = 0;
    std::int64_t race_margin = 1;

    for (std::int64_t i = 0; i < times.size(); ++i)
    {
        std::int64_t distance_to_beat = distances[i];
        std::int64_t race_time = times[i];
        races_won = 0;

        for (std::int64_t i = 1; i < race_time; ++i)
        {
            std::int64_t remaining_time = race_time - i;
            std::int64_t distance_covered = i * remaining_time;
            if (distance_covered > distance_to_beat)
            {
                races_won += 1;
            }
        }
        std::cout << "Races won: " << races_won << std::endl;
        race_margin *= races_won;
    }
    std::cout << "Race margin: " << race_margin << std::endl;
}
int main()
{
    // Part One
    std::vector<std::string> lines = read_lines("race_info.txt");
    std::string times_str = split_at_any(lines[0], ":")[1];
    std::string distances_str = split_at_any(lines[1], ":")[1];
    std::vector<std::int64_t> times = extract_numbers(times_str);
    std::vector<std::int64_t> distances = extract_numbers(distances_str);

    calculate_race(times, distances);

    // Part Two
    // Remove spaces from time string and add to times vector
    times_str.erase(std::remove(times_str.begin(), times_str.end(), ' '), times_str.end());
    std::stringstream sstream(times_str);
    std::int64_t time;
    sstream >> time;
    times = {time};

    // Remove spaces from distance string and add to distances vector
    distances_str.erase(std::remove(distances_str.begin(), distances_str.end(), ' '), distances_str.end());
    std::stringstream sstream_dist(distances_str);
    std::int64_t distance = 0;
    sstream_dist >> distance;
    distances = {distance};

    calculate_race(times, distances);
}
