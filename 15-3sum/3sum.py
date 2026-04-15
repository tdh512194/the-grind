class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # the idea is utilizing TwoSumII
        # we have 3 pointers, the first one move
        # from left to right, acting as an anchor.
        # the other two pointers move like TwoSumII
        # where we set them at the two ends and move them inwards
        # depending on how the sum of these two larger (move i->)
        # or smaller than the target (move <-j)
        # the tricky part is duplications 
        # we need to skip the duplicated target
        # AND we need to skip the duplicated low by moving inwards
        # until we found a new low
        nums.sort()
        results = []
        leng = len(nums)
        for k in range(leng-2):
            target = nums[k]
            if target > 0: 
                break
            # skip the duplicated target
            if (k > 0 and nums[k] == nums[k-1]):
                continue
            i = k+1
            j = leng-1
            while i < j:
                current_sum = nums[i] + nums[j]
                if current_sum < -target:
                    i+=1
                elif current_sum > -target:
                    j-=1
                else:
                    to_add = [nums[k],nums[i],nums[j]]
                    results.append(to_add)
                    i += 1
                    j -= 1
                    # we need to keep move the 2 pointers inward to avoid duplications
                    while i < j and nums[i] == nums[i-1]:
                        i += 1
        return results
                    
                    

                

                