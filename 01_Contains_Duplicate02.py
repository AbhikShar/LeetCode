class Solution:
    def hasDuplicate(self, nums) -> bool:
        # creating a hashset to check in O(1)
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
            
        return False
        