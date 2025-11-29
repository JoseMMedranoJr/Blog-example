# Linear Search
def linear_search_unsorted(arr, target):
    count = 0
    for i in range(len(arr)):
        if arr[i] == target: 
            count += 1
            return f"It took {count} iterations(s) to reach {target}"
    else: 
        count += 1
        return f"{target} is not in the provided area"
    

# Binary Search
def binary_search_unsorted(arr, target):
    sorted_list = sort(unsorted_list)
    count = 0
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2

    if sorted_list[mid] == target:
        

    pass

# Scenario 1 Test
unsorted_list = [42, 15, 7, 30, 22, 10, 18]
target_1 = 30
result_linear_search_1 = linear_search_unsorted(unsorted_list, target_1)
result_binary_search_1 = binary_search_unsorted(sorted(unsorted_list), target_1)
print(f"Scenario 1 (Linear Search): Target {target_1} found at index {result_linear_search_1[0]} in {result_linear_search_1[1]} steps.")
print(f"Scenario 1 (Binary Search): Target {target_1} found at index {result_binary_search_1[0]} in {result_binary_search_1[1]} steps.")