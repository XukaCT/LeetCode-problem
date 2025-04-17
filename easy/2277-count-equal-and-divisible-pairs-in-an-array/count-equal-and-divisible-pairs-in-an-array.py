class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0

        for num1 in range(0, n - 1):
            for num2 in range(num1, n):
                if num1 < num2:
                    if (num1 * num2) % k == 0:
                        if nums[num1] == nums[num2]:
                            count += 1
        return count