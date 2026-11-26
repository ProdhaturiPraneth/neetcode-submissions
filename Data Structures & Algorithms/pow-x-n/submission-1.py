class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x==0:
            return 0
        if n==0:
            return 1
        a=abs(n)
        if n<0:
            x=1/x
            if a%2==0:
                return self.myPow(x,a//2)**2
            else: 
                return (x*(self.myPow(x,a//2)**2))

        else:
            if a%2==0:
                return self.myPow(x,a//2)**2
            else: 
                return (x*(self.myPow(x,a//2)**2))