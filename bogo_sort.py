import random

# this is bogo_Sort algoryth

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


# # detect when the list is sorted after it randomly being arainged
# def is_sorted(values):
#     for index in range(len(values) - 1):
#         if values[index] > values[index + 1]:
#             return False
#     return True
#
#
# def bogo_sort(values):
#     att = 0
#     while not is_sorted(values):
#         random.shuffle(values)
#         att += 1
#     print(att)
#     return values
#
#
# print(bogo_sort(nums))
