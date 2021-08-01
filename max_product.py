def max_product(array):
    """This is a function that computes the maximum product of three integers from a given list"""
    if not isinstance(array, list):
        return None
    elif not all(isinstance(element, int) for element in array):
        return None
    else:
        quicksort(array)
        product = array[-1] * array[-2] * array[-3]
        return product


def quicksort(array):
    """This is a function that intializes the recursive call to the quicksort algorithm"""
    recursive_quicksort(array, 0, len(array) - 1)


def recursive_quicksort(array, low_index, high_index):
    """This function sets up the recursive quicksort"""
    if low_index < high_index:
        border_index = partitioner(array, low_index, high_index)
        recursive_quicksort(array, low_index, border_index - 1)
        recursive_quicksort(array, border_index + 1, high_index)


def median_pivot_index(array, low_index, high_index):
    """This functions gets the median value index between the first element, the middle element and the last element from the list"""
    middle_index = (low_index + high_index) // 2
    diff1 = array[low_index] - array[middle_index]
    diff2 = array[middle_index] - array[high_index]
    diff3 = array[low_index] - array[high_index]
    if diff1 * diff2 >= 0:
        return middle_index
    elif diff1 * diff3 > 0:
        return high_index
    else:
        return low_index


def partitioner(array, low_index, high_index):
    """This function implements the quicksort algorithm"""
    pivot_index = median_pivot_index(array, low_index, high_index)
    pivot_element = array[pivot_index]
    array[pivot_index], array[low_index] = array[low_index], array[pivot_index]
    border_index = low_index
    for index in range(low_index, high_index + 1):
        if array[index] < pivot_element:
            border_index = border_index + 1
            array[index], array[border_index] = array[border_index], array[index]
    array[border_index], array[low_index] = array[low_index], array[border_index]
    return border_index
