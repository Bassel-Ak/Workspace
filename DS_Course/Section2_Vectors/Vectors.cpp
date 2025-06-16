#include <iostream>
#include "Vectors.hpp"

using namespace std;

// Constructor implementation
Vector::Vector(int size) : 
size(size),
capacity(size * 2)
{
	cout<<"size: " << size << " capacity: " << capacity << endl;
	if(size < 0)
		size = 1;
	arr = new int[capacity];
	for(int i = 0; i < size; i++)
	{
		arr[i] = 0;
	}
}

Vector::~Vector()
{
	delete[] arr;
}

int Vector::get(int index) const // Const was used here as a compiler enforcement of not changing any private variables
{
	if(index < 0 || index >= size)
		return -1;
	return arr[index];
}

int Vector::getSize() const
{
	return size;
}

void Vector::set(int index, int value)
{
	if(index < 0 || index >= size)
		cout << "Invalid index. Cannot set value to the index given.";
	else
		arr[index] = value;
}

void Vector::push_back(int value)
{
	if(size == capacity)
		expand_capacity();
	arr[size++] = value;
}

void Vector::expand_capacity()
{
	cout << "Expand capacity function has been called!! Size is: " << size << " and capacity is: " << capacity << endl;
	capacity *= 2;
	int *tempArr = new int[capacity];
	for(int i = 0; i < size; i++)
	{
		tempArr[i] = arr[i];
	}
	swap(arr, tempArr);
	delete[] tempArr;
}

void Vector::insert(int index, int value)
{
	if(size == capacity)
		expand_capacity();
	for(int i = size - 1; i >= index; i--)
	{
		arr[i + 1] = arr[i];
	}
	arr[index] = value;
	size++;
}

int Vector::find(int value)
{
	bool found = false;
	int index = 0;
	for(int i = 0; i < size; i++)
	{
		if(arr[i] == value)
		{
			found = true;
			index = i;
		}
	}
	if(found)
		return index;
	return -1;
}

int Vector::pop(int index)
{
	if(index > size)
	{
		cout << "Index is out of range." << endl;
		return -1;
	}
	int value = arr[index];
	for(int i = index; i < size; i++)
		arr[i] = arr[i+1];
	size--;
	return value;
}

void Vector::rotateRight()
{
	// 0 1 2 3 4 5
	// 5 0 1 2 3 4 ------>> size = 6
	
	// Method 1:
	// int temp;
	// temp = arr[size-1];
	// for(int i = size - 1; i > 0; i--)
	// 	arr[i] = arr[i-1];
	// arr[0] = temp;
	
	// Method 2:
	// int *arr2 = new int[size];
	// for(int i = 0; i < size; i++)
	// 	arr2[i+1] = arr[i];
	// arr2[0] = arr[size-1];
	// swap(arr, arr2);

	// Method 3:
	int temp = arr[size-1];
	for(int i = 0; i < size; i++)
		arr[i+1] = arr[i];
	arr[0] = temp;
}

void Vector::rotateRight(int times)
{
	// size = 10, times = 2, rotate = 2
	int rotate = times % size;
	while(times--)
		rotateRight();	
}

void Vector::rotateLeft()
{
	int temp = arr[0];
	for (int i = 0; i < size; i++)
		arr[i] = arr[i + 1];
	arr[size - 1] = temp;
}

void Vector::rotateLeft(int times)
{
	times %= size;
	while(times--)
		rotateLeft();
}

int Vector::find_transposition(int value)
{
	int index = 0;
	for(int i = 0; i < size; i++)
	{
		if(arr[i] == value)
		{
			if(i==0)
				return 0;
			swap(arr[i-1], arr[i]);
			return i - 1;
		}
	}
	cout << "Value not found in the array." << endl;
	return -1;
}

void Vector::printVector()
{
	cout << "Printing values of the array..." << endl;
	for(int i = 0; i < size; i++)
		cout << "Value at index " << i << " is: " << arr[i] << endl;
}