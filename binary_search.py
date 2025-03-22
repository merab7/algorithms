import time


def binary_search(list, target):

    first, last = 0, len(list) - 1

    while first <= last:
        mid = (first + last) // 2
        if list[mid] == target:
            return mid
        elif list[mid] < target:
            first = mid + 1
        else:
            last = mid - 1

    return None


def verify(index):
    if index is not (None):
        print(f"Target found at index: {index}")
    else:
        print("Target not found in list")


numbers = [x for x in range(10000000)]
result = binary_search(numbers, 10005)

start_time = time.time()
verify(result)
end_time = time.time()


execution_time = end_time - start_time
print(f"Function took {execution_time:.6f} seconds to execute")
