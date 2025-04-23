class Solution:
    def countLargestGroup(self, n: int) -> int:
        count = 0
        max_length = 0
        dic = defaultdict(int)
        for num in range (1,n+1):
            temp = sum(int(ch) for ch in str(num))  
            dic[temp] += 1
            if dic[temp] > max_length:
                max_length = dic[temp]
        for i in dic:
            if dic[i] == max_length:
                count += 1
        return count 