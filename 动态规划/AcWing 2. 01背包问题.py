from functools import cache
import sys
sys.setrecursionlimit(10000)

parts=input().split() # ["4","5"]  # "4  5  "  ["4","","5",""]
n=int(parts[0])
V=int(parts[1])

volume=[]
worth=[]
for _ in range(n):
    parts = input().split()
    volume.append(int(parts[0]))
    worth.append(int(parts[1]))

@cache
def f(i,rest_V): # 在前i个物品中选择  且背包剩余为 rest_V 时  的最大价值
    if i==0:
        return 0

    if rest_V-volume[i-1]>=0:
        # 选
        a = worth[i - 1] + f(i - 1, rest_V - volume[i - 1])
        # 不选
        b = f(i - 1, rest_V)
        return max(a, b)
    else:
        return f(i - 1, rest_V)


print(f(n,V))


# -------------- 改写dp数组 ---------------
parts=input().split()
n=int(parts[0])
V=int(parts[1])
volume=[]
worth=[]
for _ in range(n):
    parts = input().split()
    volume.append(int(parts[0]))
    worth.append(int(parts[1]))

dp = [[0]*(V+1) for _ in range(n+1)]
for i in range(1,n+1): # 1,2,...,n
    for rest_V in range(1,V+1): # 1,2,...,V
        if rest_V - volume[i - 1] >= 0:
            # 选
            a = worth[i - 1] + dp[i - 1][ rest_V - volume[i - 1]]
            # 不选
            b = dp[i - 1][ rest_V]
            dp[i][rest_V]= max(a, b)
        else:
            dp[i][rest_V]= dp[i - 1][ rest_V]

print(dp[n][V])















