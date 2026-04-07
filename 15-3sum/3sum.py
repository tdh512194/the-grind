class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        leng = len(nums)
        result = []
        seen = set()
        for k,c in enumerate(nums):
            if (c > 0):
                break
            if k == 0 or nums[k-1] < c:
                seen = set()
                j = k + 1
                while j < leng:
                    comp = - nums[k] - nums[j]
                    if comp in seen:
                        result.append([nums[k], nums[j], comp])
                        while j + 1 < leng and nums[j]  == nums[j+1]:
                            j += 1
                    seen.add(nums[j])
                    j += 1
        return result

                    
                    

                

                