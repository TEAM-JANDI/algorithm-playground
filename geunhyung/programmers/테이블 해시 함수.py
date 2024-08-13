# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/147354

def solution(data, col, row_begin, row_end):
    answer = 0
    data = sorted(data, key=lambda x: (x[col-1], -x[0]))
    for idx in range(row_begin-1, row_end):
        Sum = 0
        for element in data[idx]:
            Sum += element % (idx+1)
        answer = answer ^ Sum
    return answer

'''
해당 문제는 정답률 47%이다.
1. 아마 xor 연산을 어떻게 하는지 몰라서 틀렸거나
2. 정렬을 비효율적으로 해서 시간초과가 났거나
3. 0을 xor 연산하면 자기자신이 나온다는 것을 모르거나

그랬을 확률이 있다. 
'''