class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        i=0
        j=10
        store=set()
        res=set()
        while j<=len(s):
            if s[i:j] not in store:
                store.add(s[i:j])
            else:
                res.add(s[i:j])
            i+=1
            j+=1

        return list(res)