#include <iostream>

using namespace std;

class Vector
{
    private:
        int *arr;
        int size;
        int capacity;

    public:
        Vector(int size);
        ~Vector();
        int get(int index) const;
        int getSize() const;
        void set(int index, int value);
        void push_back(int value);
        void expand_capacity();
        void insert(int index, int value);
        int find(int value);
        void rotateRight();
        void rotateRight(int times);
        void rotateLeft();
        void rotateLeft(int times);
        int pop(int index);
        int find_transposition(int value);
        void printVector();
};