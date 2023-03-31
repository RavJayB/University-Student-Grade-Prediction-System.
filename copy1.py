total_count = 0
progress_out = 0
module_trailer = 0
module_retriever = 0
exclude_out = 0

histogram = {'progress': [], 'trailer': [], 'exclude': [], 'retriever': []}
proval = []
trialval = []
exc_val = []
retval = []

def text_f():
    f = open('test.txt', 'w')  # Write
    p = str(proval)
    t = str(trialval)
    e = str(exc_val)
    r = str(retval)
    pn = p[1:-1]
    tn = t[1:-1]
    rn = r[1:-1]
    en = e[1:-1]

    f.write("prograss                  - ")
    f.write(pn)
    f.write("Progress(module trailer)   -")
    f.write(tn)
    f.write("Module retriever         - ")
    f.write(rn)
    f.write("Exclude                  - ")
    f.write(en)

    f.close()



def repeat_ag():  # Code repeat function
    while True:
        try:
            ask = input("\nWould you like to enter another set of data? "
                        "\nEnter 'y' for yes or 'q' to quit and view results :")
            if ask == "y":
                print()
                stuff()
                break
            elif ask == "q":
                print("quit selected\n")
                hor_histogram()
                ver_histogram()
                list_tu()
                break
            else:
                print("Invalid command")
        except ValueError:
            print("Invalid Entry. Try again! \n")


def list_tu():  # #List function
    p = str(proval)
    t = str(trialval)
    e = str(exc_val)
    r = str(retval)
    print("Progress                 -", p[1:-1])
    print("Progress(module trailer) -", t[1:-1])
    print("Module retriever         -", r[1:-1])
    print("Exclude                  –", e[1:-1])


def hor_histogram():  # Horizontal Histogram generate Function
    print("-" * 60)
    print("    Horizontal Histogram   \n")
    print(f"Progress {progress_out}\t: {'*' * progress_out}")
    print(f"Trailer {module_trailer}\t: {'*' * module_trailer}")
    print(f"Retriever {module_retriever}\t: {'*' * module_retriever}")
    print(f"Excluded {exclude_out}\t: {'*' * exclude_out}\n")
    print(f'{total_count} outcomes in total.')
    print('-' * 60)


# Vertical histogram
def ver_histogram():
    global progress_out, module_trailer, module_retriever, exclude_out

    progress_1 = progress_out
    trailer_1 = module_trailer
    retriever_1 = module_retriever
    exclude_1 = exclude_out

    print("\n    Vertical Histogram    \n")
    print("Progress\t Trailer\t Retriever\t Exclude ")

    max_val = max(progress_1, trailer_1, retriever_1, exclude_1)

    for i in range(max_val):

        if progress_1 > 0:
            print("   *", end="\t\t")
            progress_1 -= 1
        else:
            print("    ", end="\t\t")
        if trailer_1 > 0:
            print("    *", end="\t\t")
            trailer_1 -= 1
        else:
            print("     ", end="\t\t")
        if retriever_1 > 0:
            print("     *", end="\t\t")
            retriever_1 -= 1
        else:
            print("      ", end="\t\t")
        if exclude_1 > 0:
            print("    *")
            exclude_out -= 1
        else:
            print("     ")
    print("-" * 55)


def stuff_ch(value_1, value_2, value_3):
    global progress_out, module_trailer, module_retriever, exclude_out

    if (value_1 == 0 and value_2 <= 40) or (value_1 == 20 and value_2 <= 20) or (value_1 == 40 and value_2 == 0):
        print("Exclude")
        histogram['exclude'] += [value_1, value_2, value_3]
        exc_val.append(value_1)
        exc_val.append(value_2)
        exc_val.append(value_3)
        exclude_out += 1

    elif (value_1 == 0 and value_2 >= 60) or (value_1 == 20 and value_2 >= 40) or (value_1 == 40 and value_2 != 0) or (
            value_1 == 60) or (value_1 == 80):
        print("Do not progress – module retriever")
        histogram['retriever'] += [value_1, value_2, value_3]
        retval.append(value_1)
        retval.append(value_2)
        retval.append(value_3)
        module_retriever += 1

    elif value_1 == 100:
        print("Progress (module trailer) \n")
        histogram['trailer'] += [value_1, value_2, value_3]
        trialval.append(value_1)
        trialval.append(value_2)
        trialval.append(value_3)
        module_trailer += 1

    elif value_1 == 120:
        print("Progress \n")
        histogram['progress'] += [value_1, value_2, value_3]
        proval.append(value_1)  # appending pass,defer,fail values for empty string
        proval.append(value_2)
        proval.append(value_3)
        progress_out += 1

    repeat_ag()


def student_ch1(value_1, value_2):
    global progress_out, module_trailer, module_retriever, exclude_out

    if (value_1 == 0 and value_2 <= 40) or (value_1 == 20 and value_2 <= 20) or (value_1 == 40 and value_2 == 0):
        print("Exclude")
        print("-" * 60, '\n')

    elif (value_1 == 0 and value_2 >= 60) or (value_1 == 20 and value_2 >= 40) or (value_1 == 40 and value_2 != 0) or (
            value_1 == 60) or (value_1 == 80):
        print("Do not progress – module retriever")
        print("-" * 60, '\n')

    elif value_1 == 100:
        print("Progress (module trailer) \n")
        print("-" * 40, '\n')

    elif value_1 == 120:
        print("Progress \n")
        print("-" * 60, '\n')


def u_interface():
    print("-" * 60)
    print("        UNIVERSITY PROGRESSION OUTCOME CHECKER        ")
    print("-" * 60, '\n')
    try:
        print("Please select an option :")
        choose = int(input("Enter 1 - Student version \nEnter 2 - Stuff version with histograms \nEnter 3 - Text file "
                           "\nEnter 4 - Quit\n"))
        if choose == 1:
            print("Student version selected.\n")
            student()
        elif choose == 2:
            print("Stuff version selected.\n")
            stuff()
        elif choose == 3:
            text_f()
            print()
        else:
            print("Quit selected.")
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
                                    student_ch1(pass_credit, defer_credit)
                                    break
                                else:
                                    print("\nTotal incorrect. ")
                                    print("-" * 60)

                            else:
                                print("\nOut of range")
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


def stuff():
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
                                    stuff_ch(pass_credit, defer_credit, fail_credit)
                                    break
                                else:
                                    print("\nTotal incorrect.")
                                    print("-" * 60)

                            else:
                                print("\nOut of range")
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
