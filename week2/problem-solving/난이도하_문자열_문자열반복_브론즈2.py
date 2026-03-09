# 문자열 - 문자열 반복 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/2675

# 문제 :
#
# 문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오.
# 즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다.
# S에는 QR Code "alphanumeric" 문자만 들어있다.
# QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.
#
# 임력 :
#
# 첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다.
# 각 테스트 케이스는 반복 횟수 R(1 ≤ R ≤ 8), 문자열 S가 공백으로 구분되어 주어진다.
# S의 길이는 적어도 1이며, 20글자를 넘지 않는다.
#
# 입력값 예시:
#
# 2
# 3 ABC
# 5 /HTP

import sys
input = sys.stdin.readline

# 문자열 누적 - 비효율
# T = int(input())
#
# answer_list = list()
#
# for _ in range(T):
#
#     R, S = input().split()
#
#     R = int(R)
#
#     answer = ""
#
#     for ch in S:
#         answer += (ch * R)
#
#     answer_list.append(answer)
#
# for ans in answer_list:
#     print(ans)

# join 써서 풀기
T = int(input())

for _ in range(T):
    R, S = input().split()
    R = int(R)
    print("".join(ch * R for ch in S))