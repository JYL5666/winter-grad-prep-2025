#include <iostream>
using namespace std;

int main() {
    int score{};
    cout << "Enter score (0 - 100): ";
    cin >> score;

    if (!cin) {
        cout << "invalid input (not a number). \n";
        return 0;
    }

    if (score < 0 || score > 100) {
        cout << "Out of range. \n";
    } else if (score >= 90) {
        cout << "A\n";
    } else if (score >= 80)
    {
        cout << "B\n";
    } else if (score >= 70) {
        cout << "C\n";
    } else if (score >= 60) {
        cout << "D\n";
    } else {
        cout << "F\n";
    }
    return 0;
}