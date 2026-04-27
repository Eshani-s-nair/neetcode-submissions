class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a=[]
        for i,num in enumerate(nums):
            a.append([num,i])
        a.sort()
        left,right=0,len(nums)-1
        while left<right:
            sum=a[left][0]+a[right][0]
            if sum==target:
                return [min(a[left][1],a[right][1]),max(a[left][1],a[right][1])]
            elif sum<target:
                left+=1
            else:
                right-=1
        