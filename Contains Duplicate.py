def containsDuplicate(nums):
    master_dict = {}
    for val in nums: # First we will up the dictionary with the list nums. Add a 0 value for now as a placeholder.
        master_dict[val] = 0
    for val in nums: # This one will count how many times each num occurs by checking if it's in the dictionary
        if val in master_dict:
            master_dict[val] += 1
    for val in nums:
        if master_dict[val] >= 2:
            return True
    return False

# First leetcode I solved pretty easily on my own!




containsDuplicate([1, 2, 3, 67, 923, 0, 3])

"""
Optimized code:
def containsDuplicate(nums):
    seen = set()  # Create an empty set
    for num in nums:  # Loop through each number in the list
        if num in seen:  # Check if the number is already in the set
            return True  # If yes, we found a duplicate
        seen.add(num)  # Otherwise, add the number to the set
    return False  # No duplicates found

Why couldn't you just use an empty list instead of a set? You could, but this is optimal bc it is much FASTER.
Remember checking if something belongs in a list is O(n), while using a set is O(1). This method makes it as fast
as possible by making use of the O(1) features of sets. 
 

"""