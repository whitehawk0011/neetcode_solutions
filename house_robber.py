#https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        len_nums = len(nums)
        if len_nums ==0:
            return 0
        
        dp = {}
        dp[0]=nums[0]
        if len_nums==1:
            return dp[0]
        dp[1]=max(nums[1],nums[0])
        i =2
        while(i<=len_nums-1):
            dp[i]= max((nums[i]+ dp[i-2]),dp[i-1])
            i+=1

        result = (max(dp.values()))

        return result
        
        
        
        
