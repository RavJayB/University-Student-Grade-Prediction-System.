def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def power(a, b):
    return a ** b


def reminder(a, b):
    return a % b


def inputs():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(num1, "+", num2, "=", add(num1, num2))


def select_option():
    while True:
        print("Select operation. "
              "\n1.Add      : + "
              "\n2.Subtract : - "
              "\n3.Multiply : * "
              "\n4.Divide   : / "
              "\n5.power    : ^ "
              "\n6.Remainder: % "
              "\n7.Terminate: # "
              "\n8.Reset    : $ ")

        print()
        choice = input("Enter choice (+ , - , * , / , ^ , % , # , $ ): ")

        if choice in ('+', '-', '*', '/', '^', '%'):

            while True:
                try:

                    num1 = float(input("Enter first number: "))
                    num2 = float(input("Enter second number: "))
                    print()
                    con = input("Terminate: # "
                                "\nReset  : $"
                                "\nproceed  : p"
                                "\n")
                    print()

                    if con == '#':
                        print("Done, Terminating")
                        exit()

                    elif con == '$':
                        select_option()
                        exit()

                    elif con == 'p':
                        if choice == '+':
                            print(num1, "+", num2, "=", add(num1, num2))
                            print()
                            break

                        elif choice == '-':
                            print(num1, "-", num2, "=", subtract(num1, num2))
                            print()
                            break

                        elif choice == '*':
                            print(num1, "*", num2, "=", multiply(num1, num2))
                            print()
                            break

                        elif choice == '/':
                            try:
                                print(num1, "/", num2, "=", divide(num1, num2))
                                print()
                                break

                            except ZeroDivisionError:
                                print("float division by zero "
                                      "\n", num1, " / ", num2, " = 0")
                                print()
                                break

                        elif choice == '^':
                            print(num1, "^", num2, "=", power(num1, num2))
                            print()
                            break

                        elif choice == '%':
                            print(num1, "%", num2, "=", reminder(num1, num2))
                            print()
                            break

                    else:
                        print("Something wrong, Try again..!")
                        print()
                        select_option()
                        exit()

                except ValueError:
                    print("Not valid number,please enter again")
                    print()

        elif choice in '#':
            if choice == '#':
                print("Done, Terminating")
                exit()

        else:
            print("unrecognized operation. ")
            break


select_option()
