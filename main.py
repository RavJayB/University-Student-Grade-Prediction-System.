def repeat():
    while True:
        try:
            ask = input("\nWould you like to enter another set of data? "
                        "\nEnter 'y' for yes or 'q' to quit and view results :")
            if ask == "y":
                print()
                run()
                break
            elif ask == "n":
                print("quit selected\n")
                break
            else:
                print("Invalid command")
        except ValueError:
            print("Invalid Entry. Try again! \n")


def mark(value_1, value_2, value_3):
    if (value_1 == 120) & (value_2 == 0) & (value_3 == 0):
        print("Progress \n")

    elif value_1 == 100:
        if (value_2 == 20) & (value_3 == 0) | (value_2 == 0) & (value_3 == 20):
            print("Progress (module trailer) \n")

    elif value_1 == 80:
        if (value_2 == 40) & (value_3 == 0) | (value_2 == 0) & (value_3 == 40) | (value_2 == 20) & (value_3 == 20):
            print("Do not Progress – module retriever")

    elif value_1 == 60:
        if (value_2 == 60) & (value_3 == 0) | (value_2 == 0) & (value_3 == 60) | (value_2 == 20) & (value_3 == 40) | \
                (value_2 == 40) & (value_3 == 20):
            print("Do not progress – module retriever")

    elif value_1 == 40:
        if (value_2 == 0) & (value_3 == 80):
            print("Exclude")

        elif (value_2 == 80) & (value_3 == 0) | (value_2 == 60) & (value_3 == 20) |\
                (value_2 == 20) & (value_3 == 60) | (value_2 == 40) & (value_3 == 40):
            print("Do not progress – module retriever")

    elif value_1 == 20:
        if (value_2 == 20) & (value_3 == 80) | (value_2 == 0) & (value_3 == 100):
            print("Exclude")

        elif (value_2 == 100) & (value_3 == 0) | (value_2 == 80) & (value_3 == 20) | \
                (value_2 == 60) & (value_3 == 40) | (value_2 == 40) & (value_3 == 60):
            print("Do not progress – module retriever")

    elif value_1 == 0:
        if (value_2 == 0) & (value_3 == 120) | (value_2 == 20) & (value_3 == 100) | (value_2 == 40) & (value_3 == 80):
            print("Exclude")

        elif (value_2 == 60) & (value_3 == 60) | (value_2 == 80) & (value_3 == 40) | \
                (value_2 == 100) & (value_3 == 20) | (value_2 == 120) & (value_3 == 0):
            print("Do not progress – module retriever")
    repeat()


def run():
    while True:
        try:
            pass_credit = int(input("Please enter your credit at pass  :"))
            if (pass_credit == 0) | (pass_credit == 20) | (pass_credit == 40) | (pass_credit == 60) | (
                    pass_credit == 80) | (
                    pass_credit == 100) | (pass_credit == 120):
                try:
                    defer_credit = int(input("Please enter your credit at defer :"))
                    if (defer_credit == 0) | (defer_credit == 20) | (defer_credit == 40) | (defer_credit == 60) | (
                            defer_credit == 80) | (
                            defer_credit == 100) | (defer_credit == 120):
                        try:
                            fail_credit = int(input("Please enter your credit at fail  :"))
                            if (fail_credit == 0) | (fail_credit == 20) | (fail_credit == 40) | (fail_credit == 60) | (
                                    fail_credit == 80) | (
                                    fail_credit == 100) | (fail_credit == 120):
                                if pass_credit + defer_credit + fail_credit == 120:
                                    mark(pass_credit, defer_credit, fail_credit)
                                else:
                                    print("\nTotal incorrect. Recheck and try again!")
                                    print("-" * 600)
                            else:
                                print("\nTotal is incorrect. Recheck and try again!")
                                print("-" * 600)
                        except:
                            print("Integer required \n")
                    else:
                        print("Out of range \n")
                except:
                    print("Integer required \n")
            else:
                print("Out of range \n")

        except ValueError:
            print("Integer required. Try again! \n")
            run()


run()
