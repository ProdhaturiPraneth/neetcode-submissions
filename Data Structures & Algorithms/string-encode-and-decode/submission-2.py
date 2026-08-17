class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str=[]
        for string in strs:
            encoded_str.append(str(len(string))+'#')
            encoded_str.append(string)
        return "".join(encoded_str)
    def decode(self, s: str) -> List[str]:
        decoded_strs=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!='#':
                j+=1
            length=int(s[i:j])
            i=j+1
            decoded_strs.append(s[i:i+length])
            i+=length
        return decoded_strs