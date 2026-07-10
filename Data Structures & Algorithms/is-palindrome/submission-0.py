class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower()
        str_list = []
        for i in s:
            if i.isalnum():

                str_list.append(i)
        s = "".join(str_list)
        i = 0
        j = len(s)-1
        while i<j:
            if s[i]!=s[j]:
                return False
            i = i + 1
            j = j - 1
        return True