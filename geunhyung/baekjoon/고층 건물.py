# 링크: https://www.acmicpc.net/problem/1027
# 시간: 36ms

import sys

ssr = sys.stdin.readline
N = int(ssr())
l = list(map(int, ssr().split(' ')))


def solution(buildings):
    ret = 0
    if N == 1:
        return ret

    for i1, y1 in enumerate(buildings):
        temp = 0
        x1 = i1 + 1
        inc = None
        for i2 in range(i1 + 1, N):
            x2 = i2 + 1
            y2 = buildings[i2]
            a = (y2 - y1) / (x2 - x1) if x2 - x1 != 0 else 0
            if inc is None or inc < a:
                inc = a
                temp += 1

        inc = None
        for i2 in range(i1 - 1, -1, -1):
            x2 = i2 + 1
            y2 = buildings[i2]
            a = (y2 - y1) / (x2 - x1) if x2 - x1 != 0 else 0
            if inc is None or inc > a:
                inc = a
                temp += 1

        ret = max(temp, ret)

    return ret


print(solution(l))

'''
1. 한 건물에서 볼 수 있는 건물의 개수를 구하는 것은 일단 왼쪽과 오른쪽으로 나눈다.
2. 두 건물 사이에 직선을 그었을 때 기울기를 구한다.
3-1. 오른쪽은 이전 건물의 기울기보다 더 크면 볼 수 있다.
3-2. 왼쪽은 이전 건물보의 기울기보다 더 작으면 볼 수 있다.
4. 이를 통해서 한 건물에서 볼 수 있는 건물 수를 구하고 그 중 최댓값을 구하면 된다.  
'''