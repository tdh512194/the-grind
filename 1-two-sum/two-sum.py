class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            comple = target - nums[i]
            if comple in seen:
                return [i, seen[comple]]
            seen[nums[i]] = i
        return None