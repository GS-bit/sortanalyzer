"""
This module contains tests of the sorting algorithms implemented in the algorithms.py file.
We use pytest to run the tests.
"""

import random

import algorithms

def test_bubble_sort() -> None:
    """
    It tests the bubble sort algorithm, checking if the lists are sorted correctly.
    """

    list_size = 500

    # Testing random lists:

    _list = [random.randint(1,100*list_size) for i in range(list_size)]
    algorithms.bubble_sort(_list)

    for i in range(len(_list)-1):
        assert _list[i+1] >= _list[i]

    # Testing sorted lists:

    _list = list(range(1,list_size+1))
    algorithms.bubble_sort(_list)

    for i in range(len(_list)-1):
        assert _list[i+1] >= _list[i]

    # Testing sorted lists in reverse order:

    _list = list(range(list_size,0,-1))
    algorithms.bubble_sort(_list)

    for i in range(len(_list)-1):
        assert _list[i+1] >= _list[i]

def test_selection_sort() -> None:
    """
    It tests the selection sort algorithm, checking if the lists are sorted correctly.
    """

    list_size = 500

    # Testing random lists:

    _list = [random.randint(1,100*list_size) for i in range(list_size)]
    algorithms.selection_sort(_list)

    for i in range(len(_list)-1):
        assert _list[i+1] >= _list[i]

    # Testing sorted lists:

    _list = list(range(1,list_size+1))
    algorithms.selection_sort(_list)

    for i in range(len(_list)-1):
        assert _list[i+1] >= _list[i]

    # Testing sorted lists in reverse order:

    _list = list(range(list_size,0,-1))
    algorithms.selection_sort(_list)

    for i in range(len(_list)-1):
        assert _list[i+1] >= _list[i]

def test_insertion_sort() -> None:
    """
    It tests the insertion sort algorithm, checking if the lists are sorted correctly.
    """

    list_size = 500

    # Testing random lists:

    _list = [random.randint(1,100*list_size) for i in range(list_size)]
    algorithms.insertion_sort(_list)

    for i in range(len(_list)-1):
        assert _list[i+1] >= _list[i]

    # Testing sorted lists:

    _list = list(range(1,list_size+1))
    algorithms.insertion_sort(_list)

    for i in range(len(_list)-1):
        assert _list[i+1] >= _list[i]

    # Testing sorted lists in reverse order:

    _list = list(range(list_size,0,-1))
    algorithms.insertion_sort(_list)

    for i in range(len(_list)-1):
        assert _list[i+1] >= _list[i]

def test_quick_sort() -> None:
    """
    It tests the quick sort algorithm, checking if the lists are sorted correctly.
    """

    list_size = 500

    # Testing random lists:

    _list = [random.randint(1,100*list_size) for i in range(list_size)]
    algorithms.quick_sort(_list)

    for i in range(len(_list)-1):
        assert _list[i+1] >= _list[i]

    # Testing sorted lists:

    _list = list(range(1,list_size+1))
    algorithms.quick_sort(_list)

    for i in range(len(_list)-1):
        assert _list[i+1] >= _list[i]

    # Testing sorted lists in reverse order:

    _list = list(range(list_size,0,-1))
    algorithms.quick_sort(_list)

    for i in range(len(_list)-1):
        assert _list[i+1] >= _list[i]

def test_merge_sort() -> None:
    """
    It tests the merge sort algorithm, checking if the lists are sorted correctly.
    """

    list_size = 500

    # Testing random lists:

    _list = [random.randint(1,100*list_size) for i in range(list_size)]
    algorithms.merge_sort(_list)

    for i in range(len(_list)-1):
        assert _list[i+1] >= _list[i]

    # Testing sorted lists:

    _list = list(range(1,list_size+1))
    algorithms.merge_sort(_list)

    for i in range(len(_list)-1):
        assert _list[i+1] >= _list[i]

    # Testing sorted lists in reverse order:

    _list = list(range(list_size,0,-1))
    algorithms.merge_sort(_list)

    for i in range(len(_list)-1):
        assert _list[i+1] >= _list[i]
