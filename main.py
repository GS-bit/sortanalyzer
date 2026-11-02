"""
Main program.
"""

import random

import algorithms

from utils import get_compact_list, get_key, input_option, input_positive_integer

def main() -> None:
    """
    Main function.
    """

    print("=" * 26 + " SortAnalyzer " + "=" * 26)

    print("We are going to generate a list to you!\n")
    print("This list will be sorted through some sorting algorithms, \n"
          "and the time taken by each of them will be shown.")

    print("=" * 26 + "=" * len(" SortAnalyzer ") + "=" * 26)

    print("\n")

    list_type = input_option("(1) RANDOM LIST | (2) SORTED LIST | "
        "(3) SORTED LIST (reverse order)\n"
        "Select the type of the list to generate: ", ["1", "2", "3"])

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

    print("\nList generated successfully!")

    show_generated_list = input_option("Show the generated list? [y/n] ", ["y", "Y", "n"])
    if show_generated_list in ("y", "Y"):
        if len(_generated_list) > 20:
            print(f"Generated list: {_generated_list[:10]} ... {_generated_list[-10:]}")
        else:
            print(f"Generated list: {_generated_list}")

    show_sorted_list = input_option("\nShow the resulting list for each algorithm? [y/n] ",
                                    ["y", "Y", "n"])

    get_key("Type anything to continue...")

    print("")

    _list_to_work = _generated_list[:]  # A copy of the generated list.

    print("\nRunning bubble sort...")
    algorithms.bubble_sort(_list_to_work)

    if show_sorted_list in ("y", "Y"):
        print(f"Resulting list: {get_compact_list(_list_to_work)}")


    _list_to_work = _generated_list[:]  # Resetting the list to work to its previous state.

    print("\nRunning selection sort...")
    algorithms.selection_sort(_list_to_work)

    if show_sorted_list in ("y", "Y"):
        print(f"Resulting list: {get_compact_list(_list_to_work)}")


    _list_to_work = _generated_list[:]

    print("\nRunning insertion sort...")
    algorithms.insertion_sort(_list_to_work)

    if show_sorted_list in ("y", "Y"):
        print(f"Resulting list: {get_compact_list(_list_to_work)}")


    _list_to_work = _generated_list[:]

    print("\nRunning quick sort...")
    algorithms.quick_sort(_list_to_work)

    if show_sorted_list in ("y", "Y"):
        print(f"Resulting list: {get_compact_list(_list_to_work)}")


    _list_to_work = _generated_list[:]

    print("\nRunning merge sort...")
    algorithms.merge_sort(_list_to_work)

    if show_sorted_list in ("y", "Y"):
        print(f"Resulting list: {get_compact_list(_list_to_work)}")

if __name__ == "__main__":
    main()
