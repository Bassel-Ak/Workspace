#include <iostream>
#include <string>

using namespace std;

/*
   1
  121
 12321
1234321
*/

int main()
{
    string input_string {};
    cout << "Enter your string here: ";
    getline(cin,input_string);
    int length = input_string.length();
    int i = 0, j = 0, k = 0, x = 0;
    
    for(i=0; i<length; i++)
    {
        for(j=length - i - 1; j>=0; j--)
        {
            cout << " ";
        }
        for(k=0; k<=i; k++)
        {
            cout << input_string[k];
        }
        for (x = k - 1; x>0; x--)
        {
            cout << input_string[x-1];
        }
        cout << endl;
    }
    return 0;
}


/*
=================================================
instructor's example:
// Letter Pyramid
// Written by Frank J. Mitropoulos

#include <iostream>
#include <string>


int main()
{
    std::string letters{};

    std::cout << "Enter a string of letters so I can create a Letter Pyramid from it: ";
    getline(std::cin, letters);

    size_t num_letters = letters.length();

    int position {0};

    // for each letter in the string
    for (char c: letters) {

        size_t num_spaces = num_letters - position;
        while (num_spaces > 0) {
            std::cout << " ";
            --num_spaces;
        }

        // Display in order up to the current character
        for (size_t j=0; j < position; j++) {
            std::cout << letters.at(j);
        }

        // Display the current 'center' character
        std::cout << c;

        // Display the remaining characters in reverse order
        for (int j=position-1; j >=0; --j) {
            // You can use this line to get rid of the size_t vs int warning if you want
            auto k = static_cast<size_t>(j);
            std::cout << letters.at(k);
        }

        std::cout << std::endl; // Don't forget the end line
        ++position;
    }

    return 0;
}
*/