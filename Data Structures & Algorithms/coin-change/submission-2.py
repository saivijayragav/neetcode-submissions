class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        for s in range(1, amount+1):
            for c in coins:
                if c > s:
                    continue
                dp[s] = min(dp[s], dp[s-c] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1