class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        i=0
        j=k
        store=0
        s=sum(nums[:k])
        f=Counter(nums[:k])
        if(len(f)==k):
            store=s
        
        while j<len(nums):
            s=(s+nums[j])-nums[i]

            inval=nums[j]
            f[inval]=f.get(inval, 0)+1
           
            outval=nums[i]
            f[outval]-=1
            if f[outval]==0:
                del f[outval]

            if len(f)==k:
                store=max(store, s)

            i+=1
            j+=1

        return store

