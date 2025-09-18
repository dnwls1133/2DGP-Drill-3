from pico2d import *

import math

open_canvas()

glass = load_image('grass.png')
character = load_image('character.png')
width = get_canvas_width()
height = get_canvas_height()
# 시작점을 설정하자
# 캐릭터가 처음 서있는 위치이자 모든 운동의 시작점이자 종점
base_x = width / 2
base_y = 90

# 캐릭터가 현재 서있는 위치 정보
x = base_x
y = base_y

# 배경 그리기
def draw_boy_and_background(x : float, y : float):
    clear_canvas()
    glass.draw_now(400,30)
    character.draw_now(x,y)
    update_canvas()

# 캐릭터 오른쪽으로 이동
def move_right(amount):
    global x
    global y
    for i in range(0, amount, 50):
        draw_boy_and_background(x, y)
        x += 50
        delay(0.1)
    pass
def move_up(amount):
    global x
    global y
    for i in range(0,amount,50):
        draw_boy_and_background(x,y)
        y += 50
        delay(0.1)

    pass
# 캐릭터 아래로 이동
def move_down(amount):
    global x
    global y
    for i in range(0,amount,50):
        draw_boy_and_background(x,y)
        y -= 50
        delay(0.1)

    pass



# 캐릭터 좌상 대각선 이동
def move_diagonal_left_up(amount):
    global x
    global y
    theta = 60

    for i in range(0,amount,50):
        draw_boy_and_background(x, y)
        x = x - 50 * math.cos(math.radians(theta))
        y = y + 50 * math.sin(math.radians(theta))
        delay(0.1)
    pass

# 캐릭터 좌하 대각선 이동
def move_diagonal_right_down(amount):
    global x
    global y
    theta = 300
    for i in range(0,amount,50):
        draw_boy_and_background(x, y)
        x = x - 50 * math.cos(math.radians(theta))
        y = y + 50 * math.sin(math.radians(theta))
        delay(0.1)
    pass

def triangle_move():

    move_right(200)
    move_diagonal_left_up(400)
    move_diagonal_right_down(400)
    move_right(200)

    pass

def rectangle_move():
    pass

def circle_move():
    pass


# 삼각 운동
# 사각 운동
# 원 운동
# 번갈아가며 무한 반복
# fill here
while True:
    triangle_move()
    rectangle_move()
    circle_move()
    pass

close_canvas()