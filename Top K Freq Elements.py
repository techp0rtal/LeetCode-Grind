"""
There's 2 ways I'm thinking of approaching it. 1 is to just take a dictionary, then +=1 to each of the keys as a duplicate
appears. Add it to a list, then take the first k amount of indices from the list.
But I want to try something new. Try using a set to remove duplicates. Then add to the dictionary using that (if it is a
duplicate, add it to the value of the key in the dic). Then make a new set based on k?
We'll try 2 diff approaches
"""

# Here is approach #1. I got this on my own (despite having to lookup how to do max(master_dict, key=master_dict.get)
def topKFrequent(nums, k):
    max_values_list = []
    master_dict = {}
    for val in nums:
        if val in master_dict:
            master_dict[val] += 1
        else:
            master_dict[val] = 1
    #print(master_dict)
    for i in range(k):
        max_val = max(master_dict, key=master_dict.get) # the key=master_dict.get will give us the max VALUE, not max KEY from the dic
        max_values_list.append(max_val)
        master_dict.pop(max_val)

    print(max_values_list)
    return max_values_list



topKFrequent([1, 1, 1, 2, 2, 3], 2)

# This method was really slow though..... I want a better way to do it.
# Approach 2.0 (my approach, but more efficient)/




# mydic = {'a': 1,  'b': 2}
# #print(max(mydic, mydic.get))
# print(max(mydic, key=mydic.get))
#


    # compare_set = set(nums)
    # for counter in nums:
    #     if counter
    #print(compare_set)





# dicts = {7: 2, 8: 34, 2: 10}
#
# nested_dict = {3: {30: 300, 20: 3}, 10: 78, 8:22}
# # print(max(dicts))
# # print(nested_dict[0][3])
# print(max(nested_dict[3]))
# #
# # print(max(nested_dict[0]))
#



"""
Use pop to not just remove the key-value pair, but it also RETURNS the value
vs del which just deletes it.

"""