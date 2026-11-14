class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s=sum(nums[:k])
        i=0
        j=k
        maxx=s
        while j<len(nums):
            s=s+nums[j]-nums[i]
            maxx=max(maxx,s)
            i+=1
            j+=1
        return maxx/k
                



        