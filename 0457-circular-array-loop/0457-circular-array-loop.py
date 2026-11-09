class Solution:

  def circularArrayLoop(self, nums: list[int]) -> bool:
    n=len(nums)

    def get_next(i: int) -> int:
      return (i+nums[i])%n

    for i in range(n):
      if nums[i]==0:
        continue

      slow=fast=i
      f=nums[i]>0


      while ((nums[slow]>0)==f and(nums[fast]>0)==f and(nums[get_next(fast)]>0)==f):
        slow=get_next(slow)
        fast=get_next(get_next(fast))

        if slow==fast:

          if slow==get_next(slow):
            break
          return True


      curr=i
      while nums[curr]!=0 and(nums[curr]>0)==f:
        nxt=get_next(curr)
        nums[curr]=0
        curr=nxt

    return False