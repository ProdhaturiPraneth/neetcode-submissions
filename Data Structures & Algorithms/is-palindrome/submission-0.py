class Solution:
    def isPalindrome(self, s: str) -> bool:
        n=len(s)
        new_s=''
        for i in range(n):
            if s[i].isalnum():
                new_s=new_s+s[i]
        new_s=new_s.lower()
        n=len(new_s)
        for i in range(n//2):
            if new_s[i]!=new_s[n-i-1]:
                return False
        return True