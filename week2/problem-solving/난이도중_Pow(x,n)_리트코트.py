# https://leetcode.com/problems/powx-n/description/?envType=study-plan-v2&envId=top-interview-150

def myPow(x: float, n: int) -> float:

    # 순서대로 for문을 돌리면 답은 맞으나 Timeout

    # answer = 1

    # if n == 0:
    #     return float(answer)

    # if n > 0:
    #     for _ in range(n):
    #         answer *= x
    #     return answer

    # if n < 0:
    #     m = abs(n)
    #     for _ in range(m):
    #         answer *= x
    #     return 1 / answer


    # (n^2)^2 이 방식으로 n // 2로 순차적으로 해결

    if n == 0:
        return 1.0

    # 음수 지수 처리
    if n < 0:
        x = 1 / x
        n = -n

    answer = 1.0

    while n > 0:
        # 현재 지수가 홀수면 answer에 x를 반영
        if n % 2 == 1:
            answer *= x

        # 밑을 제곱
        x *= x

        # 지수를 절반으로 줄임
        n //= 2

    return answer