class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        count = 0
        min_pos = max_pos = bad_pos = -1

        for i, num in enumerate(nums):
            if num == minK:
                min_pos = i
            
            if num == maxK:
                max_pos = i
            
            if  num < minK or num > maxK:
                bad_pos = i
            if min_pos > bad_pos and max_pos > bad_pos:
                count += (min(min_pos, max_pos) - bad_pos)
        return count
