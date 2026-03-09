# 완전탐색 - 차이를 최대로 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10819

"""
문제
N개의 정수로 이루어진 배열 A가 주어진다.
이때, 배열에 들어있는 정수의 순서를 적절히 바꿔서 다음 식의 최댓값을 구하는 프로그램을 작성하시오.

|A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]|

입력
첫째 줄에 N (3 ≤ N ≤ 8)이 주어진다.
둘째 줄에는 배열 A에 들어있는 정수가 주어진다. 배열에 들어있는 정수는 -100보다 크거나 같고, 100보다 작거나 같다.

출력
첫째 줄에 배열에 들어있는 수의 순서를 적절히 바꿔서 얻을 수 있는 식의 최댓값을 출력한다.

입력 1
6
20 1 15 8 4 10

출력 1
62

"""
import sys
input = sys.stdin.readline
from itertools import permutations

N = int(input())
arr = list(map(int, input().split()))

max_value = 0

for p in permutations(arr):
    total = 0

    # 한개의 항 부족하게 나옴.
    for i in range(N-1):
        total += abs(p[i] - p[i+1])

    max_value = max(max_value, total)

print(max_value)

