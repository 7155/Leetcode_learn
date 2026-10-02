from functools import cache
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n=len(nums)
        sum_num=sum(nums)
        if sum_num % 2==1: # 奇数
            return False

        target=sum_num//2
        @cache
        def f(i,rest_num): # 对于前i个数字进行选择  剩余容量rest_num  是否可以使背包恰好填满
            if rest_num==0:
                return True
            if i==0:
                return False


            if rest_num-nums[i-1]>=0:
                return f(i-1,rest_num-nums[i-1]) or f(i - 1, rest_num)
            else:
                return f(i - 1, rest_num)


        return f(n,target)


# dp动态规划
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n=len(nums)
        sum_num=sum(nums)
        if sum_num % 2==1: # 奇数
            return False
        target=sum_num//2

        dp= [[False]*(target+1) for _ in range(n+1)]
        for i in range(0,n+1):
            dp[i][0]=True

        for i in range(1,n+1):
            for rest_num in range(0,target+1):
                if rest_num - nums[i - 1] >= 0:
                    dp[i][rest_num] = dp[i - 1][ rest_num - nums[i - 1]] or dp[i - 1][ rest_num]
                else:
                    dp[i][rest_num] = dp[i - 1][ rest_num]

        return dp[n][target]










