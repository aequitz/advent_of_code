#include <cstdint>
#include <iostream>


// static constexpr char input0[] =
// #include "day1_input_part2_0.txt"
// // "two1nine\n"
// // "eightwothree\n"
// // "abcone2threexyz\n"
// // "xtwone3four\n"
// // "4nineeightseven2\n"
// // "zoneight234\n"
// // "7pqrstsixteen\n"
// ;
// static constexpr char input1[] =
// #include "day1_input_part2_1.txt"
// ;
// static constexpr char input2[] =
// #include "day1_input_part2_2.txt"
// ;
// static constexpr char input3[] =
// #include "day1_input_part2_3.txt"
// ;
// static constexpr char input4[] =
// #include "day1_input_part2_4.txt"
// ;
// static constexpr char input5[] =
// #include "day1_input_part2_5.txt"
// ;
// static constexpr char input6[] =
// #include "day1_input_part2_6.txt"
// ;
// static constexpr char input7[] =
// #include "day1_input_part2_7.txt"
// ;
static constexpr char input8[] =
#include "day1_input_part2_8.txt"
;
static constexpr char input9[] =
#include "day1_input_part2_9.txt"
;

template<char c>
struct is_digit
{
    static constexpr bool value = '0' <= c && c <= '9';
};

template<char c>
struct letters
{
    static constexpr char arr[] = "\0\0\0\0\0\0";
};
#define MAKE_TEMPLATE(c, name) template<> struct letters<c> { static constexpr char arr[] = name; };
// MAKE_TEMPLATE('0', "zero")
MAKE_TEMPLATE('1', "one")
MAKE_TEMPLATE('2', "two")
MAKE_TEMPLATE('3', "three")
MAKE_TEMPLATE('4', "four")
MAKE_TEMPLATE('5', "five")
MAKE_TEMPLATE('6', "six")
MAKE_TEMPLATE('7', "seven")
MAKE_TEMPLATE('8', "eight")
MAKE_TEMPLATE('9', "nine")

// General case
template<int size1, int index, char current1, char const *str1, int index2, char current2, char const *str2>
struct str_prefix_same
{
    static constexpr int next_index = index + 1;
    static constexpr bool value = current1 == current2 &&
        str_prefix_same<size1, next_index, str1[next_index], str1, index2, str2[index2 + next_index], str2>::value;
};
// str1 (prefix) ends
template<int size1, int index, char const *str1, int index2, char current2, char const *str2>
struct str_prefix_same<size1, index, '\0', str1, index2, current2, str2>
{
    static constexpr bool value = true;
};
// str2 ends
template<int size1, int index, char current1, char const *str1, int index2, char const *str2>
struct str_prefix_same<size1, index, current1, str1, index2, '\0', str2>
{
    static constexpr bool value = false;
};
// both end
template<int size1, int index, char const *str1, int index2, char const *str2>
struct str_prefix_same<size1, index, '\0', str1, index2, '\0', str2>
{
    static constexpr bool value = true;
};
template<int size1, char const *prefix, int index2, char const *str2>
struct str_prefix_same_api
{
    static constexpr bool value = str_prefix_same<size1, 0, prefix[0], prefix, index2, str2[index2], str2>::value;
};

constexpr char one[] = "one";
constexpr char onestring[] = "onestring";
static_assert(str_prefix_same_api<4, one, 0, onestring>::value);
constexpr char lonestring[] = "lonestring";
static_assert(!str_prefix_same_api<4, one, 0, lonestring>::value);
static_assert(str_prefix_same_api<4, one, 1, lonestring>::value);

template<char check_digit, int index, char const *str, char found_digit>
struct is_string_digit
{
    static constexpr char current_digit = str_prefix_same_api<sizeof(letters<check_digit>::arr), letters<check_digit>::arr, index, str>::value ?
        check_digit : '\0';
    static constexpr char digit = found_digit != '\0' ? found_digit :
        (current_digit != '\0' ? current_digit : is_string_digit<check_digit - 1, index, str, found_digit>::digit);
};
template<int index, char const *str, char found_digit>
struct is_string_digit<'0', index, str, found_digit>
{
    static constexpr char digit = found_digit;  // Shortcut from the problem. Sounds like we don't need to check for "zero"
};
template<int index, char const *str>
struct is_string_digit_api
{
    static constexpr char digit = is_string_digit<'9', index, str, '\0'>::digit;
};
static_assert(is_string_digit_api<0, onestring>::digit == '1');
static_assert(is_string_digit_api<1, lonestring>::digit == '1');
constexpr char eight[] = "eight";
static_assert(is_string_digit_api<0, eight>::digit == '8');
static_assert(is_string_digit_api<0, lonestring>::digit == '\0');

template<int t_running_sum, char t_line_tens, char t_line_ones, char current, int index, char const *str>
struct get_sum
{
    static constexpr char current_digit = is_digit<current>::value ? current : is_string_digit_api<index, str>::digit;
    static constexpr char line_tens = t_line_tens != '\0' ? t_line_tens : current_digit;
    static constexpr char line_ones = is_digit<current_digit>::value ? current_digit : t_line_ones;
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
    std::cout << 0
        // + get_sum_api<input0>::value
        // + get_sum_api<input1>::value
        // + get_sum_api<input2>::value
        // + get_sum_api<input3>::value
        // + get_sum_api<input4>::value
        // + get_sum_api<input5>::value
        // + get_sum_api<input6>::value
        // + get_sum_api<input7>::value
        + get_sum_api<input8>::value
        + get_sum_api<input9>::value
        ;
    std::cout << std::endl;
    return 0;
}
