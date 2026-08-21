class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0:
            return 0
        #Initialize the longest sequence length
        longest=1
        st=set()
        #Put all array elements in it
        for i in range(n):
            st.add(nums[i])
        #Traverse through the array elements in set to find the longest sequence
        for  it in st:
            #check if 'it' is a starting number of sequence
            if it-1 not in st:
                cnt=1
                #starting element of the sequence
                x=it
                #Find consecutive numbers in the set
                while x+1 in st:
                    #Move to the next element in the sequence
                    x=x+1
                    #Increment the count of the sequence
                    cnt=cnt+1
                #Update the longest sequence length
                longest=max(longest,cnt)
        return longest
