class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num=0
        n=len(digits)-1
        i=0
        while(i<=n):
            num+=digits[i]
            num*=10
            i+=1
        num=num//10
        num+=1
        sol=list()
        while num>0:
            sol.insert(0,num%10)
            num=num//10
        return sol