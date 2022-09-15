class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        len_cost = len(cost)
        dp={}
        dp[len_cost-1] = cost[len_cost-1]
        dp[len_cost-2] = cost[len_cost-2]
        i = len_cost-3
        
        while i >= 0:
            dp[i]= cost[i] + min(dp[i+1],dp[i+2])
            i-=1
        return min(dp[0],dp[1])
      
      #https://leetcode.com/problems/min-cost-climbing-stairs/submissions/
