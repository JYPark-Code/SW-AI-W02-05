# 문자열 - IPv6 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/3107

"""
문제
IPv6은 길이가 128비트인 차세대 인터넷 프로토콜이다.

IPv6의 주소는 32자리의 16진수를 4자리씩 끊어 나타낸다. 이때, 각 그룹은 콜론 (:)으로 구분해서 나타낸다.

예를 들면, 다음과 같다.

2001:0db8:85a3:0000:0000:8a2e:0370:7334
32자리의 16진수는 사람이 읽고 쓰기에 불편하고, 대부분의 자리가 0이기 때문에 아래와 같이 축약할 수 있다.

각 그룹의 앞자리의 0의 전체 또는 일부를 생략 할 수 있다. 위의 IPv6을 축약하면, 다음과 같다
2001:db8:85a3:0:00:8a2e:370:7334
만약 0으로만 이루어져 있는 그룹이 있을 경우 그 중 한 개 이상 연속된 그룹을 하나 골라 콜론 2개(::)로 바꿀 수 있다.
2001:db8:85a3::8a2e:370:7334
2번째 규칙은 모호함을 방지하기 위해서 오직 한 번만 사용할 수 있다.

올바른 축약형 IPv6주소가 주어졌을 때, 이를 원래 IPv6 (32자리의 16진수)로 복원하는 프로그램을 작성하시오.

입력
첫째 줄에 올바른 IPv6 주소가 주어진다. 이 주소는 최대 39글자이다. 또한, 주소는 숫자 0-9, 알파벳 소문자 a-f, 콜론 :으로만 이루어져 있다.

출력
첫째 줄에, 입력으로 주어진 IPv6의 축약되지 않은 형태를 출력한다.

입력 1
25:09:1985:aa:091:4846:374:bb

출력 1
0025:0009:1985:00aa:0091:4846:0374:00bb

입력 2
2001:db8:85a3::8a2e:370:7334

출력 2
2001:0db8:85a3:0000:0000:8a2e:0370:7334

입력 3
::1

출력 3
0000:0000:0000:0000:0000:0000:0000:0001

"""

import sys
input = sys.stdin.readline

address_must_length = 8
short_address = input().strip()

# zfill(4) 사용해서 0001 형태 만들기 (string에 사용가능)

address_list = short_address.split(":")

if "::" in short_address:
    left, right = short_address.split("::")
    left = left.split(":") if left else [] # 비어있지 않는 것 체크
    right = right.split(":") if right else [] # 비어있지 않는 것 체크

    # print(left, len(left))
    # print(right, len(right))

    missing = address_must_length - ( len(left) + len(right) )

    result = left + ["0000"] * missing + right # list 형태로 합쳐진다.

    # print(result)
    print(":".join(x.zfill(4) for x in result))

else:
    print(":".join(address.zfill(4) for address in address_list))




