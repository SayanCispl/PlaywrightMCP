# Find duplicates in a list

nums = [1, 2, 3, 4, 5, 2, 3, 6, 7, 8, 9, 1]
duplicates = []
for n in nums:
    if nums.count(n)> 1 and n not in duplicates: # The count() method returns the number of times a specified value appears in the list. If the count is greater than 1, it means that the number is a duplicate. Additionally, we check if the number is not already in the duplicates list to avoid adding the same duplicate multiple times.
        duplicates.append(n)
print("Duplicates in the list: ", duplicates)
