class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return s
        def expand(s:str,left:int,right:int,n:int):
            while left>=0 and right <=n-1:
                if s[left] == s[right]:
                    left-=1
                    right+=1
                else:
                    return left+1,right-1
            return left+1,right-1

        start,end = 0,0
        for i in range(n):
            left_two,right_two = expand(s,i,i,n)
            left_three,right_three = expand(s,i,i+1,n)
            two_len = right_two-left_two+1
            three_len = right_three-left_three+1
            left,right = (left_two, right_two) if max(two_len,three_len) == two_len else (left_three,right_three)
            if max(two_len,three_len) > end-start+1:
                start = left
                end = right
        return s[start:end+1]
        
            








