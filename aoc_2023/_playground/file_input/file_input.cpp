#include <iostream>

static constexpr char input[] =
#include "file.txt"
    ;

int main()
{
    for (std::size_t i = 0; i < sizeof(input); ++i)
    {
        std::cout << input[i] << std::endl;
    }
    return 0;
}
