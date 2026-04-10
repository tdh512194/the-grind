class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        left_max, right_max = 0, 0
        result = 0
        left = 0
        right = len(height)-1
        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])

            if height[left] < height[right]:
                add = left_max - height[left]
                result += add
                left += 1
            else:
                add = right_max - height[right]
                result += add
                right -= 1
        return result
        