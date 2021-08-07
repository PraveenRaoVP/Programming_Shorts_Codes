// Multi-Ternary operators in JavaScript
// Ternary operators in JS works exactly similar to the ternary operators in C or C++
// The syntax is condition? operation1:operation2
// This can be done multiple times in the same ternary operator
// Eg:
//

const age = 50;

age >=18 ?
    age>=40?
        console.log("Renew your license before driving")
        :console.log("Make sure to renew your license when you turn 40")
    :console.log("You are not eligible to drive")
