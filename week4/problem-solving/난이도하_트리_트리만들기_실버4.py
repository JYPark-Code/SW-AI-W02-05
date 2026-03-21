# 트리 - 트리 만들기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/14244

"""
n과 m이 주어졌을 때, n개의 노드로 이루어져 있고, m개의 리프로 이루어져 있는 트리를 만드는 프로그램을 작성하시오.

항상 정답이 존재하는 경우만 입력으로 주어진다.

트리는 사이클이 없는 연결 그래프이고, 리프는 차수가 1인 노드를 의미한다.

입력
첫째 줄에 n과 m이 주어진다. (3 ≤ n ≤ 50, 2 ≤ m ≤ n-1)

출력
첫째 줄부터 n-1개의 줄에 트리의 간선 정보를 출력한다. 트리의 정점은 0번부터 n-1번까지 이다.
"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

"""
Leaf Node를 늘리는 방법을 생각해보자
노드만 늘리기 : 그냥 기존 리프에 붙이면 리프수 변화 X (+1, 0)
내부 노드에 붙이기 : 리프 수 +1 (+1, +1)

전체 답은 n-1개 나오지만 
내부 노드를 k개로 두고
내부 줄기를 만드는데 k-1 (n-m-1) 이 필요.
"""

k = n-m

if k == 1:

    for i in range(1, n):
        print(0, i)

elif k >= 2:

    for i in range(k):
        print(i, i+1)

    leaf = k

    for i in range(k + 1, n):
        print(leaf, i)