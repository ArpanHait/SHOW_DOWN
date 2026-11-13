class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        size=float('inf')
        s=0
        i,j=0,0
        while j<len(nums):
            s+=nums[j]
            
            while s>=target:
                size=min(size, j-i+1)
                s-=nums[i]
                i+=1
                
            j+=1
            
        return 0 if size==float('inf') else size