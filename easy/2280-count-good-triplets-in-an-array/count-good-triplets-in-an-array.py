
class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        pos2 = {val: i for i, val in enumerate(nums2)}
        transformed = [pos2[val] for val in nums1]

        class BIT:
            def __init__(self, size):
                self.tree = [0] * (size + 2)

            def update(self, i, delta):
                i += 1
                while i < len(self.tree):
                    self.tree[i] += delta
                    i += i & -i

            def query(self, i):
                i += 1
                res = 0
                while i > 0:
                    res += self.tree[i]
                    i -= i & -i
                return res

        bit_left = BIT(n)
        bit_right = BIT(n)

        for idx in transformed:
            bit_right.update(idx, 1)

        result = 0
        for idx in transformed:
            bit_right.update(idx, -1)

            left_smaller = bit_left.query(idx - 1)
            right_greater = bit_right.query(n - 1) - bit_right.query(idx)

            result += left_smaller * right_greater

            bit_left.update(idx, 1)

        return result
