"""
Main program.
"""

import random

import algorithms

from utils import input_option, input_positive_integer

def main() -> None:
    """
    Main function.
    """

    print("=" * 26 + " SortAnalyzer " + "=" * 26)

    print("We are going to generate a list to you!\n")

    list_type = input_option("(1) RANDOM LIST | (2) SORTED LIST | "
        "(3) SORTED LIST (reverse order)\n"
        "Select the type of the list: ", ["1", "2", "3"])

    list_size = input_positive_integer("Type the list size: ")

    _generated_list = []

    match list_type:
        case "1":
            _generated_list = [random.randint(1,100*list_size) for i in range(list_size)]
        case "2":
            _generated_list = list(range(1,list_size+1))
        case "3":
            _generated_list = list(range(list_size,0,-1))
        case _:
            print("Invalid option!")
            return

    print("List generated successfully!")

    _list_to_work = _generated_list[:]  # A copy of the generated list.

    print("\nRunning bubble sort...")
    algorithms.bubble_sort(_list_to_work)
    _list_to_work = _generated_list[:]  # Resetting the list to work to its previous state.

    print("\nRunning selection sort...")
    algorithms.selection_sort(_list_to_work)
    _list_to_work = _generated_list[:]

    print("\nRunning insertion sort...")
    algorithms.insertion_sort(_list_to_work)
    _list_to_work = _generated_list[:]

    print("\nRunning quick sort...")
    algorithms.quick_sort(_list_to_work)
    _list_to_work = _generated_list[:]

    print("\nRunning merge sort...")
    algorithms.merge_sort(_list_to_work)

if __name__ == "__main__":
    main()
