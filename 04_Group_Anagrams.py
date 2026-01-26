# Algorithim: O(m*n), m is the num of strings and n is the lenght of the longest string
# 1.) Create a empty hashmap (use defaultdict(list) to ensure uninitialized keys have valyes if acessed).
# 2.) For loop -> iterate through all the strings in the list
# 3.) create a count array with 26 zeros.
# 4.) For loop -> iterate though all the letters in the string.
# 5.) If a letter is encountered increase it's count (in the alphabet array)
# 6.) Store the count array as the "key" of the hashmap and the strings that have it as a list of strings (use tuple as list is not hashable).
# 7.) return a list of the values of the hashmap (the list of strings)

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        
        hashmap = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            hashmap[tuple(count)].append(s)
        
        return list(hashmap.values())