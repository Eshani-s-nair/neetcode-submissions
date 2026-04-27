class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a=[]
        s=[]
        copy=[]
        for i in range(len(strs)):
            copy.append(strs[i])
        for i in range(len(strs)):
            if strs[i] in copy:
                s.append(strs[i])
                copy.remove(strs[i])
            for j in range(i+1,len(strs)):
                if len(strs[i])!=len(strs[j]):
                    continue
                elif sorted(strs[i])==sorted(strs[j]):
                    if strs[j] in copy:
                        s.append(strs[j])
                        copy.remove(strs[j])  
                else:
                    pass
            if s not in a :
                if s !=[]:
                    a.append(s)
                    s=[]
        return a
                    
                    

                
                
        
        