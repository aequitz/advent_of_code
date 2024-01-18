#include <iostream>
#include <fstream>
#include <string>
#include <vector>

// open file
std::ifstream file("somefile.txt");

std::string line;
std::vector<std::string> myLines;

int main()
{
    // read each line
    while (std::getline(file, line))
    {
        myLines.push_back(line);
    }
    for (std::size_t i = 0; i < myLines.size(); ++i)
    {
        std::cout << "Line " << i << ": ";
        std::cout << myLines[i] << std::endl;
    }
}
