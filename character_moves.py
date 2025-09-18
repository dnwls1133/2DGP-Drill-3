from pico2d import *

open_canvas()

glass = load_image('grass.png')
character = load_image('character.png')
width = get_canvas_width()
height = get_canvas_height()
# 시작점을 설정하자
# 캐릭터가 처음 서있는 위치이자 모든 운동의 시작점이자 종점
base_x = width / 2
base_y = 90
def triangle_move():
    clear_canvas_now()
    glass.draw_now(400, 30)
    character.draw_now(base_x, base_y)
    delay(0.5)
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