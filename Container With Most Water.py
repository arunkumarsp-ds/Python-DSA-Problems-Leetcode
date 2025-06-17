"""BruteForce Method:"""

def maxArea(self, height: List[int]) -> int:
        n= len(height)
        max_water = 0

        for i in range(n-1):
            for j in range(i+1,n):
                width = j-i
                current_water = min(height[i],height[j]) * width
                max_water = max(max_water,current_water)
        return max_water

""" Optimal Soltion Using Two Pointer"""
  def maxArea(self, height: List[int]) -> int:
        n= len(height)
        max_water = 0
        i = 0
        j = n-1
        while i < j:
            width = j-i
            current_water = min(height[i],height[j]) * width
            max_water = max(current_water, max_water)

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_water
