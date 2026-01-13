#include <iostream>
using namespace std;

int add(int a, int b) {
    return a + b;
}

int square(int c) {
    return c * c;
}

int main() {
    int a = 0;
    int b= 0;

    cout << "Enter 2 intergers: ",
    cin >> a >> b;
    
    int sum = add(a, b);
    int sa = square(a);
    int sb = square(b);
    cout << "sum = " << sum << endl;
    cout << "a^2 = " << sa << endl;
    cout << "b^2 = " << sb << endl;

    return 0;
}