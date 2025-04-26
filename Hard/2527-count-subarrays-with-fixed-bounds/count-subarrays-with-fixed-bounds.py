class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        count = 0
        min_pos = max_pos = bad_pos = -1

        for i, num in enumerate(nums):
            if num == minK:
                min_pos = i
            
            if num == maxK:
                max_pos = i
            
            if  minK > num or num > maxK:
                bad_pos = i
            
            count += max(0, min(min_pos, max_pos) - bad_pos)
        return count
