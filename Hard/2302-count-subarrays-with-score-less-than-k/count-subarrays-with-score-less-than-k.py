class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        res, left, win_sum = 0, 0, 0

        for right in range(len(nums)):
            win_sum += nums[right]

            while left <= right and win_sum * (right - left + 1) >= k:
                win_sum -= nums[left]
                left += 1
            
            res += right - left + 1
        return res
