# 링크: https://www.acmicpc.net/problem/1019
# 시간: 36ms
# 메모리: 31120KB

import sys

ssr = sys.stdin.readline
n = int(ssr())
l = [0 for _ in range(10)] # 0~9 갯수
weight = 1 # 단위

for step in range(len(str(n))):
    temp = int(str(n//10) + "9") # 일의 자리를 9로 만든 수를 구해보자. 일의 자리가 최고인 숫자를 구하는 것이다.
    rem = temp - n # 일의 자리의 차이를 구하는 것이다.
    for idx in range(10):
        l[idx] += (n//10 + 1) * weight # 일의 자리를 고려하지 않으면 각 숫자가 나타나는 횟수는 (현재 수 / 10 + 1) * 단위
    for idx in range(10-rem, 10):
        l[idx] -= weight # 원래 일의 자리 숫자에서 9까지의 수는 일의 자리에서 단위만큼의 수가 안 나타나므로 빼야한다.
    for num in list(str(n))[:-1]:
        num = int(num)
        l[num] -= weight * rem # 그 위의 단위의 숫자도 일의 자리가 안 나타나는 수가 있으므로 해당 단위만큼의 수를 뺴줘야 한다.

    l[0] -= weight # 0은 시작 숫자가 아니므로 해당 단위만큼의 개수만큼 빼줘야 한다.
    n //= 10 # 일의 자리를 버리기 위함.
    weight *= 10 # 단위 증가
print(' '.join(map(str, l)))