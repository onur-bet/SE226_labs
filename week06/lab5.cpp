//
// Created by aonur on 3.04.2026.
//

#include "lab5.h"
#include <iostream>
using namespace std;

double power(double base , int exp) {
    if (exp==0) {
        return 1;
    }
    else return base*power(base,exp-1);
}
double commonrat( int n, double r) {
    if (n<0){
        return 0;
    }
    else return power(r,n) + commonrat(n-1,r);
}

int main () {
int x;
    int n;
cout<<"Enter number of terms";
cin>>x;
    cout<<"Enter common ratio";
    cin>>n;

    double result =commonrat(x,n);
    cout<<"result=" <<result<<endl;

}
