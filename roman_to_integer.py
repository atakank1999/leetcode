class Solution:
    def trap(self, height: List[int]) -> int:

        sum = 0
        n = len(height)
        left_index = 0
        right_index = n-1
        max = 0
        left_max = height[left_index]
        right_max = height[right_index]
        while(left_index < right_index):
            if left_max >= right_max:
                right_index-=1
                if height[right_index] < right_max:
                    sum+= right_max - height[right_index]
                else:
                    right_max = height[right_index]
            else:
                left_index+=1
                if height[left_index] < left_max:
                    sum+= left_max - height[left_index]
                else:
                    left_max = height[left_index]
        return sum


            
