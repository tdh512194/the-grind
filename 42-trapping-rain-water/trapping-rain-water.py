class Solution:
    def trap(self, height: List[int]) -> int:
        """
        maintain left_max,right_max,left and right
        we can add the water of left_max - height[left] if the right is larger than left
        it means that left is min(left_max, someright but it surely higher than left max)
        ok why is it higher than left max?
        because if it is smaller than left_max, we would have move the right pointer
        inward until it's smaller than left
        vice versa, the same logic applies for the right
        """
        i = 0
        right_max, left_max = 0, 0
        result = 0
        right = len(height)-1
        left = 0
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
        