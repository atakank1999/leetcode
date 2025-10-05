class Solution:
    def reverseString(self, s:list)->list:
        left = 0
        right = len(s)-1
        while left < right:
            s[left],s[right] = s[right],s[left]
            left,right = left+1,right-1
        return s
            
        
    def reverseWords(self, s: str) -> str:
        rev = self.reverseString(list(s))
        n = len(rev)
        i = 0
        left = 0
        right = 0
        while i < n:
            
            while(i<n and rev[i] == " "):
                i+=1

            while(i<n and rev[i] != " "):
                rev[right] = rev[i] 
                right +=1
                i+=1

            l = left
            r = right-1
            while(l < r):
                tmp = rev[l]
                rev[l] = rev[r]
                rev[r] = tmp
                l,r = l+1,r-1

            if right<n:
                if rev[right]!= " ":
                    rev[right] = " "
                    
                right+=1

            left = right
        if right<n:
            rev = rev[:right-1]
        rev = "".join(rev).strip()
        return rev









            

            



            
            

            

            



            

            




            

                
            
