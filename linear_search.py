# linear search
# sequential search
# simple search

# vs

# binary search

# clearly defined problem
# steps should be in very specific order
# steps need to be distinct
# should produced result
# should ocmplite in some time
import time


def linear_search(list, target):
    """
    returns the position of the target if found, else returns None
    """

    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None


def verify(index):
    if index is not (None):
        print(f"Target found at index: {index}")
    else:
        print("Target not found in list")


numbers = [x for x in range(10000000)]
result = linear_search(numbers, 10005)

start_time = time.time()
verify(result)
end_time = time.time()


execution_time = end_time - start_time
print(f"Function took {execution_time:.6f} seconds to execute")
