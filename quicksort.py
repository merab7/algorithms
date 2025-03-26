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


def quicksort(n):

    if len(n) <= 1:
        return n
    less_than_pivot = []
    greater_than_pivot = []
    pivot = n[0]

    for value in n[1:]:
        if value <= pivot:
            less_than_pivot.append(value)
        else:
            greater_than_pivot.append(value)

    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)


sort_numbers = quicksort(nums)
print(sort_numbers)
