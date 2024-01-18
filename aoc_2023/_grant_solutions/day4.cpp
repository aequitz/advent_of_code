#include <iostream>

static constexpr char input[] =
#include "input_quoted.txt"
// "Card   1: 79 93 21 74 81 76 17 89  3  5 |  5 67 87 81 76 35 79 21 15 80  8 74 99 28  3 23 19 42 89 16 22 77 92 70 34"
// "Card   2: 83 16 24 23 59 70 14 57 74 53 | 79 82 70 23 61 14 74 57 36 37 59 72 83 16  3  2 28 63 50 60 38 86 97 24 53"
// "Card   3: 12 77 13 14 48 55 69  4 18 81 | 69  7 94 88 18 73 55 48 49 81 14 21 12 15  5 27 22 84 51 52 13 77  4 57 17"
;

template<char const *str, int index>
struct get_value
{
    static constexpr int value = (str[index] != ' ' ? ((str[index] - '0') * 10) : 0)
        + (str[index + 1] - '0');
};

template<int x, bool high>
struct get_map
{
    static constexpr bool x_is_high = x >= 64;
    static constexpr uint64_t value = x_is_high == high ? (1uLL << (x & 0x3F)) : 0;
};

template<char const *str, int index, uint64_t winning_map_low, uint64_t winning_map_high, int n_nums_left, int n_matches>
struct get_matches
{
    static constexpr int current = get_value<str, index>::value;
    static constexpr bool is_match = current >= 64 ? ((1uLL << (current - 64)) & winning_map_high) : ((1uLL << current) & winning_map_low);
    static constexpr int value = get_matches<str, index + 3, winning_map_low, winning_map_high, n_nums_left - 1, n_matches + is_match>::value;
};
template<char const *str, int index, uint64_t winning_map_low, uint64_t winning_map_high, int n_matches>
struct get_matches<str, index, winning_map_low, winning_map_high, 0, n_matches>
{
    static constexpr int value = n_matches;
};
template<char const *str, int index, uint64_t winning_map_low, uint64_t winning_map_high, int n_nums_left>
struct get_matches_api
{
    static constexpr int value = get_matches<str, index, winning_map_low, winning_map_high, n_nums_left, 0>::value;
};

template<int matches>
struct to_score
{
    static constexpr int value = 1 << (matches - 1);
};
template<>
struct to_score<0>
{
    static constexpr int value = 0;
};

template<char const *str, int index, int running_sum>
struct get_sum
{
    static constexpr uint64_t winning_map_low =
        get_map<get_value<str, index + 10>::value, false>::value |
        get_map<get_value<str, index + 13>::value, false>::value |
        get_map<get_value<str, index + 16>::value, false>::value |
        get_map<get_value<str, index + 19>::value, false>::value |
        get_map<get_value<str, index + 22>::value, false>::value |
        get_map<get_value<str, index + 25>::value, false>::value |
        get_map<get_value<str, index + 28>::value, false>::value |
        get_map<get_value<str, index + 31>::value, false>::value |
        get_map<get_value<str, index + 34>::value, false>::value |
        get_map<get_value<str, index + 37>::value, false>::value;
    static constexpr uint64_t winning_map_high =
        get_map<get_value<str, index + 10>::value, true>::value |
        get_map<get_value<str, index + 13>::value, true>::value |
        get_map<get_value<str, index + 16>::value, true>::value |
        get_map<get_value<str, index + 19>::value, true>::value |
        get_map<get_value<str, index + 22>::value, true>::value |
        get_map<get_value<str, index + 25>::value, true>::value |
        get_map<get_value<str, index + 28>::value, true>::value |
        get_map<get_value<str, index + 31>::value, true>::value |
        get_map<get_value<str, index + 34>::value, true>::value |
        get_map<get_value<str, index + 37>::value, true>::value;

    static constexpr int n_matching = get_matches_api<str, index + 42, winning_map_low, winning_map_high, 25>::value;
    static constexpr int score = to_score<n_matching>::value;

    static constexpr int value = get_sum<str, index + 116, running_sum + score>::value;
};
template<char const *str, int running_sum>
struct get_sum<str, 116*218, running_sum>
{
    static constexpr int value = running_sum;
};

template<char const *str>
struct get_sum_api
{
    static constexpr int value = get_sum<str, 0, 0>::value;
};


int main()
{
    std::cout << get_sum_api<input>::value << std::endl;
    return 0;
}
