# https://school.programmers.co.kr/learn/courses/30/lessons/81303

# 정확성 성공, 효율성 실패, 스택 이용
'''
def solution(n, k, cmd):
    stack = []
    answer = ['O'] * n
    cur = k

    for string in cmd:
        if string == 'C':
            answer[cur] = 'X'
            stack.append(cur)
            temp = ''.join(answer)
            next_index = temp.find('O', cur)
            cur = next_index if next_index != -1 else n - ''.join(reversed(temp)).find('O', 0, cur) - 1
            answer = list(temp)
        elif string == 'Z':
            idx = stack.pop()
            answer[idx] = 'O'
        else:
            direction, num = string.split(' ')
            cnt = int(num)
            if direction == 'U':
                for idx in range(cur - 1, -1, -1):
                    if answer[idx] == 'X': continue
                    if cnt == 1:
                        cur = idx
                        break
                    cnt -= 1
            else:
                for idx in range(cur + 1, n + 1):
                    if answer[idx] == 'X': continue
                    if cnt == 1:
                        cur = idx
                        break
                    cnt -= 1

    return ''.join(answer)
'''

# 모두 성공, 링크드 리스트 이용
def solution(n, k, cmd):
    linked_list = {i: [i - 1, i + 1] for i in range(n)}
    linked_list[0] = [None, 1]
    linked_list[n - 1] = [n - 2, None]
    stack = []
    cur = k
    answer = ['O'] * n

    for string in cmd:
        if string == 'C':
            answer[cur] = 'X'
            prev, nex = linked_list[cur]
            stack.append([prev, cur, nex])
            cur = nex if nex != None else prev
            if prev == None:
                linked_list[nex][0] = None
            elif nex == None:
                linked_list[prev][1] = None
            else:
                linked_list[nex][0] = prev
                linked_list[prev][1] = nex
        elif string == 'Z':
            prev, now, nex = stack.pop()
            answer[now] = 'O'
            if prev == None:
                linked_list[nex][0] = now
            elif nex == None:
                linked_list[prev][1] = now
            else:
                linked_list[nex][0] = now
                linked_list[prev][1] = now
        else:
            direction, num = string.split(' ')
            if direction == 'U':
                for _ in range(int(num)):
                    if linked_list[cur][0] == None:
                        break
                    cur = linked_list[cur][0]
            else:
                for _ in range(int(num)):
                    if linked_list[cur][1] == None:
                        break
                    cur = linked_list[cur][1]

    return ''.join(answer)