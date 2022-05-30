import pygame #파이게임 패키지 불러오기
import sys # 파이썬 인터프리터 제어
import time

#로켓 이미지와 길이, 높이 불러오기
imgShuttle = pygame.image.load("DogeRocket.png")
img_width = imgShuttle.get_width()
img_height = imgShuttle.get_height()

#소행성 사진 생성
imgasteroid = pygame.image.load("DogeCoin.png")
imgater_width = imgasteroid.get_width()
imgater_height = imgasteroid.get_height()

#스크린 사이즈와 측정을 위한 시작 시간 생성
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 480
START_TIME = time.time()

pygame.init()
pygame.display.set_caption("DogeCoin Avoidance Game") # 창 제목 설정

#지정한 크기의 창 생성
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
myFont = pygame.font.SysFont("arial", 30, True, False)
clock = pygame.time.Clock()

#소행성 5개 생성
loc_rock = [[100,100],
            [150,300],
            [300,150],
            [250,250],
            [500,300]]
rocks_list = []
size_rock = 20

#속도 지정
vel=[[5,5],
    [5,-5],
    [-5,-5],
    [-5,5],
    [4,-4]]

#도지 우주선 생성
loc_ship = [SCREEN_WIDTH/2,SCREEN_HEIGHT/2]
size_ship = 15

#폰트 설정
myFont = pygame.font.SysFont("arial", 30, True, False)

#소행성에 닿았을 때 게임 종료
def collision_check(loc_rock,size_rock,loc_ship,size_ship):
    dist_x = loc_rock[0] - loc_ship[0]
    dist_y = loc_rock[1] - loc_ship[1]
    dist = (dist_x**2 + dist_y**2)**(0.5)
    
    if dist < (size_rock + size_ship):
        collision_text = myFont.render("Collision!", 1, (255,0,0))
        screen.blit(collision_text, [20,20])
        print("\n"*10)
        print("-"*48,"+")
        print(" "*48,"|")
        print(f"소행성 충돌!! 도지로켓이 생존한 시간 : {time_diff[:4]} 초   |")
        print(" "*48,"|")
        print("-"*48,"+\n")
        pygame.quit() # pygame 종료
        sys.exit()
        
while True:
    clock.tick(30)
    screen.fill((0,0,0))

    #소행성 표시
    for i in range(len(loc_rock)):
        pygame.draw.circle(screen, 	(234, 215, 42), loc_rock[i], size_rock,2)
        x = loc_rock[i][0] - imgater_width/2
        y = loc_rock[i][1] - imgater_height/2
        screen.blit(imgasteroid,(x,y))
    keys = pygame.key.get_pressed()      
    
    if keys[pygame.K_LEFT]:
        loc_ship[0] -=3
        
    if keys[pygame.K_RIGHT]:
        loc_ship[0] +=3
        
    if keys[pygame.K_UP]:
        loc_ship[1] -=3
        
    if keys[pygame.K_DOWN]:
        loc_ship[1] +=3
    
    if keys[pygame.K_q]:
        pygame.quit()
        sys.exit()
    
    for event in pygame.event.get(): #발생한 입력 event 목록의 event 마다 검사
        if event.type == pygame.QUIT: #event의 type이 QUIT에 해당할 경우
            pygame.quit() # pygame 종료
            sys.exit()
    
    for i in range(len(loc_rock)): #소행성 개수만큼 만복

        #소행성 움직이기 (소행성 위치 + 속도를 반복적으로 추가하여)
        loc_rock[i][0]+=vel[i][0]
        loc_rock[i][1]+=vel[i][1]

        #소행성이 벽면에 닿을 경우 진행 방향으로 반대로 이동
        if loc_rock[i][0] >= SCREEN_WIDTH:
            vel[i][0] = -vel[i][0]
            
        if loc_rock[i][0] <= 0:
            vel[i][0] = -vel[i][0]       
        
        if loc_rock[i][1] >= SCREEN_HEIGHT:
            vel[i][1] = -vel[i][1]
        
        if loc_rock[i][1] <= 0:
            vel[i][1] = -vel[i][1]

        #소행성 충돌 시
        collision_check(loc_rock[i], size_rock, loc_ship, size_ship)

        # 게임 진행 시간 표시
        time_diff = str(time.time()-START_TIME)
        currentTime_text = myFont.render(time_diff[:4],1,(255,255,255))
        screen.blit(currentTime_text, [SCREEN_WIDTH-70,20])

    #도지 우주선
    pygame.draw.circle(screen,(255,255,255),loc_ship, size_ship,1)
    x = loc_ship[0] - img_width/2
    y = loc_ship[1] - img_height/2
    screen.blit(imgShuttle,(x,y))

    pygame.display.update() # 화면 업데이트