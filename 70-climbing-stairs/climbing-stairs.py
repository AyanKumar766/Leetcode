class Solution:
    def climbStairs(self, n: int) -> int:
        # Initialize DP array
        dp = [-1] * (n + 1)
        dp[0] = 1  # 1 way for 0 stairs
        dp[1] = 1  # 1 way for 1 stair
        
        # Fill array bottom-up
        for index in range(2, n + 1):
            dp[index] = dp[index - 1] + dp[index - 2]  # Ways = from (index-1) + from (index-2)
        
        return dp[n]