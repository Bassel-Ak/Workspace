#include <iostream>
#include <vector>

using namespace std;

int main()
{
    vector<int> vector1;
    vector<int> vector2;
    vector1.push_back(10);
    vector1.push_back(20);
    cout << "Vector 1 contains: " << vector1.at(0) << " and " << vector1.at(vector1.size() - 1) << endl;

    vector2.push_back(100);
    vector2.push_back(200);
    cout << "Vector 2 contains: " << vector2.at(0) << " and " << vector2.at(vector2.size() - 1) << endl;

    vector<vector<int>> vector_2d;
    vector_2d.push_back(vector1);
    vector_2d.push_back(vector2);
    cout << "Vector_2d contains: \n"
         << vector_2d.at(0).at(0) << " "
         << vector_2d.at(0).at(1) << endl
         << vector_2d.at(1).at(0) << " "
         << vector_2d.at(1).at(1)
         << endl;

    vector1.at(0) = 1000;

    cout << "2nd attempt: Vector_2d contains: \n"
         << vector_2d.at(0).at(0) << " "
         << vector_2d.at(0).at(1) << endl
         << vector_2d.at(1).at(0) << " "
         << vector_2d.at(1).at(1)
         << endl;

    cout << "2nd attempt: Vector 1 contains: " << vector1.at(0) << " and " << vector1.at(vector1.size() - 1) << endl;

    return 0;
}