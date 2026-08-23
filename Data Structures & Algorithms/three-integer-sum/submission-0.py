class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)
        
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            L, R = i + 1, n - 1
            while L < R:
                summ = nums[i] + nums[L] + nums[R]
                if summ < 0:
                    L += 1
                elif summ > 0:
                    R -= 1
                else:
                    result.append([nums[i], nums[L], nums[R]])
                    L += 1
                    R -= 1
                    # Skip duplicate values for L
                    while L < R and nums[L] == nums[L - 1]:
                        L += 1
                        
        return result