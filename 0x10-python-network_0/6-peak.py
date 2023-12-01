#!/usr/bin/python3
# Finds a peak in a list of unsorted integers

def find_peak(list_of_integers):
    #find a peak in list_of_integers"
    if list_of_integers is None or len(list_of_integers) == 0:
        return None
    the_peak = bSearch(list_of_integers, 0, len(list_of_integers) - 1)
    return list_of_integers[the_peak]

def bSearch(a, lo, hi):
    if lo > hi:
        return lo
    mid = (hi - lo) // 2 + lo

    if mid > 0 and a[mid] < a[mid - 1]:
        return bSearch(a, lo, mid - 1)
    elif mid < len(a) - 1 and a[mid] < a[mid + 1]:
        return bSearch(a, mid + 1, hi)
    else:
        return mid
