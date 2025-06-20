class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        result = 0
        N,S,W,E = 0,0,0,0
        for i in range(len(s)):
            char = s[i]
            if char == "N":
                N += 1
            elif char == "W":
                W += 1
            elif char == "S":
                S += 1
            else:
                E += 1
        
            x = abs(N - S)
            y = abs(E - W)
            dis = x+y
            result = max(result,dis + min(2*k, i+1 - dis))
        return result
