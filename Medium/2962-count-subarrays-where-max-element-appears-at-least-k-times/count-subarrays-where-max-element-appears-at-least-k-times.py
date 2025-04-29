class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        left = 0
        count = 0
        max_num = max(nums)
        max_num_count = 0
        n = len(nums)

        for right in range(n):
            if nums[right] == max_num:
                max_num_count += 1
            while k == max_num_count:
                if nums[left] == max_num:
                    max_num_count -= 1   
                left += 1
            count += left
            
        return count
