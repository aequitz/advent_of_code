#include <cstdint>
#include <iostream>


static constexpr char input[] =
#include "day1_input copy 2.txt"
// "tmmnhlxzpj1eightldxhjnone97\n"
// "9fivekfpl855mjmfdqzvbn\n"
// "two29eighteight1\n"
;
static constexpr char input2[] =
#include "day1_input copy 3.txt"
;

template<char c>
struct is_digit
{
    static constexpr bool value = '0' <= c && c <= '9';
};

template<int t_running_sum, char t_line_tens, char t_line_ones, char current, int index, char const *str>
struct get_sum
{
    static constexpr char line_tens = t_line_tens != '\0' ? t_line_tens :
        (is_digit<current>::value ? current : '\0');
    static constexpr char line_ones = is_digit<current>::value ? current : t_line_ones;
    static constexpr int running_sum = t_running_sum + (current == '\n' ? 10 * (line_tens - '0') + (line_ones - '0') : 0);
    static constexpr char next_line_tens = current == '\n' ? '\0' : line_tens;
    static constexpr int value = get_sum<running_sum, next_line_tens, line_ones, str[index + 1], index + 1, str>::value;
};

template<int running_sum, char line_tens, char line_ones, int index, char const *str>
struct get_sum<running_sum, line_tens, line_ones, '\0', index, str>
{
    static constexpr int value = running_sum;
};


template<char const *str>
struct get_sum_api
{
    static constexpr int value = get_sum<0, '\0', '\0', *str, 0, str>::value;
};

int main()
{
    std::cout << get_sum_api<input>::value + get_sum_api<input2>::value << std::endl;
    return 0;
}
