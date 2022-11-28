import random
import turtle

t_list = [] # 벌레 객체 리스트
t_color = ["red", "orange", "gold", "green", "blue", "indigo", "violet", "black", "gray", "aqua"]

class Result: # 결과 객체용 클래스
    tile = [] # 각 타일별 벌레가 멈추었던 횟수를 저장하는 2차원 배열
    count = 0 # 바퀴벌레가 총 움직인 횟수

#############################################################

def Make_tile(m):
    d = 50
    turtle.hideturtle()
    turtle.color("lightgray")  # 격자의 색상: 회색
    turtle.shape("turtle")
    turtle.speed(0)

    for i in range(m):
        for j in range(m - 1):
            turtle.forward(50)
        turtle.penup()
        turtle.goto(0, d)
        turtle.pendown()
        d += 50

    turtle.penup()
    turtle.goto(0, 0)
    turtle.left(90)
    d = 50
    turtle.pendown()

    for i in range(m):
        for j in range(m - 1):
            turtle.forward(50)
        turtle.penup()
        turtle.goto(d, 0)
        turtle.pendown()
        d += 50

#############################################################

def Make_bugs(num):
    for i in range(num): # 벌레 객체 생성 및 설정 후 삽입
        t = turtle.Turtle()
        t.speed(2)
        t.pensize(3)
        t.shape("circle")
        t.color(random.choice(t_color))
        t_list.append(t)

#############################################################

def Drunken_bug(m,num, bug_loc, bar_loc):

    Make_tile(m)

    Make_bugs(num)

    t_check_list = [0 for i in range(num)]  # 술집 방문 확인 리스트

    tile = [[0 for i in range(m)] for j in range(m)] # 타일별 멈춘 횟수 초기값 0으로 세팅하여 생성
    new_bug = [] # 편의상 임시 변수(벌레의 이동 후의 새로운 좌표를 나타냄)
    count = 0 # 총 이동 횟수 저장용 변수
    bar_count = 0 # 술집 방문 횟수 내역

    idx = 0 # 벌레 인덱스
    for i in t_list:  # 초기 벌레 위치시키기
        i.penup()
        i.goto(bug_loc[idx][0] * 50, bug_loc[idx][1] * 50)
        i.pendown()
        tile[bug_loc[idx][0]][bug_loc[idx][1]] = 1  # 일단 시작 위치에도 멈춘 횟수 1을 줌
        idx += 1

    while 1:
        idx = 0 # 벌레 인덱스
        for i in bug_loc:
            if i == bar_loc:
                if t_check_list[idx] == 0:
                    bar_count += 1
                    t_check_list[idx] = 1
                    idx += 1
                    continue
                elif t_check_list[idx] == 1:
                    idx += 1
                    continue

            while 1:
                random_dx = random.choice((-1, 0, 1,))
                random_dy = random.choice((-1, 0, 1,))
                new_bug = [bug_loc[idx][0] + random_dx, bug_loc[idx][1] + random_dy]  # 벌레를 랜덤 이동시킴

                if not (random_dx == 0 and random_dy == 0):  # 랜덤 이동의 유효성을 평가
                    if new_bug[0] > -1 and new_bug[0] < m and new_bug[1] > -1 and new_bug[1] < m:
                        count = count + 1
                        break  # 유효한 이동이 나오면 랜덤화 중단

            bug_loc[idx] = [new_bug[0], new_bug[1]]  # 실제로 벌레를 이동 시킴
            tile[bug_loc[idx][0]][bug_loc[idx][1]] = tile[bug_loc[idx][0]][bug_loc[idx][1]] + 1  # 이동한 타일에 대하여 멈춘 횟수를 업데이트
            t_list[idx].goto(bug_loc[idx][0] * 50, bug_loc[idx][1] * 50)
            idx += 1

        if bar_count == num:
            break

    result = Result()
    result.tile = tile
    result.count = count

    return result

#############################################################

# 술집 위치 램덤 선택
bar_count = 0 #술집 찾은 횟수
bar_loc = [random.randrange(0, 5), random.randrange(0, 5)] #술집 위치 -> 사용자 입력: 크기
print("Bar Location: ", bar_loc, "\n")

#초기 벌레 위치 배열
bug_loc = [[random.randrange(0, 5), random.randrange(0, 5)] for i in range(1)] #사용자 입력: 크기 & 벌레 수

bug_test = Drunken_bug(5, 1, bug_loc, bar_loc)  #사용자 입력: 크기 & 벌레 수
for i in bug_test.tile:
    print (i)

print ("Total Count: %d" % (bug_test.count))

turtle.done()