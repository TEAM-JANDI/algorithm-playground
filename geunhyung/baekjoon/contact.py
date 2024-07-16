# https://www.acmicpc.net/problem/1013
# 메모리: 34736 KB
# 시간: 96 ms

import sys
import re

ssr = sys.stdin.readline
T = int(ssr())

pattern = re.compile('(100+1+|01)+')

for _ in range(T):
    string = ssr().rstrip()
    flag = pattern.fullmatch(string)
    print("NO") if not flag else print('YES')


'''
해당 문제는 정규표현식을 사용하는 문제
해당 패턴에 맞는 문자가 입력이 되었는지에 대한 문제로 패턴에 관한 정규표현식 이용이 가능한지 확인
'''