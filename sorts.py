import random
import time

def selection_sort(L):
    # i indicates how many items were sorted
    compar = 0
    for i in range(len(L)-1):
        # To find the minimum value of the unsorted segment
        # We first assume that the first element is the lowest
        min_index = i
        # We then use j to loop through the remaining elements
        for j in range(i+1, len(L)):
            # Update the min_index if the element at j is lower than it
            compar += 1
            if L[j] < L[min_index]:
                min_index = j
        # After finding the lowest item of the unsorted regions, swap with the first unsorted item
        L[i], L[min_index] = L[min_index], L[i]

    return compar


def insertion_sort(arr):
    comps = 0
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            comps += 1
        arr[j + 1] = key

        if key > arr[j]:
            comps += 1
    return comps


def merge_sort(list1):
    if len(list1) > 1:
        mid = len(list1) // 2
        left_half = list1[:mid]
        merge_sort(left_half)
        right_half = list1[mid:]
        merge_sort(right_half)
    return merge(list1, left_half, right_half)


