# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/152995#

def solution(scores):
    answer = 1
    temp = 0
    target_sum, target_first, target_second = sum(scores[0]), scores[0][0], scores[0][1]
    scores.sort(key=lambda x: (-x[0], x[1]))

    for a, b in scores:
        if target_first < a and target_second < b:
            return -1
        if temp <= b:
            temp = b
            if a + b > target_sum:
                answer += 1
    return answer