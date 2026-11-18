class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        i=0
        j=10
        store=set()
        res=set()
        n=len(s)
        while j<=n:
            seq=s[i:j]
            if seq not in store:
                store.add(seq)
            else:
                res.add(seq)
            i+=1
            j+=1

        return list(res)