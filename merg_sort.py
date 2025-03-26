def merge_sort(list):
    """
    Sorts a list in scending order
    Returns a new sorted list
    Devide: Find the midpoint of the list and divide into sublists
    Conquer: Recursivelu sort the sublists created in previous step
    Combain: Merg the sorted sublists created in previous step
    takes O(n log n)
    """

    if len(list) <= 1:
        return list

    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(list):
    """
    Devides lists into sublists in the mid point
    returns two sublists - left and right
    takes overall O(log n) time
    """
    mid = len(list) // 2
    left = list[:mid]
    right = list[mid:]

    return left, right


def merge(left, right):
    """
    Merges two lists or arrays, sorting them in the porcess
    Returns a new merged sorted list
    runs in overall O(n) time
    """

    new_list = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            new_list.append(left[i])
            i += 1
        else:
            new_list.append(right[j])
            j += 1

    while i < len(left):
        new_list.append(left[i])
        i += 1

    while j < len(right):
        new_list.append(right[j])
        j += 1

    return new_list


#
#
unsorted_list = [9, 5, 10, 99, 3, 1, 5, 25, 100, 10000, 0, -1]
sorted_list = merge_sort(unsorted_list)
print(sorted_list)
#
#
# def verify_sorted(list):
#     n = len(list)
#     if n == 0 or n == 1:
#         return True
#
#     return list[0] <= list[1] and verify_sorted(list[1:])
#
#
# print(verify_sorted(unsorted_list))
# print(verify_sorted(sorted_list))
#

# Corrected alphabet list
# alpha = [
#     "a",
#     "b",
#     "c",
#     "d",
#     "e",
#     "f",
#     "g",
#     "h",
#     "i",
#     "j",
#     "k",
#     "l",
#     "m",
#     "n",
#     "o",
#     "p",
#     "q",
#     "r",
#     "s",
#     "t",
#     "u",
#     "v",
#     "w",
#     "x",
#     "y",
#     "z",
# ]

# # Print length to verify correctness
# print(len(alpha))  # Should print 26
#
# # Create a hash map to store letter indices
# h_map = {alpha[x]: x for x in range(26)}
# print(h_map)
#
# # Given word
# word = "rrtkjsdglssadf"
#
# # Sorting the word based on the custom order from h_map
# sorted_word = "".join(sorted(word, key=lambda ch: h_map[ch]))
#
# # Print results
# print("Original:", word)
# print("Sorted:", sorted_word)
