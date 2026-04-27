class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    flag=0
                    if nums[i]+nums[j]+nums[k]==0:
                        for elem in output:
                            x=set(elem)
                            if x==set([nums[i],nums[j],nums[k]]):
                                flag=1
                                continue
                        if flag==0:
                            output.append([nums[i],nums[j],nums[k]])
                        
        return output
        