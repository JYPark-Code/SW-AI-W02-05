# DP - 피보나치 수 2 (백준 브론즈 1)
# 문제 링크: https://www.acmicpc.net/problem/2748
import sys
input = sys.stdin.readline

n = int(input().strip())

if n == 0:
    print(0)
    exit()
if n == 1:
    print(1)
    exit()
if n == 2:
    print(1)
    exit()

if n >= 3:
    dp = [0] * (n+1)

dp[0] = 0
dp[1] = 1
dp[2] = 1


for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])