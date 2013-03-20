#include <iostream>
#include <cmath>
#include <stdint.h>

using std::cout;
using std::endl;

bool is_prime(int number)
{
    if (number == 1) return false;
    if (number == 2) return true;
    if (number == 3) return true;
    if (number == 5) return true;
    if (number == 7) return true;
    if (number % 2 == 0) return false;
    if (number % 3 == 0) return false;
    int k,a,b;
    k = a = b = 1;
    int sr = sqrt(number); 
    while (b < sr) {
        a = (6 * k) - 1;
        b = (6 * k) + 1;
        if (number % a == 0) return false;
        if (number % b == 0) return false;
        k++;
    }
    return true;
}

int main()
{
    uint64_t sum = 0;
    for (int i = 0; i < 2000000; i++) {
        if (is_prime(i)) {
            sum += i;
        }
    }
    cout << "sum = " << sum << endl;
    return 0;
}
