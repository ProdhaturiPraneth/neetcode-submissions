class Solution:
    def isHappy(self, n: int) -> bool:
        seen={n}
        while n!=1:
            sum=0
            a=n
            while(a>0):
                sum+=((a%10)**2)
                a=a//10
            n=sum
            if sum in seen and sum!=1:
                return False
            seen.add(sum)

        return True