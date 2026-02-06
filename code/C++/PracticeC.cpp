#include <iostream>
using namespace std;
int main() {
    int a = 1;
    int b = 2;
    int temp = a;
    a = b;
    b = temp;
    double x = 10;
    double y = 5;
    double z = (x+10)/(3*y);
    std::cout << z;
    return 0;
}