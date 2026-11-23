class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        i,j=0,0
        store={}
        maxx=0
        while j<len(fruits):
            if fruits[j] not in store and len(store)<2:
                store[fruits[j]]=1
                maxx=max(maxx, j-i+1)
                j+=1
            elif fruits[j] in store:
                store[fruits[j]]+=1
                maxx=max(maxx, j-i+1)
                j+=1
            else:
                store[fruits[i]]-=1
                if store[fruits[i]]==0:
                    del store[fruits[i]]
                i+=1

        return maxx


            
