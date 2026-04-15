class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # the idea is we have 2 pointers and it is sorted
        # so if the sum is less than target, we move the left
        # pointer inwards and vice versa
        i,j = 0, len(numbers)-1
        while i < j:
            current_sum = numbers[i] + numbers[j]
            if current_sum < target:
                i += 1
                continue
            elif current_sum > target:
                j -= 1
                continue
            else:
                return [i+1,j+1]
        return [1,1]
            