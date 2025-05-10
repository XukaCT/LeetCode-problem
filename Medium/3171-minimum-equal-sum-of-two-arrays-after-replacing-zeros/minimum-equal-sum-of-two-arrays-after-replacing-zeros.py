class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        total1, count1 = 0, 0
        total2, count2 = 0, 0
        for num1 in nums1:
            total1 += num1
            if num1 == 0:
                total1 += 1
                count1 += 1
        
        for num2 in nums2:
            total2 += num2
            if num2 == 0:
                total2 += 1
                count2 += 1
        
        if (count1 == 0 and total2 > total1) or (count2 == 0 and total1 > total2):
            return -1
        return max(total1, total2)