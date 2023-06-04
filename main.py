import pygame
from player import Player
from bullet import Bullet
import random as rnd
import math
import time

def collision(obj1, obj2):
    if math.sqrt( (obj1.pos[0] - obj2.pos[0]) ** 2 + (obj1.pos[1]- obj2.pos[1]) ** 2) < 20:
        return True
    return False

def draw_text(txt, size, pos, color):
    font = pygame.font.Font('freesansbold.ttf', size)
    r = font.render(txt, True, color)
    screen.blit(r, pos)    

pygame.init()
WIDTH, HEIGHT = 1000, 800
pygame.display.set_caption("총알 피하기") #title 제목 짓기
screen = pygame.display.set_mode((WIDTH, HEIGHT)) #pygame 화면크기 설정


player = Player(WIDTH/2, HEIGHT/2) #비행기 좌표 가운데 설정

#===============
#프레임 제한
clock = pygame.time.Clock()
FPS = 60
#===============
#총알 갯수
bullets = []
for i in range(10):
    bullets.append(Bullet(0, rnd.random()*HEIGHT, rnd.random()-0.5, rnd.random()-0.5))
    
#===============
#이미지 불러오기
image = pygame.image.load("player.png")
#이미지 출력
image = pygame.transform.scale(image, (128, 128))
#배경 이미지
bg_image = pygame.image.load('bg.jpg')
bg_pos = 0
#===============
#배경 음악
pygame.mixer.music.load('bgm.wav')
pygame.mixer.music.play(-1)
#===============
time_for_adding_bullets = 0 #시간 세기 총알 갯수 늘리는 데에 사용
start_time = time.time() #시작 시간
#===============
#mission1 총알에 맞았을 때 효과음 발생
explosion_sound = pygame.mixer.Sound('explosion.wav')

#==============

running = True #게임 시작
Life = 4 # 목숨 4개
gameover = False # 게임 오버
score = 0 # 

while running:
    dt = clock.tick(FPS) #60프레임으로 cpu 부담 줄이기
   
    time_for_adding_bullets += dt # 총알 수 늘리기
    if time_for_adding_bullets > 1000:
        bullets.append(Bullet(0, rnd.random()*HEIGHT, rnd.random()-0.5, rnd.random()-0.5))
        time_for_adding_bullets -= 1000
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #================
        #방향키로 비행기 움직이기
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.goto(-1, 0)
            elif event.key == pygame.K_RIGHT:
                player.goto(1,0)
            elif event.key == pygame.K_UP:
                player.goto(0,-1)
            elif event.key == pygame.K_DOWN:
                player.goto(0,1)
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.goto(1,0)
            elif event.key == pygame.K_RIGHT:
                player.goto(-1,0)
            elif event.key == pygame.K_UP:
                player.goto(0, 1)
            elif event.key == pygame.K_DOWN:
                player.goto(0,-1)
        #================
    if gameover:
        draw_text("GAME OVER", 100, (WIDTH/2 - 300, HEIGHT/2 - 50), (255, 255, 255))
        txt = (f"Time: {score:.2f} Bullets: {len(bullets)}")
        draw_text(txt, 32, (10,10), (255, 255, 255))
    else:
        score = time.time() - start_time
        txt = (f"Time: {score:.2f} Bullets: {len(bullets)}")
        draw_text(txt, 32, (10, 10), (255, 255, 255))
    screen.fill((0, 0, 0))
    bg_pos -= 0.01 *dt
    screen.blit(bg_image, (bg_pos, 0))
    player.update(dt, screen)
    player.draw(screen)
    
    
    for b in bullets:
        b.update_and_draw(dt, screen)
    
    for b in bullets:    
        if collision(player, b):
            time.sleep(2)
            running = False
            
    draw_text(f"Time: {time.time() - start_time:.2f}, Bullets: {len(bullets)}", 16, (10, 10), (255, 255, 255))
    pygame.display.update()
    if not gameover:
        for b in bullets:
            if collision(player, b):
                gameover = True
        time_for_adding_bullets += dt
        if time_for_adding_bullets > 1000:
            bullets.append(Bullet(0, rnd.random()*HEIGHT, rnd.random()-0.5, rnd.random()-0.5))
            time_for_adding_bullets -= 1000    