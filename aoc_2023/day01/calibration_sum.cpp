#include <iostream>
#include <fstream>
#include <string>
#include <list>

// Declare variables
std::ifstream calibration("calibration.txt");
std::size_t calibration_sum = 0;
std::string line;
std::string numbers = "0123456789";
std::list<std::string> number_strings = {
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
};

size_t first_num_index = UINT_MAX;
size_t first_num_str_index;
size_t last_num_index;
size_t last_num_str_index;
size_t first_num_str_idx_found;
size_t last_num_str_idx_found;
std::string first_num;
std::string first_num_str;
std::string last_num;
std::string last_num_str;
std::string line_sum;

std::string wordToNumber(const std::string &word)
{
    if (word == "one")
    {
        return "1";
    }
    else if (word == "two")
    {
        return "2";
    }
    else if (word == "three")
    {
        return "3";
    }
    else if (word == "four")
    {
        return "4";
    }
    else if (word == "five")
    {
        return "5";
    }
    else if (word == "six")
    {
        return "6";
    }
    else if (word == "seven")
    {
        return "7";
    }
    else if (word == "eight")
    {
        return "8";
    }
    else if (word == "nine")
    {
        return "9";
    }
    else
    {
        return word;
    }
}

int main()
{

    // Part 1
    // Only run if file exists
    // std::cout << "Sum of each line: " << std::endl;

    // // Read each line
    // while (std::getline(calibration, line))
    // {
    //     // Find first number
    //     first_num_index = line.find_first_of(numbers);
    //     first_num = line.substr(first_num_index, 1);

    //     // Find last number
    //     last_num_index = line.find_last_of(numbers);
    //     last_num = line.substr(last_num_index, 1);

    //     // Combine first and last number and add to sum
    //     line_sum = first_num + last_num;
    //     std::cout << line_sum << std::endl;
    //     calibration_sum += std::stoi(line_sum);
    // }

    // std::cout << "Sum of all lines: " << calibration_sum << std::endl;

    // Part 2 Only run if file exists
    // Reset file and variables
    // calibration.clear();
    // calibration.seekg(0);
    // calibration_sum = 0;

    std::cout << "Sum of each line: " << std::endl;

    // Read each line
    while (std::getline(calibration, line))
    {
        first_num_index = UINT_MAX;
        last_num_index = 0;
        first_num = "None";
        last_num = "None";

        std::cout << "Line: " << line << std::endl;
        // Find first number
        for (std::string number_string : number_strings)
        {
            // Search for number string
            first_num_str_idx_found = line.find(number_string);
            last_num_str_idx_found = line.rfind(number_string);

            if (first_num_str_idx_found != std::string::npos)
            {
                // std::cout << "Number found: " << number_string << " at index " << first_num_str_idx_found << std::endl;
                // Check if number string is before first number
                if (first_num_str_idx_found < first_num_index)
                {
                    // std::cout << "Found number " << number_string << " before number " << first_num << std::endl;
                    first_num_index = first_num_str_idx_found;
                    first_num = wordToNumber(number_string);
                }
            }

            if (last_num_str_idx_found != std::string::npos)
            {
                // std::cout << "Number found: " << number_string << " at index " << last_num_str_idx_found << std::endl;
                // Check if number string is after last number
                if (last_num_str_idx_found > last_num_index)
                {
                    // std::cout << "Found number " << number_string << " after number " << last_num << std::endl;
                    last_num_index = last_num_str_idx_found;
                    last_num = wordToNumber(number_string);
                }
            }
        }

        // std::cout << "First number: " << first_num << std::endl;
        // std::cout << "Last number: " << last_num << std::endl;
        if (last_num == "None")
        {
            last_num = first_num;
        }
        // Combine first and last number and add to sum
        line_sum = first_num + last_num;
        std::cout << line_sum << std::endl;
        calibration_sum += std::stoi(line_sum);
    }
    std::cout << "Sum of all lines: " << calibration_sum << std::endl;
}
