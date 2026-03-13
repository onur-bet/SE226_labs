//
// Created by aonur on 13.03.2026.
//

#include "lab3.h"
#include "iostream"
using namespace std;

void printArray(int* arr, int size) {
    cout<<"Array elemets:"<<endl;
    for (int i=0; i<size; i++) {
        cout<<*(arr+i)<< " ";
    }
}



void swapValues(int* p1,int* p2) {
    int temp=*p1;
    *p1=*p2;
    *p2=temp;
}



int findMax(int* arr, int size) {
    int max=*(arr);
    for (int i=1; i<size; i++) {

        if (max<*(arr+i)) {
            max=*(arr+i);
        }
    }
    return max;
}

void reverseArray(int* arr,int size) {
    for (int i=0; i<size/2; i++) {
        int temp=*(arr+i);
        *(arr+i)=*(arr+size-i-1);
        *(arr+size-i-1)=temp;
    }
}

int* createArray(int size) {
    int* arr;
    arr=new int[size];
    return arr;
}

void deleteArray(int* arr) {
    delete[] arr;
}

int main() {
    cout<<"Enter array size:";
    int size;

    cin>>size;

    int* arr;

    arr= new int[size];

    cout<<"Enter values:"<< endl;

    for (int i=0; i<size;i++) {
        cin>>*(arr+i);
    }

    printArray(arr, size);

    reverseArray(arr, size);

    printArray(arr,size);



    return 0;

}













