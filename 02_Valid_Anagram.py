# This solution is brute force
# O(mLogm + nLogn) where m and are the respective sizes of s and t

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sort str s and t
        sorted_s = "".join(sorted(s))
        sorted_t = "".join(sorted(t))

        if sorted_s == sorted_t:
            return True
        else:
            return False

