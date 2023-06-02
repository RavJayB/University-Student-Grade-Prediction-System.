total_count = 0
progress_outcome = 0
module_trailer = 0
module_retriever = 0
exclude = 0


def repeat_ag():
    while True:
        try:
            ask = input("\nWould you like to enter another set of data? "
                        "\nEnter 'y' for yes or 'q' to quit and view results :")
            if ask == "y":
                print()
                run()
                break
            elif ask == "q":
                print("quit selected\n")
                histogram()
                # ver_histogram()
                break
            else:
                print("Invalid command")
        except ValueError:
            print("Invalid Entry. Try again! \n")


def histogram():  # Histogram Generator Function
    print('-' * 60)  # print dashed line 60char's long
    print('Horizontal Histogram')
    print(f"progress {progress_outcome}\t: {'*' * progress_outcome}")
    print(f"Trailer {module_trailer}\t: {'*' * module_trailer}")
    print(f"Retriever {module_retriever}\t: {'*' * module_retriever}")
    print(f"Excluded {exclude}\t: {'*' * exclude}\n")
    print(f'{total_count} outcomes in total.')
    print('-' * 60)  # print dashed line 60char's long


def mark_ch(value_1, value_2, value_3):
    global progress_outcome, module_trailer, module_retriever, exclude

    if (value_1 == 120) & (value_2 == 0) & (value_3 == 0):
        print("Progress \n")
        progress_outcome += 1

    elif value_1 == 100:
        if (value_2 == 20) & (value_3 == 0) | (value_2 == 0) & (value_3 == 20):
            print("Progress (module trailer) \n")
            module_trailer += 1

    elif value_1 == 80:
        if (value_2 == 40) & (value_3 == 0) | (value_2 == 0) & (value_3 == 40) | (value_2 == 20) & (value_3 == 20):
            print("Do not Progress – module retriever")
            module_retriever += 1

    elif value_1 == 60:
        if (value_2 == 60) & (value_3 == 0) | (value_2 == 0) & (value_3 == 60) | (value_2 == 20) & (value_3 == 40) | \
                (value_2 == 40) & (value_3 == 20):
            print("Do not progress – module retriever")
            module_retriever += 1

    elif value_1 == 40:
        if (value_2 == 0) & (value_3 == 80):
            print("Exclude")
            exclude += 1

        elif (value_2 == 80) & (value_3 == 0) | (value_2 == 60) & (value_3 == 20) | \
                (value_2 == 20) & (value_3 == 60) | (value_2 == 40) & (value_3 == 40):
            print("Do not progress – module retriever")
            module_retriever += 1

    elif value_1 == 20:
        if (value_2 == 20) & (value_3 == 80) | (value_2 == 0) & (value_3 == 100):
            print("Exclude")
            exclude += 1

        elif (value_2 == 100) & (value_3 == 0) | (value_2 == 80) & (value_3 == 20) | \
                (value_2 == 60) & (value_3 == 40) | (value_2 == 40) & (value_3 == 60):
            print("Do not progress – module retriever")
            module_retriever += 1

    elif value_1 == 0:
        if (value_2 == 0) & (value_3 == 120) | (value_2 == 20) & (value_3 == 100) | (value_2 == 40) & (value_3 == 80):
            print("Exclude")
            exclude += 1

        elif (value_2 == 60) & (value_3 == 60) | (value_2 == 80) & (value_3 == 40) | \
                (value_2 == 100) & (value_3 == 20) | (value_2 == 120) & (value_3 == 0):
            print("Do not progress – module retriever")
            module_retriever += 1

    repeat_ag()


def u_interface():
    print("-" * 60)
    print("        UNIVERSITY PROGRESSION OUTCOME CHECKER         ")
    print("-" * 60, '\n')
    try:
        choose = int(input("[01] Student version \n[02] Stuff version with histograms \n[03] Text file \n"))
        if choose == 1:
            print("Student version selected.\n")
            run()
    except ValueError:
        print("Invalid Entry!.")


def student():
    while True:
        try:
            global total_count
            credits_x = (0, 20, 40, 60, 80, 100, 120)
            pass_credit = int(input("Please enter your credit at pass  :"))
            if pass_credit in credits_x:
                try:
                    defer_credit = int(input("Please enter your credit at defer :"))
                    if defer_credit in credits_x:
                        try:
                            fail_credit = int(input("Please enter your credit at fail  :"))
                            if fail_credit in credits_x:

                                if pass_credit + defer_credit + fail_credit == 120:
                                    total_count += 1
                                    mark_ch(pass_credit, defer_credit, fail_credit)
                                    break
                                else:
                                    print("\nTotal incorrect. Recheck and try again!")
                                    print("-" * 60)

                            else:
                                print("\nTotal is incorrect. Recheck and try again!")
                                print("-" * 60)
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


def run():
    while True:
        try:
            global total_count
            credits_x = (0, 20, 40, 60, 80, 100, 120)
            pass_credit = int(input("Please enter your credit at pass  :"))
            if pass_credit in credits_x:
                try:
                    defer_credit = int(input("Please enter your credit at defer :"))
                    if defer_credit in credits_x:
                        try:
                            fail_credit = int(input("Please enter your credit at fail  :"))
                            if fail_credit in credits_x:

                                if pass_credit + defer_credit + fail_credit == 120:
                                    total_count += 1
                                    mark_ch(pass_credit, defer_credit, fail_credit)
                                    break
                                else:
                                    print("\nTotal incorrect. Recheck and try again!")
                                    print("-" * 60)

                            else:
                                print("\nTotal is incorrect. Recheck and try again!")
                                print("-" * 60)
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


u_interface()
