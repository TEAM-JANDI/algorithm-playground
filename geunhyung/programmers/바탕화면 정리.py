# 링크:https://school.programmers.co.kr/learn/courses/30/lessons/161990

def solution(wallpaper):
    col_wallpaper = list(zip(*wallpaper))
    len_x, len_y = len(wallpaper), len(wallpaper[0])
    lux, luy, rdx, rdy = len_x, len_y, 0, 0
    for x in range(len_x):
        if '#' in wallpaper[x]:
            if lux > x:
                lux = x
            if rdx <= x:
                rdx = x+1
    for y in range(len_y):
        if '#' in col_wallpaper[y]:
            if luy > y:
                luy = y
            if rdy <= y:
                rdy = y+1
    return [lux, luy, rdx, rdy]

'''
진심으로 그냥 이렇게 푸는 거였구나.
'''