class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str="#"
        for s in strs:
            length=len(s)
            encoded_str+=str(length)
            encoded_str+="#"
            for i in s:
                encoded_str+=i
        return encoded_str
    

    def decode(self, s: str) -> List[str]:
        res=[]
        i = 1
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            res.append(s[i : i + length])
            i += length
        return res


