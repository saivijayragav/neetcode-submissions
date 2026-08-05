class Solution:
    def numSquares(self, n: int) -> int:
        allsq = []
        for i in range(1, n+1):
            if int(i**(0.5)) == i**0.5:
                allsq.append(i)
        
        dp = [float('inf')]*(n+1)
        dp[0] = 0
        for t in range(1, n+1):
            for num in allsq:
                dp[t] = min(dp[t], 1+dp[t-num])
        return dp[n]