import pygame
import sys
from pygame.locals import QUIT
import random


pygame.init()

score=0
font=pygame.font.SysFont("Arial", 30)

screen= pygame.display.set_mode((640,640))
pygame.display.set_caption("My Fun Game")

clock=pygame.time.Clock()

red=(255,0,2)

rabit_img=pygame.image.load("rabbit.png")
rabit_img=pygame.transform.scale(rabit_img,(50,50))

rabbit=pygame.Rect(screen.get_width ()//2, screen.get_height() -60, 50, 50)
rabbit_speed_x=0
rabbit_speed_y=-0
food = pygame.Rect(random.randint(0, screen.get_width()-30), -30, 30, 30)
food_speed = 4


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rabbit_speed_x = -5
            elif event.key == pygame.K_RIGHT:
                rabbit_speed_x = 5

        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                rabbit_speed_x = 0

    rabbit.x += rabbit_speed_x
    rabbit.y += rabbit_speed_y

    if rabbit.x < 0:
        rabbit.x = 0
    if rabbit.x > screen.get_width() - rabbit.width:
        rabbit.x = screen.get_width()- rabbit.width

    food.y += food_speed

    if food.y > screen.get_height() or rabbit.colliderect(food):
        if rabbit.colliderect(food):
            score += 1
        food.x = random.randint(0, screen.get_width() - food.width)
        food.y = -30


    screen.fill((0,0 ,0 )) 

        
    screen.blit(rabit_img, rabbit)  # Draw the rabbit image
    pygame.draw.rect(screen, red, food)
    score_text = font.render(f"Score: {score}", True, (0, 0, 255))  # blue color
    score_place=score_text.get_rect(topright=(screen.get_width()-10, 10))
    screen.blit(score_text, score_place)

    pygame.display.flip()
    clock.tick(60)



     
    
