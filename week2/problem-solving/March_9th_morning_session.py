"""
2026년 3월 9일 월요일 (Week2) - 10:00 ~ 11:00 알고리즘 강의 - 이동석 코치님
"""

'''
element of programming

1. primitive expression

2. means of combination

3. means of abstraction - making function. - most important but not specified on one meaning.
 - how를 숨기고, what을 보여주는, naming으로만 define하는 것.
'''
def nsum(n):
    # return sum([x for x in range(n+1)])

    return sum(list(range(n+1)))

# recursion
## 특징 1 : 중간의 break를 넣으면 끝까지 답을 못 구한다.
## 특징 2 : 무조건 변곡점이 생긴다. (base-condition까지 갔다가 돌아옴)
## 특징 3 : 성능이 저하된다.

def rec_nsum(n):

    # base condition을 지정해야 한다. (무한정 내려가는 걸 방지하기 위해, (돌아오지 않음))
    if n == 0:
        return 0

    else:
        return n + rec_nsum(n-1)

# tail recursion - 중간의 break를 두어도 부분합이 나온다.
## 특징 1 : return 자체에 자기 자신을 호출한다.
## 특징 2 : 기존 rec 보다 속도가 빠르고, for문과 동일하게 작동한다.
### python은 tail recursion을 권장하지 않는다.

def sum_iter(n, total):
    if n == 0:
        return total
    else:
        return sum_iter(n-1, total+n)

def i_sum(n):
    return sum_iter(n, 0)

# Exponentiation (거듭제곱) - rec
def expt(a, n):

    if n == 0:
        return 1

    else:
        return a * expt(a, n-1)

# Exp - tail ver
def tail_expt(a, n):
    pass

# fast exponentiation
def fast_expt(a, n):
    if n == 0:
        return 1
    else:
        if n % 2 == 0:
            return pow(fast_expt(a, n/2), 2)
        else:
            return a * fast_expt(a, n-1)

# fibonacci - tree recursion
# 이러면 결국 겹치는 연산이 존재한다. -> 오버헤드가 심해진다.

def fibo(n):

    if n == 0:
        return 0
    elif n == 1:
        return 1

    else:
        return fibo(n-1) + fibo(n-2)

# fibo - tail version

def fibo_tail(n):
    def fibo_iter(a,b, count):
        if count == 0:
            return b
        else:
            return fibo_iter(b, a+b, count-1)

    return fibo_iter(0,1, n)

"""
재귀는 큰 문제를 작은 문제로 나누고, 그 작은 문제가 자기 자신과 구조가 동일할 때 적용할 수
있는 해결 방법
● 문제 파악: 이 문제를 자기 자신보다 작은 하위 문제로 표현할 수 있는가?
● 기저 조건 정의: 언제 재귀 호출을 멈출 것인가?
● 하위 문제 호출: 더 작은 인풋에 대해 자기 자신을 호출
● 결과 조합: 하위 문제의 결과를 조합하여 전체 문제 해결
"""


# Counting change Problem - 동전 거슬러주는 방법 세기
"""
 금액 4 동전 종류 [1,2,3]
 정답 : [1,1,1,1], [1,1,2], [2,2], [3,1]
 
 접근 방법 : 1만 사용해서 만들기, 1,2만 사용해서 만들기, 2만 사용해서 사용하기 ... 1,2,3만 이용해서 하기
 * 정답 완성하기
"""

def count_change(amount, coins):
    if amount == 0:
        return 1
    if amount < 0 or len(coins) == 0:
        return 0
    return count_change(amount, coins[1:]) + count_change(amount - coins[0], coins)

# 하노이의 탑 hanoi tower
"""
시간 관계상 알아서 풀 것 : 과제 백준 문제로도 있다. 난이도 중.
"""



# print(nsum(10)) # 55
# print(rec_nsum(10)) # 55
# print(i_sum(5)) # 15
# print(expt(2,2)) # 4
# print(fast_expt(2,2)) # 4
# print(fibo(5))