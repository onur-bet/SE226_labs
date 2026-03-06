//
// Created by aonur on 6.03.2026.
//

#include "lab2.h"

#include <iostream>
#include <string>

using namespace std;

int main() {
    int x;
    int counter = 0;

    cout << "Enter a positive integer greater than 9: ";
    cin >> x;

    cout << x;


    while (x > 9) {
        int sum_digits = 0;
        int temp = x;


        while (temp > 0) {
            sum_digits += temp % 10;
            temp /= 10;
        }


        cout << " -> " << sum_digits;

        x = sum_digits;
        counter++;
    }

    cout << endl;
    cout << "Final value : " << x << endl;
    cout << "Total steps: " << counter << endl;







    int num;
    int fizzCount = 0;
    int buzzCount = 0;
    int fizzBuzzCount = 0;


    cout << "Please enter a number between 10 and 100: ";
    cin >> num;

    while (num < 10 || num > 100) {
        cout << "Invalid input. Please enter a number between 10 and 100: ";
        cin >> num;
    }


    for (int i = 1; i <= num; i++) {

        if (i % 7 == 0) {
            cout << "(" << i << " is skipped)" << endl;
            continue;
        }


        if (i % 3 == 0 && i % 5 == 0) {
            cout << "FizzBuzz" << endl;
            fizzBuzzCount++;
        }

        else if (i % 3 == 0) {
            cout << "Fizz" << endl;
            fizzCount++;
        }

        else if (i % 5 == 0) {
            cout << "Buzz" << endl;
            buzzCount++;
        }

        else {
            cout << i << endl;
        }
    }


    cout << "\n--Summary--" << endl;
    cout << "Fizz count     : " << fizzCount << endl;
    cout << "Buzz count     : " << buzzCount << endl;
    cout << "FizzBuzz count : " << fizzBuzzCount << endl;







    int n;


    cout << "Please enter a number between 3 and 9: ";
    cin >> n;


    if (n >= 3 && n <= 9) {


        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= i; j++) {
                cout << j;
            }
            cout << endl;
        }


        for (int i = n - 1; i >= 1; i--) {
            for (int j = 1; j <= i; j++) {
                cout << j;
            }
            cout << endl;
        }

    } else {
        cout << "Invalid input!" << endl;
    }

    return 0;
}