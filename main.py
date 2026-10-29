import random

import algorithms

def main() -> None:
    """
    Main function.
    """

    print("================ SortAnalyzer ===============")

    print("We are going to generate a random list to you!")

    list_size = int(input("Type the list size: "))

    _generated_list = [random.randint(1,100*list_size) for i in range(list_size)]
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
