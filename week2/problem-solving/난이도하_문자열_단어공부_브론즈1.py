# 문자열 - 단어 공부 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/1157
from collections import Counter

s = input().upper() # MISSISSIPPI
c = Counter(s)

# 횟수 세기
# max_count = max(c.values())
#
# if list(c.values()).count(max_count) > 1:
#     print("?")
# else:
#     for k, v in c.items():
#         if v == max_count:
#             print(k)

# 최상위 2개만 뽑아내기 - better
top = c.most_common(2) # [('I', 4), ('S', 4)]

if len(top) > 1 and top[0][1] == top[1][1]:
    print("?")
else:
    print(top[0][0])