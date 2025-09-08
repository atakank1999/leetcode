class Solution:
    def intToRoman(self, num: int) -> str:
        conversions = ["I","V","X","L","C","D","M",""]
        strnum = str(num)
        nums = list(strnum)
        n = len(nums)
        res = ""


        for i in range(n):
            current = ""
            decimal = int(nums[n-1-i])
            if decimal %5 == 4:
                decimal +=1
                current += conversions[2*i]
            if decimal == 10:
                current += conversions[2*i+2]
            elif decimal >= 5:
                current += conversions[2*i+1]
            current += conversions[2*i] * (decimal%5)
            res = current + res

        return res


            
            

                



