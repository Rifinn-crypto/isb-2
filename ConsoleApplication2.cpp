#include <iostream>

int main()
{
    srand(time(0));
    int randNum = std::rand() % 12347;
    bool num;
    for (int i = 0; i < 128; i++)
    {
        randNum = (randNum * 222 + 4) % 12347;
        num = randNum % 2;
        std::cout << num;
    }
    return 0;
}
//11101111111101101110100110110100111011101011011010111010000110100101110011011011010000100101010010000000011110001100011110011000