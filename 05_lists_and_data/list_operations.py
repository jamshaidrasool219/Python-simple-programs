# Program: List ke basic operations
nums = [5, 2, 9, 1, 7]
print("List:", nums)

nums.append(10)
print("Append ke baad:", nums)

nums.remove(2)
print("Remove ke baad:", nums)

nums.sort()
print("Sorted:", nums)

print("Max:", max(nums))
print("Min:", min(nums))
print("Sum:", sum(nums))
print("Average:", sum(nums) / len(nums))
