#include <iostream>
#include <cmath>
#include <stdint.h>

using std::cout;
using std::endl;

uint32_t numberOfDivisors(int number) {
    if (number == 0) return 0;
    uint64_t nod = 0;
    uint64_t sr = (uint64_t)sqrt(number);
    for (uint64_t i=1; i <= sr; i++) {
        if (number % i == 0) {
            nod += 2;
        }
    }
    if (sr * sr == number) nod--;
    return nod;
}

int main() {
    uint64_t number = 0;
    uint64_t i = 1;
    while (numberOfDivisors(number) < 500) {
        number += i;
        i++;
        //if (i % 1000 == 0) { cout << "triangle number("<<i<<") is " << number << endl; }
    }
    cout << "number = " << number << endl;
    return 0;
}
