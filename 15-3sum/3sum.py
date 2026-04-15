class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        leng = len(nums)
        seen = set()
        for k in range(leng-2):
            target = nums[k]
            if target > 0: 
                break
            i = k+1
            j = leng-1
            while i < j:
                current_sum = nums[i] + nums[j]
                if current_sum == - target:
                    to_add = [nums[k],nums[i],nums[j]]
                    if str(to_add) not in seen:
                        results.append(to_add)
                        seen.add(str(to_add))
                    else:
                        i += 1
                        continue
                elif current_sum < -target:
                    i += 1
                    continue
                else:
                    j -= 1
                    continue
        return results

                    
                    

                

                