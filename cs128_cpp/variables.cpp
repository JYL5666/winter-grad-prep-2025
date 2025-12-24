#include <iostream>
#include <string>
using namespace std;

int main () {
    int age = 0;
    double gpa = 4.0;
    string name = "Junyi";
    
    cout << "Name: " << name << endl;
    cout << "GPA: " << gpa << endl;

    cout << "Enter your age:";
    cin >> age;

    if (age < 0) {
        cout << "invalid age";
        return 0;
    }

    int NextYearAge = age + 1;
    cout << "You are " << age << " years old now." << endl;
    cout << "Next year, you are " << NextYearAge << " years old." << endl;
    
    return 0;
}