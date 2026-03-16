#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;


class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> diff;
        vector<int> ans;
        int temp = 0;

        for(size_t i = 0; i<nums.size(); i++){
            temp = target - nums[i];
            if(diff.find(temp)!=diff.end()){
                ans.push_back(i);
                ans.push_back(diff.at(temp));
                return ans;
            }
            diff.insert({nums[i], i});
        }
        return ans;
    }
};