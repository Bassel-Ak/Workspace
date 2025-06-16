#include <iostream>
#include "Vectors.hpp"

using namespace std;

/*
Vectors Problems:
    Problem #1: Right rotation
    Problem #2: Left rotation
    Problem #3: Right rotation with index
    Problem #4: Left rotation with index
    Problem #5:
*/

int main()
{
    int n = 10;
    Vector v(n);
    for(int i = 0; i < n; i++)
        v.set(i,i); // 0 1 2 3 4 5
    // v.rotateRight(4);
    // v.rotateLeft();
    // v.rotateLeft(5);
    // v.pop(16);
    v.find_transposition(8);
    v.printVector();
    return 0;
}