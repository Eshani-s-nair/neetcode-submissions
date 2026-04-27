class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        count=0
        freq=[]
        if len(nums)==0:
            return 0
        for i in range(len(nums)):
            if i+1<len(nums) and nums[i]+1==nums[i+1]:
                count+=1   
            elif i+1<len(nums) and nums[i]==nums[i+1]:
                pass
            else:
                freq.append(count+1)
                count=0
        return max(freq) 
