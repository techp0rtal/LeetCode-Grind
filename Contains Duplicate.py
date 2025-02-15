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