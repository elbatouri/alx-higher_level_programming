#!/usr/bin/python3
""" Finds a peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """find a peak in list_of_integers"""
    
    if list_of_integers is None or len(list_of_integers) == 0:
        return None
    the_peak = binary_search(list_of_integers, 0, len(list_of_integers) - 1)
    return list_of_integers[the_peak]

def binary_search(a, lo, hi):
    if lo > hi:
        return lo
    mid = (hi - lo) // 2 + lo

    if mid > 0 and a[mid] < a[mid - 1]:
        return binary_search(a, lo, mid - 1)
    elif mid < len(a) - 1 and a[mid] < a[mid + 1]:
        return binary_search(a, mid + 1, hi)
    else:
        return mid
