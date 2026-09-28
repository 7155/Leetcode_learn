from functools import cache


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m=len(word1)
        n=len(word2)
        @cache
        def f(i,j): # word1的0~i子串 到word2的0~j子串  转换所使用的最少操作数
            if i==-1:
                return j+1
            if j==-1:
                return i+1

            if word1[i]==word2[j]:
                return f(i-1,j-1)
            else:
                # 删掉i字符
                a=1+f(i-1,j)
                # i后面插入j相同字符
                b=1+f(i,j-1)
                # i位置替换成j相同字符
                c=1+f(i-1,j-1)
                return min(a,b,c)

        return f(m-1,n-1)

# 改写
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m=len(word1)
        n=len(word2)
        @cache
        def g(i,j): # word1的前i个的子串 到word2的前j个的子串 转换所使用的最少操作数
            if i==0:
                return j
            if j==0:
                return i

            if word1[i-1]==word2[j-1]:
                return g(i-1,j-1)
            else:
                a=1+g(i-1,j)
                b=1+g(i,j-1)
                c=1+g(i-1,j-1)
                return min(a,b,c)

        return g(m,n)

# dp数组动态规划
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m=len(word1)
        n=len(word2)
        dp= [[0]*(n+1) for _ in range(m+1)]
        # 初始化base case
        for i in range(m+1): # 0,1,...,m
            dp[i][0]=i
        for j in range(n+1): # 0,1,...,n
            dp[0][j]=j

        for i in range(1,m+1): # 1,2,...,m
            for j in range(1,n+1): # 1,2,...,n
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j]= dp[i - 1][ j - 1]
                else:
                    a = 1 + dp[i - 1][ j]
                    b = 1 + dp[i][ j - 1]
                    c = 1 + dp[i - 1][ j - 1]
                    dp[i][j]= min(a, b, c)

        return dp[m][n]








