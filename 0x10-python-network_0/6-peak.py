#!/usr/bin/python3
#finds a peak in a list of unsorted integers

def def find_peak(list_of_integers):

    if list_of_integers is None or list_of_integers_len == 0:
        return None
    thePeak = bSearch(list_of_integers, 0, list_of_integers_len - 1)
    return list_of_integers[peak]

def bSearch(a, lo, hi):

    if lo > hi:
        return lo
    mid = (hi - lo) // 2 + lo

    if mid > 0 and a[mid] < a[mid - 1]:
        return bSearch(a, lo, mid - 1)
    elif mid < len(a) - 1 and a[mid] < a[mid +1]:
        return bSearch(a, mid + 1, hi)

    else:
        return mid
