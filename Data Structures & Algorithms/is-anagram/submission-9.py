class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)==len(t):
            count={}
            for i in s:
                if i in count:
                    count[i]+=1
                else:
                    count[i]=1
            for j in count:
                if j in t:
                    if count[j]==t.count(j):
                        continue
                    else:
                        return False
                else:
                    return False
                
            return True
        return False

        