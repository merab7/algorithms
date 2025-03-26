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
    48,
    6,
    27,
    85,
    58,
    9,
    39,
    70,
    33,
    81,
    20,
    97,
    11,
    55,
    43,
    66,
    30,
    74,
    21,
    96,
    60,
    19,
    80,
    98,
    4,
    23,
    41,
    90,
    1,
    86,
    5,
    53,
    45,
    68,
    31,
    79,
    15,
    64,
    35,
    99,
    26,
    46,
    7,
    52,
    82,
    16,
    71,
    92,
    40,
    28,
    87,
    13,
    37,
    49,
    93,
    18,
    57,
    10,
    65,
    22,
    78,
    54,
    32,
    47,
    84,
    25,
    76,
    59,
    38,
    94,
    44,
    83,
    63,
    51,
    75,
    61,
    72,
    0,
]


def selection_sort(nums):
    for i in range(len(nums)):
        index_to_move = index_of_min(nums, i)
        nums[i], nums[index_to_move] = nums[index_to_move], nums[i]

    return nums


def index_of_min(nums, start):
    min_index = start
    for i in range(start + 1, len(nums)):
        if nums[i] < nums[min_index]:
            min_index = i
    return min_index


#
#
#
# def selection_sort(nums):
#     sorted_list = []
#     for i in range(0, len(nums)):
#         index_to_move = index_of_min(nums)
#         sorted_list.append(nums.pop(index_to_move))
#     return sorted_list
#
#
# def index_of_min(nums):
#     min_index = 0
#     for i in range(1, len(nums)):
#         if nums[i] < nums[min_index]:
#             min_index = i
#     return min_index
#

print(selection_sort(nums))
