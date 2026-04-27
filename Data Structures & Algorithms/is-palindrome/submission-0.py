class Solution:
    def isPalindrome(self, s: str) -> bool:
        clear_str="".join(char for char in s if char.isalnum())
        clear_str=clear_str.lower()
        left=0
        right=len(clear_str)-1
        while left<right:
            if clear_str[left]==clear_str[right]:
                left+=1
                right-=1
            else:
                return False
        return True