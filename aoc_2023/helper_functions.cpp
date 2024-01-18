#include <iostream>
#include <vector>
#include <string>
#include <stdio.h>

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
