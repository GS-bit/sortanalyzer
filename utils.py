"""
Utility functions.
"""

def input_option(msg: str, options: list[str]) -> str:
    """
    It prompts the user for input until a valid option is given.

    Arguments:
        msg: a prompt message to the user.
        options: a list of available options.

    Return:
        the chosen option.
    """

    chosen_option = ""

    not_valid = True
    while not_valid:
        chosen_option = input(msg)

        if chosen_option in options:
            not_valid = False
        elif chosen_option == "":
            print("Empty input!")
        else:
            print("Invalid option!")

    return chosen_option

def input_positive_integer(msg: str) -> int:
    """
    It prompts the user for input until a positive integer is given.
    
    Arguments:
        msg: a prompt message to the user.

    Return:
        the positive integer.
    """

    user_input = 0

    not_valid = True
    while not_valid:
        user_input = input(msg)

        try:
            user_input = int(user_input)

            if user_input >= 0:
                not_valid = False
            else:
                print("Invalid number!")
        except ValueError:
            if user_input == "":
                print("Empty input!")
            else:
                print("Invalid value!")

    return user_input
