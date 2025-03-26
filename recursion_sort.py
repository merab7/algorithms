nums = [1, 2, 3, 4, 5]


def sum_func(nums):

    if not nums:
        return 0

    remaining_sum = sum_func(nums[1:])
    return nums[0] + remaining_sum


print(sum_func(nums))
