def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        mid = len(list) // 2
        if list[mid] == target:
            return True
        else:
            if list[mid] < target:
                return recursive_binary_search(list[mid + 1 :], target)
            else:
                return recursive_binary_search(list[:mid], target)


def verify(result):
    print(f"target found: {result}")


numbers = [x for x in range(10000000)]
result = recursive_binary_search(numbers, 500)
verify(result)
