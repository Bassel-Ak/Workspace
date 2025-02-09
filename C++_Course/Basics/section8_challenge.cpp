#include <iostream>

using namespace std;

int main()
{
    // Code better be solved with / and %
    cout << "Enter the number of cents: ";
    int cents = 0;
    cin >> cents;
    int dollars = 0;
    int quarter = 0;
    int dime = 0;
    int nickel = 0;
    int penny = 0;
    while (cents > 0)
    {
        if (cents >= 100)
        {
            dollars++;
            cents -= 100;
        }
        else if (cents >= 25)
        {
            quarter++;
            cents -= 25;
        }
        else if(cents >= 10)
        {
            dime++;
            cents -= 10;
        }
        else if(cents >= 5)
        {
            nickel++;
            cents -= 5;
        }
        else if(cents >= 1)
        {
            penny++;
            cents -= 1;
        }
    }
    cout << "Your change will be: " << endl
         << "Dollars: " << dollars << endl
         << "Quarters: " << quarter << endl
         << "Dimes: " << dime << endl
         << "Nickels: " << nickel << endl
         << "Pennies: " << penny << endl;
    return 0;
}