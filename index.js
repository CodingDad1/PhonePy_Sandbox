const input = require('readline-sync');
console.log("The Code is Running");
let num1 = parseFloat(input.question("Enter your first number: "));
let sign = input.question("+,-, *, /?: ");
let num2 = parseFloat(input.question("Enter your second number: "));

if (sign == "+") {
    console.log(`${num1} + ${num2} = ${num1 + num2}`);
} else if(sign == '-') {
    console.log(`${num1} - ${num2} = ${num1 - num2}`);
} else if (sign == "*") {
    console.log(`${num1} * ${num2} = ${num1 * num2}`)
} else if (sign == "/") {
    if (num2 == 0){
        console.log("You know how diving works right?")
    }else {
        console.log(`${num1} / ${num2} = ${num1 / num2}`)
    }
} else {
    console.log("invalid operator, try using a math sign next time instead of that garbage.")
}


/*console.log("Start");
throw new Error("This is a test error.");
console.log("end")
console.log("End"); */