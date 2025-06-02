

num1 = input("Enter your first number: ")
sign = input("Enter your mathmatical sign here: ")
num2 = input("Enter your second number: ")

if sign == "+":
    try:
        sum_result = int(num1) + int(num2)
        print(f"{num1} + {num2} = ", sum_result)
    except ValueError:
        print("Invalid input you twat.")
elif sign == "-":
    try:
        minus_res = int(num1) - int(num2)
        print(f"{num1} - {num2} = ", minus_res)
    except ValueError:
        print("Invalid input, seems like user error to me.")
elif sign == "*":
    try:
        times_res = int(num1) * int(num2)
        print(f"{num1} * {num2} = ", times_res)
    except ValueError:
        print("Bruh how do you fuck this up. Invalid Input...")
elif sign == "/":
    try:
        div_res = int(num1) / int(num2)
        print(f"{num1} / {num2} = ", div_res)
    except ValueError:
        print("Ok division is kind hard.. but try to enter a number next time")
else:
    print("Your sign isn't: +, -, * or / come on, its basic math.")