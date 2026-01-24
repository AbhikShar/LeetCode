# Algorithim:
# if the length of s and t are not equal -> they are not anagrams
# create hasmap (key -> char) to keep count of the times each value appears (value -> frequency)
# loop through both strings to store key:value for both hashmaps
# loop through both hashmaps to check for each key if the value is not the same -> not anagram
# else it is a valid anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        
        # hasmap for s and t
        countS = {} # key(char) : value(frequency)
        countT = {} # key(char) : value(frequency)

        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1

        for n in countS:
            if countS[n] != countT.get(n, 0):
                return False
        
        return True