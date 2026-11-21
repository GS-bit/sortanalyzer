"""
This module contains tests of the sorting algorithms implemented in the algorithms.py file.
We use pytest to run the tests.
"""

import random
from typing import Callable

import pytest

import algorithms


@pytest.fixture
def sample_lists() -> list[list[int]]:
    """
    It provides random, sorted and reverse-sorted sample lists for sorting tests.

    Return:
        a list of the lists used for sorting tests.
    """

    list_size = 500

    lists = [
        [random.randint(1, 100 * list_size) for _ in range(list_size)],  # Random list
        list(range(1, list_size + 1)),  # Sorted list
        list(range(list_size, 0, -1)),  # Sorted list (reverse order)
    ]

    return lists


@pytest.mark.parametrize(
    "sorting_algorithm",
    [
        algorithms.bubble_sort,
        algorithms.selection_sort,
        algorithms.insertion_sort,
        algorithms.quick_sort,
        algorithms.merge_sort,
        algorithms.heap_sort
    ],
)
def test_algorithms(
    sorting_algorithm: Callable[[list[int]], str], sample_lists: list[list[int]]
) -> None:
    """
    It tests the sorting algorithms, checking if the lists are sorted correctly.

    Arguments:
        sorting_algorithm: sorting function.
        sample_lists: the sample lists.
    """

    for original_list in sample_lists:
        expected = sorted(original_list)

        candidate = original_list[:]
        sorting_algorithm(candidate)

        assert candidate == expected
