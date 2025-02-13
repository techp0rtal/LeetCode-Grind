
# This is my first attempt. Aka the "bubble sort" type method.
# Not efficient to say the least, but it was my first attempt.
# My logic can be broken down into these steps:
# 1. Pick the first item from the list/array.
# 2. Save its index somewhere
# 3. Start looping through the array and checking the next item's value.
#       If we only need two numbers to sum to the target, then basic arithmetic tells us that
#       the target - value 1 = value 2.
#       So we continue looping through the array and ask if target - the first item = second item.
# 4. if target - the first item = second item, then we know that is the answer so we save that index.
# 6. Then we simply add index 1 and index 2 to a list, and return that list as the final answer
# 7. If we have gone through all the values and that if statement is not triggered, then the first value is clearly not
#        one of them. So we move on to the next value, and make THAT the first value (and save the new index for it)
# 8. Rinse and repeat until eventually we get a match
"""
def twoSum(nums, target):

    final_answer = []
    for first_value in nums:
        first_index = nums.index(first_value)
        for second_value in nums:
            second_index = nums.index(second_value)
            if target - first_value == second_value:
                final_answer.extend([first_index, second_index])
            if len(final_answer) >= 2:
                return final_answer


print(twoSum([2,7,11,15], 9))
"""
# ChatGPT said the following:
# .index(value) always returns the first occurrence of a number, causing incorrect index lookups.
# You're not checking first_index != second_index, meaning it includes duplicate pairs in different orders.
# This works fine when numbers are unique.
# ❌ But if you have duplicates ([3, 3, 4]), nums.index(3) will always return 0, never 1.
#
# 📌 Fix: Use enumerate(nums) to track both the index and the value properly.
# Also I had the return final_answer outside of the loop, which was a mistake bc I got duplicate additions

#Version 1.1 -- fixes the issues I had that Chat GPT pointed out.
# This design is different because of several reasons:
# 1. it doesn't save the variables anywhere, it just uses the memory of the loop

def twoSum(nums, target):
    for first_index, first_value in enumerate(nums):  # Correct indexing
        for second_index, second_value in enumerate(nums):
            if first_index != second_index and first_value + second_value == target:
                return [first_index, second_index]  #  Correct indices!

# print(twoSum([3, 3, 4], 6))  # Output: [0, 1]

# Version 2.0 - an entirely different method that uses a hash table (dictionary).
# My attempt

# def twoSum(nums, target):
#     master_dic = {}
#     answer = []
#
#     for value in nums:
#         complement = target - value
#         master_dic[value] = nums.index(value)
#         if complement in master_dic:
#             answer.extend([nums.index(value), nums.index(complement)])
#             print(answer)
#             return answer
# twoSum([0, 23, 45, 100, 23, 5, 44], 67)
#

# Version 2.1 (corrected by ChatGPT)
# My issue with the last one was the BLOODY INDEX METHOD. That thing is useless for finding more than 1 index.
# Just use enumerate for loops now and for always and be done with it. Never again.

# def twoSum(nums, target):
#     master_dic = {}
#     for value, index in enumerate(nums):
#         compliment = target - value
#         master_dic[value] = index
#         if compliment in nums:
#             return master_dic[index], compliment[index]


#
def twoSum(nums, target):
    master_dic = {}  # Dictionary for quick lookups

    for index, value in enumerate(nums):  # Use enumerate() to track index
        complement = target - value
        if complement in master_dic:  # Check first before adding to dict
            return [master_dic[complement], index]  #  Return correct indices
        master_dic[value] = index  #  Store the value and index AFTER checking

print(twoSum([3, 3, 4], 6))  #  Output: [0, 1]


# Alternate way a youtuber did it. This is the manual way of using the enumerate function by using range(len(nums)).
# ("The first loop stores all values and their indices in a dictionary. The second loop checks for complements and "
#  "ensures they are not the same index before returning the answer.")
# he('s basically using the range function to create indexes from the nums list, and then just taking the value of i '
#   'directly from nums, and then adding both to the empty dictioanry?)
# range(len(nums)) generates numbers from 0 to len(nums) - 1 (i.e., all valid indices).
# i takes on each of these index values during the loop.
# nums[i] retrieves the actual number at that index.

# def twoSum(nums, target):
#     h = {}
#     for i in range(len(nums)):
#         h[nums[i]] = i
#     for i in range(len(nums)):
#         y = target - nums[i]
#         if y in h and h[y] != i:
#             return [i, h[y]]
