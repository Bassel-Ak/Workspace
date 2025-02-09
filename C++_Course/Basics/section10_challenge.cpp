#include <iostream>
#include <string>

using namespace std;

int main()
{
    string secret_message {};
    string alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    string key = "XZNLWEBGJHQDYVTKFUOMPCIASRxznlwebgjhqdyvtkfuompciasr";
    int index = 0;
    cout << "Enter a secret message: ";
    // this is the secret message
    getline(cin,secret_message);
    string encrypted_message {};
    string decrpted_message {};
    for(size_t i = 0; i < secret_message.length(); i++)
    {
        index = alphabet.find(secret_message[i]);
        if(index != string::npos)
            encrypted_message += key[index];
        else
            encrypted_message += secret_message[i];
    }
    cout << "The encrypted message is: " << encrypted_message << endl;
    for(size_t i = 0; i < encrypted_message.length(); i++)
    {
        index = key.find(encrypted_message[i]);
        if(index != string::npos)
            decrpted_message += alphabet[index];
        else
            decrpted_message += encrypted_message[i];
    }
    cout << "The decrypted message is: " << decrpted_message << endl;

    return 0;
}