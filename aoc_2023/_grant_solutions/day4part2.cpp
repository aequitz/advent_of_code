#include <iostream>

static constexpr char input[] =
#include "input_quoted.txt"
// "Card   1: 79 93 21 74 81 76 17 89  3  5 |  5 67 87 81 76 35 79 21 15 80  8 74 99 28  3 23 19 42 89 16 22 77 92 70 34"
// "Card   2: 83 16 24 23 59 70 14 57 74 53 | 79 82 70 23 61 14 74 57 36 37 59 72 83 16  3  2 28 63 50 60 38 86 97 24 53"
// "Card   3: 12 77 13 14 48 55 69  4 18 81 | 69  7 94 88 18 73 55 48 49 81 14 21 12 15  5 27 22 84 51 52 13 77  4 57 17"
;

static constexpr int n_candidates = 25;
static constexpr int n_winner_start = 10;
static constexpr int n_candidate_start = 42;
static constexpr int n_chars_per_line = 116;
static constexpr int n_lines = 218;

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

template<char const *str, int index, int n_cards, int copies0, int copies1, int copies2, int copies3, int copies4, int copies5, int copies6, int copies7, int copies8, int copies9>
struct get_sum
{
    static constexpr uint64_t winning_map_low =
        get_map<get_value<str, index + n_winner_start>::value, false>::value |
        get_map<get_value<str, index + n_winner_start + 3>::value, false>::value |
        get_map<get_value<str, index + n_winner_start + 6>::value, false>::value |
        get_map<get_value<str, index + n_winner_start + 9>::value, false>::value |
        get_map<get_value<str, index + n_winner_start + 12>::value, false>::value |
        get_map<get_value<str, index + n_winner_start + 15>::value, false>::value |
        get_map<get_value<str, index + n_winner_start + 18>::value, false>::value |
        get_map<get_value<str, index + n_winner_start + 21>::value, false>::value |
        get_map<get_value<str, index + n_winner_start + 24>::value, false>::value |
        get_map<get_value<str, index + n_winner_start + 27>::value, false>::value;
    static constexpr uint64_t winning_map_high =
        get_map<get_value<str, index + n_winner_start>::value, true>::value |
        get_map<get_value<str, index + n_winner_start + 3>::value, true>::value |
        get_map<get_value<str, index + n_winner_start + 6>::value, true>::value |
        get_map<get_value<str, index + n_winner_start + 9>::value, true>::value |
        get_map<get_value<str, index + n_winner_start + 12>::value, true>::value |
        get_map<get_value<str, index + n_winner_start + 15>::value, true>::value |
        get_map<get_value<str, index + n_winner_start + 18>::value, true>::value |
        get_map<get_value<str, index + n_winner_start + 21>::value, true>::value |
        get_map<get_value<str, index + n_winner_start + 24>::value, true>::value |
        get_map<get_value<str, index + n_winner_start + 27>::value, true>::value;

    static constexpr int n_matching = get_matches_api<str, index + n_candidate_start, winning_map_low, winning_map_high, n_candidates>::value;

    static constexpr int copies_this = 1 + copies0;
    static constexpr int new_copies1 = copies1 + (n_matching >= 1 ? copies_this : 0);
    static constexpr int new_copies2 = copies2 + (n_matching >= 2 ? copies_this : 0);
    static constexpr int new_copies3 = copies3 + (n_matching >= 3 ? copies_this : 0);
    static constexpr int new_copies4 = copies4 + (n_matching >= 4 ? copies_this : 0);
    static constexpr int new_copies5 = copies5 + (n_matching >= 5 ? copies_this : 0);
    static constexpr int new_copies6 = copies6 + (n_matching >= 6 ? copies_this : 0);
    static constexpr int new_copies7 = copies7 + (n_matching >= 7 ? copies_this : 0);
    static constexpr int new_copies8 = copies8 + (n_matching >= 8 ? copies_this : 0);
    static constexpr int new_copies9 = copies9 + (n_matching >= 9 ? copies_this : 0);
    static constexpr int new_copies10 = n_matching >= 10 ? copies_this : 0;

    static constexpr int value = get_sum<str, index + n_chars_per_line, n_cards + copies_this,
        new_copies1, new_copies2, new_copies3, new_copies4, new_copies5,
        new_copies6, new_copies7, new_copies8, new_copies9, new_copies10
    >::value;
};
template<char const *str, int running_sum, int copies0, int copies1, int copies2, int copies3, int copies4, int copies5, int copies6, int copies7, int copies8, int copies9>
struct get_sum<str, n_chars_per_line*n_lines, running_sum, copies0, copies1, copies2, copies3, copies4, copies5, copies6, copies7, copies8, copies9>
{
    static constexpr int value = running_sum;
};

template<char const *str>
struct get_sum_api
{
    static constexpr int value = get_sum<str, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0>::value;
};


int main()
{
    std::cout << get_sum_api<input>::value << std::endl;
    return 0;
}
