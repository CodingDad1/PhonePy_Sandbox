while True:
    # inputs for 1st number operator and 2nd number
    num1 = input("Enter your first number: ")
    sign = input("Enter your mathmatical sign here: ")
    num2 = input("Enter your second number: ")

# math +
    if sign == "+":
        try:
            sum_result = float(num1) + float(num2)
            print(f"{num1} + {num2} = ", sum_result)
        except ValueError:
            print("Invalid input you twat.")

    # math -
    elif sign == "-":
        try:
            minus_res = float(num1) - float(num2)
            print(f"{num1} - {num2} = ", minus_res)
        except ValueError:
            print("Invalid input, seems like user error to me.")

    # math *
    elif sign == "*":
        try:
            times_res = float(num1) * float(num2)
            print(f"{num1} * {num2} = ", times_res)
        except ValueError:
            print("Bruh how do you fuck this up. Invalid Input...")

    # math / and last else statement for anything but numbers
    elif sign == "/":
        try:
            div_res = float(num1) / float(num2)
            print(f"{num1} / {num2} = ", div_res)
        except ValueError:
            print("Ok division is kind hard.. but try to enter a number next time")
    else:
        print("Your sign isn't: +, -, * or / come on, its basic math.")

#User choice to restart function/Calculator
    cont = input("Continue with another equation? (y/n): ").strip().lower()
    if cont != "y":
        print("Until the next session, Until the next equation, the calculator sleeps....")
        break
