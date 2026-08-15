class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]
        
        # 1. Count frequencies of each number
        for n in nums:
            count[n] = 1 + count.get(n, 0)
            
        # 2. Populate bucket array (OUTSIDE the first loop)
        for n, c in count.items():
            freq[c].append(n)
            
        # 3. Gather the top k frequent elements from highest frequency to lowest
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res