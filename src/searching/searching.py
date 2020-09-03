def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
        
    return -1


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    new_arr = sorted(arr)
    start = 0
    end = len(new_arr) - 1
    while end >= start:
        middle_index = (start + end) // 2
        middle_value = new_arr[middle_index]

        if target == middle_value:
            return middle_index
        if target > middle_value:
            start = middle_index + 1
            if target == middle_value:
                return start
        if target < middle_value:
            end = middle_index - 1
            if target == middle_value:
                return end



    return -1  # not found
