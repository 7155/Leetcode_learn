


from functools import cache

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m=len(text1)
        n=len(text2)

        @cache
        def f(i,j): # text1的0~i范围  text2的0~j范围 最长公共子序列的长度
            if i==-1: # "" 空串
                return 0
            if j==-1:
                return 0

            # 考虑 i 指针和 j 指针指向的字符
            if text1[i]==text2[j]: # 这两个字符一样
                return f(i-1,j-1)+1
            else:  # 这两个字符不一样
                return max(f(i,j-1),f(i-1,j))


        return f(m-1,n-1)



# dp
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m=len(text1)
        n=len(text2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m): # 0,1,2,...,m-1
            for j in range(n): # 0,1,2,...,n-1
                # 考虑 i 指针和 j 指针指向的字符
                if text1[i] == text2[j]:  # 这两个字符一样
                    dp[i][j]= dp[i - 1][ j - 1] + 1
                else:  # 这两个字符不一样
                    dp[i][j]= max(dp[i][ j - 1], dp[i - 1][ j])

        return dp[m-1][n-1]



