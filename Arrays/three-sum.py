"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        def twosum(nums, idx, result):
            idx1, idx2 = idx+1, len(nums)-1
            
            while idx1 < idx2:
                tgt = nums[idx] + nums[idx1] + nums[idx2]
                if tgt == 0:
                    result.append([nums[idx], nums[idx1], nums[idx2]])
                    idx1+=1
                    idx2-=1
                    while nums[idx1-1] == nums[idx1] and idx1 < idx2:
                        idx1+=1
                        
                elif tgt < 0:
                    idx1+=1
                else:
                    idx2-=1
            
            
        result = []
        
        nums = sorted(nums)
        
        for i in range(len(nums)):
            if nums[i] > 0:
                break
                
            if i == 0 or nums[i-1] != nums[i]:
                twosum(nums, i, result)
                
        return result