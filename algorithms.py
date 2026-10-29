from typing import Any, Callable
import random
import time

def clock(func: Callable[..., Any]) -> Callable[..., None]:
    """
    It runs a sort algorithm with a clock.

    Arguments:
        func: a function that runs the sort algorithm.
    """

    def wrapper(*args: Any, **kwargs: Any) -> None:
         start_time = time.perf_counter()

         func(*args, **kwargs)

         end_time = time.perf_counter()

         total_time = 1000*(end_time - start_time)  # Time in milliseconds.

         if total_time < 1000:
             print(f"[Time taken: {(total_time):.2f}ms]")
         elif total_time < 60000:
             print(f"[Time taken: {(total_time/1000):.2f}s]")
         elif total_time < 3.6e+6:
             print(f"[Time taken: {(total_time/60000):.2f}min]")
         else:
             print(f"[Time taken: {(total_time/3.6e+6):.2f}h]")


    return wrapper

@clock
def bubble_sort(_list: list[int]) -> None:
    """
    It runs bubble sort on an existing list in-place.

    Arguments:
        _list: the list.
    """

    list_size = len(_list)

    has_change = False

    for i in range(list_size-1):
        for j in range(list_size-1-i):
            if _list[j+1] < _list[j]:
                _list[j], _list[j+1] = _list[j+1], _list[j]

                has_change = True

        if not has_change:
            return

@clock
def selection_sort(_list: list[int]) -> None:
    """
    It runs selection sort on an existing list in-place.

    Arguments:
        _list: the list.
    """

    list_size = len(_list)

    for i in range(list_size-1):
        minor = _list[i]
        minor_pos = i

        for j in range(i+1, list_size):
            if _list[j] < minor:
                minor = _list[j]
                minor_pos = j

        _list[i], _list[minor_pos] = _list[minor_pos], _list[i]

@clock
def insertion_sort(_list: list[int]) -> None:
    """
    It runs insertion sort on an existing list in-place.

    Arguments:
        _list: the list.
    """

    list_size = len(_list)

    for i in range(1, list_size):
        j = i
        cur_number = _list[j]

        while j > 0 and _list[j-1] > cur_number:
            _list[j] = _list[j-1]
            j-=1
        _list[j] = cur_number

@clock
def quick_sort(_list: list[int]) -> None:
    """
    It runs quick sort on an existing list in-place.

    Arguments:
        _list: the list.
    """

    def _quick_sort(_list: list[int]) -> list[int]:
        """
        Quick sort internal function.

        Arguments:
            _list: the list to sort.

        Return:
            the passed list sorted.
        """

        if not _list:
            return []
        elif len(_list) <= 1:
            return _list
        else:
            pivot_id = random.randint(0, len(_list)-1)
            pivot = _list[pivot_id]

            lesser_pivot = []
            equal_pivot = []
            greater_pivot = []

            for i in _list:
                if i < pivot:
                    lesser_pivot.append(i)
                elif i == pivot:
                    equal_pivot.append(i)
                else:
                    greater_pivot.append(i)


            new_list = _quick_sort(lesser_pivot) + equal_pivot + _quick_sort(greater_pivot)

            return new_list

    _list[:] = _quick_sort(_list)

@clock
def merge_sort(_list: list[int]) -> None:
    """
    It runs merge sort on an existing list in-place.

    Arguments:
        _list: the list.
    """

    def merge(_list1: list[int], _list2: list[int]) -> list[int]:
        """
        It merges two sorted lists.

        Arguments:
            list1: the first list.
            list2: the second list.

        Return:
            the result of the merge.
        """

        result = []

        i = 0
        j = 0

        while i < len(_list1) and j < len(_list2):
            if _list1[i] < _list2[j]:
                result.append(_list1[i])
                i += 1
            else:
                result.append(_list2[j])
                j += 1

        result.extend(_list1[i:])
        result.extend(_list2[j:])

        return result

    def _merge_sort(_list) -> list[int]:
        """
        Merge sort internal function.

        Arguments:
            _list: the list to sort.

        Return:
            the passed list sorted.
        """

        if _list:
            if not _list or len(_list) <= 1:
                return _list
            else:
                _list_half1 = _list[:len(_list)//2]
                _list_half2 = _list[len(_list)//2:]

                _list_sorted_half1 = _merge_sort(_list_half1)
                _list_sorted_half2 = _merge_sort(_list_half2)

                return merge(_list_sorted_half1, _list_sorted_half2)

    _list[:] = _merge_sort(_list)
