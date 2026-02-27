//
// Created by aonur on 27.02.2026.
//

#include "myFirstLabScript.h"
#include <iostream>
using namespace std;

int main() {
    string name;
    string studentId;

    cout << "What is your name?" << endl;
    cin >> name;

    cout << "Hello " << name << "." << endl;

    cout << "What is your Student ID?" << endl;
    cin >> studentId;

    cout << "Your ID is " << studentId << "." << endl;

    return 0;
}