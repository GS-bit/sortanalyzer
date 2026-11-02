"""
Utility functions.
"""

import os


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

def get_key(msg: str) -> str:
    """
    It waits for the user to press any key.

    Arguments:
        msg: a prompt message to the user.

    Return:
        the key pressed.
    """

    print(msg, end="", flush=True)

    # For Windows systems:
    if os.name == "nt":
        import msvcrt

        return msvcrt.getch().decode("utf-8")

    # For Linux/macOS:
    import sys
    import termios
    import tty

    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def get_compact_list(_list: list) -> str:
    """
    It displays the list in a compact format.

    Arguments:
        _list: the list.

    Return:
        a string with the compact representation of the list.
    """

    if len(_list) > 20:
        return f"{_list[:10]} ... {_list[-10:]}"

    return f"{_list}"
    