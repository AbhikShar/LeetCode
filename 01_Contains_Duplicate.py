class Solution:
    def hasDuplicate(self, nums) -> bool:
        # creating a hasmap to check in O(1)
        prevMap = {} # Value : index

        for i, n in enumerate(nums):
            if n in prevMap:
                return True
            prevMap[n] = i
        return False