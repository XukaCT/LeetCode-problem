class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0

        for k in range(2,len(arr)):
            for j in range(1, k):
                if abs(arr[j] - arr[k]) <= b:
                    for i in range(0, j):
                        if abs(arr[i] - arr[j]) <= a:
                            if abs(arr[i] - arr[k]) <= c:
                                    count += 1
                else:
                    continue
        return count
