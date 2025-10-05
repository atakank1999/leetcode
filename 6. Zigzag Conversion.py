##O(1) space not using extra 2-d list

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        s_out = ""

        if numRows == 1:
            return s
        n = len(s)
        pattern = numRows*2 -2

        
        numCols = n//pattern + 2

        for i in range(numRows):
            for j in range (numCols):
                if i != 0 and i != numRows-1 and j != 0:
                    if j*pattern-i < n:
                        s_out += s[j*pattern-i]
                if i+j*pattern<n:
                    s_out += s[i+j*pattern]

        return s_out

