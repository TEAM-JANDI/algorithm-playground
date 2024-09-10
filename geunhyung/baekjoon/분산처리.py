# 링크: https://www.acmicpc.net/problem/1026
# 메모리: 31220 KB
# 시간: 28 ms

import sys

ssr = sys.stdin.readline
T = int(ssr())

for _ in range(T):
    a, b = map(int, ssr().split(' '))
    a %= 10

    if a == 0: print(10)
    elif a == 1 or a == 5 or a == 6: print(a)
    elif a == 4 or a == 9:
        print((a**2) % 10 if b % 2 == 0 else a % 10)
    else:
        rem = b % 4
        l = [a**4, a, a**2, a**3]
        print(int(str(l[rem])[-1]))

'''
몇 번을 제곱해도 일의 자리의 숫자는 규칙을 가지면서 일정하게 변하게 된다.
그것을 이용하는 문제이다.
'''