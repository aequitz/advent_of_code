#ifndef HELPER_FUNCTIONS_H
#define HELPER_FUNCTIONS_H

#include <iostream>
#include <vector>
#include <string>
#include <stdio.h>

std::vector<std::string> split_at_any(const std::string input, const std::string delimiters);

std::size_t first_number(std::string const &str);

#endif // HELPER_FUNCTIONS_H
