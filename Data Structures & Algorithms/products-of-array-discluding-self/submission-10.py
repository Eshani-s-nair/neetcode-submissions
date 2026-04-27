class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[]
        count=0
        for num in nums:
            if num==0:
                count+=1
        if count==len(nums):
            return [0]*count


        for num in range(len(nums)):
            product=1
            for j in range(len(nums)):
                if num!=j:
                    product*=nums[j]
            output.insert(num,product)
        return output

        