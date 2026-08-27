class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1 or n==2:
            return n
        f=[1,2]
        for i in range(2,n):
            f.append(f[i-1]+f[i-2])
        return f[-1]