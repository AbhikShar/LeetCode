# Algorithm (optimal approach):
# 1.) Create a hashmap to count the frequency of each value -> value : freq
# 2.) Create a bucket (with the freq as the the index) and store values.
# 3.) Create an empty array and append the values from starting from high freq and going to 1
# 4.) Stop when the length of the array becomes k

class Solution:
    def topKFrequent(self, nums, k):
        # hashmap to store the count of each value
        count = {} # value : freq

        for n in nums:
            count[n] = count.get(n, 0) + 1

        # bucket with freq as indices and the nums as values
        bucket = [[] for i in range(len(nums)+1)]

        for key, value in count.items():
            bucket[value].append(key)

        # create an array and append values fron high freq to low
        res = []
        for i in range(len(bucket)-1, 0, -1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res
            
        
