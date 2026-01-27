# Algorithm (brute force approach):
# 1.) Create a hashmap to store frequency of each value -> value : freq
# 2.) Sort the freq in ascending order
# 3.) Return the top k values

class Solution:
    def topKFrequent(self, nums, k):
        # hashmap to store freq
        count = {} # value : count

        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        # store in arr and sort
        arr = []
        for key, value in count.items():
            arr.append([value, key])
        
        arr.sort()

        # return the top k values
        res = []
        while len(res)<k:
            res.append(arr.pop()[1])
        
        return res

