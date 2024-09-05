# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/86052

def solution(grid):
    answer = []
    n, m = len(grid), len(grid[0])
    visited = [[[False for _ in range(4)] for _ in range(m)] for _ in range(n)]
    dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

    for r in range(n):
        for c in range(m):
            for d in range(4):
                if not visited[r][c][d]:
                    cx, cy, cd = r, c, d
                    cnt = 0
                    while not visited[cx][cy][cd]:
                        visited[cx][cy][cd] = True
                        cnt += 1
                        cx, cy = (cx + dx[cd]) % n, (cy + dy[cd]) % m
                        node = grid[cx][cy]
                        if node == "L":
                            cd = (cd + 1) % 4
                        elif node == "R":
                            cd = (cd - 1) % 4
                    answer.append(cnt)
    return sorted(answer)

'''
node의 방문만 바라볼 것이 아니라
node와 나아갈 방향까지도 방문을 한 것인지 확인을 해야하는 문제이다.
'''