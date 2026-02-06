// 2 dashes without a space next to eachother allows you to write a comment exactly how # makes a comment in Python


#include <iostream> // Need to add any and all capabilities into your code: This includes the ability to get or return (stream) inputs/outputs (io) i nthe code, like printing!
// From the c++ standered library

// Main is the starting place in your code: Only one is defined and all code happens inside it
int main() { // Code that is accessable should happen inside these braces: {} Int just allows the you to know if the code works, as if the # isn't 0, something went wrong.
    double sales = 95000;
    double state_tax = 0.04;
    double county_tax = 0.02;
    double final_sales = (sales - (sales*state_tax) - (sales * county_tax));
    std::cout << "final sales = $" << final_sales <<  "." << std::endl; // std = standered library, cout = Character Out. This line: uses the cout function from the standered library to print "Hello World"
    return 0;
}
