# 정수론 - 소수 찾기 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/1978
'''
문제
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

입력
첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

출력
주어진 수들 중 소수의 개수를 출력한다.

4
1 3 5 7

3
'''
import math
import sys
input = sys.stdin.readline

def is_prime(n):

    if n < 2:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    # for i in range(3, int(math.sqrt(n)) + 1, 2):
    #     if n % i == 0:
    #         return False

    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2

    return True

N = int(input())
num_list = list(map(int, input().split()))
answer = 0

for num in num_list:
    if is_prime(num):
        answer += 1

print(answer)