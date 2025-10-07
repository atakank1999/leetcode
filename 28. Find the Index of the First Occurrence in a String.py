class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if(len(needle) > len(haystack)):
            return -1
        for i in range(len(haystack)):
            for j in range(len(needle)):
                if(i + j >= len(haystack) or haystack[i+j] != needle[j]):
                    break
                if j == len(needle)-1:
                    return i
        return -1
            
        # return haystack.find(needle)
