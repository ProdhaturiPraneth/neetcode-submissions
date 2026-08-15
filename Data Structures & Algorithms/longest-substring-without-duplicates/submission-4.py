class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        else:
            max_len=[1]
        for i in range(len(s)):
            hashset={s[i]}
            count=1
            for j in range(i+1,len(s)):
                if s[j] not in hashset:
                    hashset.add(s[j])
                    count+=1
                else:
                    max_len.append(count)
                    break
                max_len.append(count)
        return max(max_len)