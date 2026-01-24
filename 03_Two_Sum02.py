# This is a optimal implementation -> O(n)
# Algorithim:
# 1.) Create an empty hashmap to store values you encounter as you go through the loop
# 2.) Loop though nums using enumerate (to get both the value and index)
# 3.) Create a variable diff to store (target - n) i.e. the desired num in the list
# 4.) Check if diff is in hashmap -> O(1)
# 5.) If yes, return the index of diff, and i
# 5.) If no, store the current num in hashmap with its index and move to the next iteration of the loop


class Solution:
    def twoSum(self, nums, target):   
        # create empty hashmap to store previously encountered nums
        prevMap = {} # num (key) : index (value)

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return

