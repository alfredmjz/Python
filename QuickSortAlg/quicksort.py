def partition(unsorted, leftIndex, rightIndex):
    """
    This function sorts a sub-array of integers and returns the pivot index of the sorted array.

    >>> partition([2,9,5,4], 2, 4)
    0
    """

    pivot = unsorted[rightIndex]
    toSwap = leftIndex - 1
    for i in range(leftIndex, rightIndex):
        if unsorted[i] <= pivot:
            # swap position
            toSwap += 1
            unsorted[toSwap], unsorted[i] = unsorted[i], unsorted[toSwap]

    toSwap += 1
    index = unsorted.index(pivot)
    unsorted[toSwap], unsorted[index] = unsorted[index], unsorted[toSwap]
    return toSwap


def quicksort(unsorted, leftIndex, rightIndex):

    if(leftIndex >= rightIndex):
        return unsorted
    pivotIndex = partition(unsorted, leftIndex, rightIndex)
    quicksort(unsorted, leftIndex, pivotIndex - 1)
    quicksort(unsorted, pivotIndex + 1, rightIndex)
