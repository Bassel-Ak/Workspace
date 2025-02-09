#include <iostream>
#include <vector>
#include <limits>

using namespace std;

int main()
{
    vector<int> numbers;
    char selection = ' ';
    int i = 0;
    do{
        // Menu display
        cout << "\n--------------" << endl
        << "P - Print numbers" << endl
        << "A - Add a number" << endl
        << "M - Display mean of the numbers" << endl
        << "S - Display the smallest number" << endl
        << "L - Display the largest number" << endl
        << "C - Clear the list" << endl
        << "F - Find a number" << endl
        << "I - Print number in a specific index" << endl
        << "Q - Quit" << endl
        << "\nEnter your choice: ";

        int number_entered = 0, sum = 0, smallest = 0, largest = 0, index = 0, search = 0, times = 0, found = false;
        double mean = 0.0;
        cin >> selection;
        if (cin.fail())
        {
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            cout << "Invalid input. Please enter a number." << endl;
            continue;
        }
        selection = tolower(selection);
        switch(selection)
        {
            case 'p':
                if(!numbers.empty())
                {
                    // Display [1 2 3 4 5]
                    cout << "[ ";
                    for(i = 0; i < numbers.size(); i++)
                        cout << numbers.at(i) << " ";
                    cout << "]";
                }
                else
                    cout << "[] - the list is empty";
                break;
            
            case 'a':
                cout << "Enter the number you want to add: ";
                cin >> number_entered;
                if (cin.fail())
                {
                    cin.clear();
                    cin.ignore(numeric_limits<streamsize>::max(), '\n');
                    cout << "Invalid input. Please enter a number." << endl;
                    continue;
                }
                numbers.push_back(number_entered);
                cout << number_entered << " added";
                break;
            case 'm':
                if(!numbers.empty())
                {
                    for(i = 0; i < numbers.size(); i++)
                        sum += numbers.at(i);
                    mean = sum/numbers.size();
                    cout << "Mean of the numbers in the list is: " << mean;
                }
                else
                    cout << "Unable to calculate the mean - no data";
                break;
            case 's':
                if (!numbers.empty())
                {
                    smallest = numbers.at(0);
                    for (i = 1; i < numbers.size(); i++)
                    {
                        if (numbers.at(i) < smallest)
                            smallest = numbers.at(i);
                    }
                    cout << "Smallest number in the list is: " << smallest;
                    break;
                }
                else
                    cout << "Unable to determine the smallest number - list is empty";
                break;
            case 'l':
                if (!numbers.empty())
                {
                    largest = numbers.at(0);
                    for (i = 1; i < numbers.size(); i++)
                    {
                        if (numbers.at(i) > largest)
                            largest = numbers.at(i);
                    }
                    cout << "Largest number in the list is: " << largest;
                    break;
                }
                else
                    cout << "Unable to determine the largest number - list is empty";
                break;
            case 'c':
                if (!numbers.empty())
                {
                    numbers.clear();
                    cout << "List is cleared";
                }
                else
                    cout << "List is already empty.";
                break;
            case 'f':
                if(!numbers.empty())
                {
                    cout << "Enter the number you are searching for: ";
                    cin >> search;
                    if (cin.fail())
                    {
                        cin.clear();
                        cin.ignore(numeric_limits<streamsize>::max(), '\n');
                        cout << "Invalid input. Please enter a number." << endl;
                        continue;
                    }
                    for(i = 0; i < numbers.size(); i++)
                    {
                        if(numbers.at(i) == search)
                            times++;
                            found = true;
                    }
                    if(found)
                        cout << search << " was found in the list " << times << " times.";
                    else
                        cout << search << " was not found in the list.";
                }
                else
                    cout << "Cannot find the number - list is empty";
                break;
            case 'i':
                if(!numbers.empty())
                {
                    cout << "Enter the index of the number: ";
                    cin >> index;
                    if (cin.fail())
                    {
                        cin.clear();
                        cin.ignore(numeric_limits<streamsize>::max(), '\n');
                        cout << "Invalid input. Please enter a number." << endl;
                        continue;
                    }
                    if (index >= 0 && index < numbers.size())
                        cout << "The number at index " << index << " is: " << numbers.at(index) << endl;
                    else 
                        cout << "Unable to print the number - index is out of range";
                    }
                else
                    cout << "Unable to print the number - list is empty.";
                break;
            case 'q':
                cout << "Goodbye\n";
                break;
                
            default:
                cout << "Wrong entry .. try again";
                break;
        }

    }while(selection != 'q');

    return 0;
}