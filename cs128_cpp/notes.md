# CS128 — cpp Notes
Winter prep starts on 12/21. This folder warms up C++ fundamentals for CS 128

# Variables

## Key points from LearnCpp
- 1) In C++, we use objects to access memory. A named object is called a variable. Each variable has an identifier, a type, and a value (and some other attributes that aren’t relevant here). A variable’s type is used to determine how the value in memory should be interpreted.
- 2) Variables are actually created at runtime, when memory is allocated for their use.

## Program: variables.cpp
### What the program does
- Reads an integer (age)
- Prints next year age
- Demonstrates int/double/string output

### Run log (paste terminal output)
#### Run 1 (normal input)
Input: 19
Output: 
Name: Junyi
GPA: 4
Enter your age:19
You are 19 years old now.
Next year, you are 20 years old.

#### Run 2 (edge input)
Input:-1
Output:
Name: Junyi
GPA: 4
Enter your age:-1
invalid age

## Common pitfalls (at least 2)
- 1) Mixing up stream operators: output uses 'cout << ...', input uses 'cin >>...'
- 2) Missing spaces/newlines in output