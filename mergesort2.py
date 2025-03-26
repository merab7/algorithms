nums = [
    42,
    17,
    89,
    3,
    56,
    24,
    73,
    91,
    8,
    34,
    67,
    29,
    14,
    100,
    2,
    77,
    88,
    50,
    36,
    62,
    95,
    12,
]


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    middle_index = len(arr) // 2
    left_values = merge_sort(arr[:middle_index])
    right_values = merge_sort(arr[middle_index:])

    sorted_values = []

    left_index = 0
    right_index = 0

    while left_index < len(left_values) and right_index < len(right_values):
        if left_values[left_index] < right_values[right_index]:
            sorted_values.append(left_values[left_index])
            left_index += 1
        else:
            sorted_values.append(right_values[right_index])
            right_index += 1
    while left_index < len(left_values):

        sorted_values.append(left_values[left_index])
        left_index += 1

    while right_index < len(right_values):
        sorted_values.append(right_values[right_index])
        right_index += 1

    return sorted_values


print(merge_sort(nums))
