# Program: Binary search (list sorted honi chahiye)
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


nums = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = int(input("Kya dhoondna hai? "))

idx = binary_search(nums, target)
if idx == -1:
    print("Number nahi mila")
else:
    print("Number index", idx, "par mila")
