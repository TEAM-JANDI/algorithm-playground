# 링크: https://www.acmicpc.net/problem/1026
# 메모리: 31252 KB
# 시간: 40 ms

import sys

ssr = sys.stdin.readline
N = int(ssr())
a = list(map(int, ssr().split(' ')))
b = list(map(int, ssr().split(' ')))
answer = 0

a.sort()
b.sort(reverse=True)

for idx in range(N):
    answer += a[idx] * b[idx]

print(answer)