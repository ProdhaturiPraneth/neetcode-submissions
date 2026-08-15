class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            complement=target-nums[i]
            a=nums[i+1:]
            if complement in set(a):
                return [i,a.index(complement)+1+i]
        