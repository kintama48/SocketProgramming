def is_digit(number):
    try:
        int(number)
        return True
    except ValueError:
        return False


def search_again():
    return input(f"\n"
                 f"          Do you want to calculate        \n"
                 f"          again (Y/N)? : ")


def print_result(result):
    print(f"\n"
          f"    _____________________________________________\n"
          f"   |             Result: {result}                     |\n"
          f"    _____________________________________________\n")


def get_numerical_input():
    while True:
        print("    _____________________________________________")
        a = input("      Please enter first digit `a`: ")
        b = input("      Please enter second digit `b`: ")
        if not is_digit(a) or not is_digit(b):
            print("      ERROR: Please Enter a Valid Integer!")
            continue
        return int(a), int(b)


def get_input():
    input_str = '\n' \
                '    _____________________________________________\n' \
                '   |    1.  Multiply                             |\n' \
                '   |    2.  Subtract                             |\n' \
                '   |    3.  Divide                               |\n' \
                '   |    4.  Add                                  |\n' \
                '    _____________________________________________\n\n' \
                '      Please enter an option between (1-4) or\n' \
                '      "Q" to quit: '
    return input(input_str)
