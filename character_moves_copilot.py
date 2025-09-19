from pico2d import *
import math

# 캔버스 초기화
open_canvas()

# 리소스 로드
grass_image = load_image('grass.png')
boy_sprite = load_image('character.png')

# 화면 크기 정보
screen_width = get_canvas_width()
screen_height = get_canvas_height()

# 기준점 x, y (시작점이자 모든 움직임의 중심점)
base_x = screen_width / 2
base_y = 90

# 현재 캐릭터 위치
current_x = base_x
current_y = base_y

def render_scene(x_pos, y_pos):
    """화면에 배경과 캐릭터를 그리는 함수"""
    clear_canvas()
    grass_image.draw_now(400, 30)
    boy_sprite.draw_now(x_pos, y_pos)
    update_canvas()

def horizontal_movement(distance, direction=1):
    """수평 이동 (direction: 1=오른쪽, -1=왼쪽)"""
    global current_x, current_y
    step_size = 50
    steps = abs(distance) // step_size

    for _ in range(steps):
        render_scene(current_x, current_y)
        current_x += step_size * direction
        delay(0.1)

def vertical_movement(distance, direction=1):
    """수직 이동 (direction: 1=위, -1=아래)"""
    global current_x, current_y
    step_size = 50
    steps = abs(distance) // step_size

    for _ in range(steps):
        render_scene(current_x, current_y)
        current_y += step_size * direction
        delay(0.1)

def 좌상단_대각선운동(distance):
    """좌상단 대각선 이동 (60도 각도)"""
    global current_x, current_y
    angle = 60
    step = 50
    steps = distance // step

    for _ in range(steps):
        render_scene(current_x, current_y)
        current_x -= step * math.cos(math.radians(angle))
        current_y += step * math.sin(math.radians(angle))
        delay(0.1)

def diagonal_right_down_movement(distance):
    """우하단 대각선 이동 (300도 각도)"""
    global current_x, current_y
    angle = 300
    step = 50
    steps = distance // step

    for _ in range(steps):
        render_scene(current_x, current_y)
        current_x -= step * math.cos(math.radians(angle))
        current_y += step * math.sin(math.radians(angle))
        delay(0.1)

def triangle_pattern():
    """삼각형 패턴 이동"""
    horizontal_movement(200, 1)  # 오른쪽
    좌상단_대각선운동(400)  # 좌상단 대각선
    diagonal_right_down_movement(400)  # 우하단 대각선
    horizontal_movement(200, 1)  # 오른쪽

def rectangle_pattern():
    """사각형 패턴 이동"""
    horizontal_movement(200, 1)  # 오른쪽
    vertical_movement(400, 1)    # 위
    horizontal_movement(400, -1) # 왼쪽
    vertical_movement(400, -1)   # 아래
    horizontal_movement(200, 1)  # 오른쪽

def circular_pattern():
    """원형 패턴 이동"""
    global current_x, current_y
    center_x = screen_width / 2
    center_y = (screen_height / 2 + 90) / 1.5
    radius = center_y - 90

    # 360도에서 0도까지 1도씩 감소하며 원 그리기
    for angle in range(360, 0, -1):
        render_scene(current_x, current_y)
        current_x = center_x + radius * math.cos(math.radians(angle - 90))
        current_y = center_y + radius * math.sin(math.radians(angle - 90))
        delay(0.01)

# 메인 실행 루프 - 삼각형, 사각형, 원형 패턴을 무한 반복
while True:
    triangle_pattern()
    rectangle_pattern()
    circular_pattern()

close_canvas()
