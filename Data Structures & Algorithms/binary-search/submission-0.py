class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        left=0
        right=n-1
        
        while left<=right:
            middle=(left+right)//2
            if nums[middle]==target:
                return middle
            elif target<nums[middle]:
                right=middle-1
            elif target>nums[middle]:
                left=middle+1
        return -1