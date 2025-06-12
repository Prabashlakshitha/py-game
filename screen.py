import pygame
import sys
from pygame.locals import QUIT
import random
WIDTH = 640

pygame.init()

screen= pygame.display.set_mode((640,640))
pygame.display.set_caption("My Fun Game")

clock=pygame.time.Clock()

red=(255,0,2)

rabit_img=pygame.image.load("rabbit.png")
rabit_img=pygame.transform.scale(rabit_img,(50,50))

rabiit=pygame.Rect(200, 600, 50, 50)
rabiit_speed_x=0
rabiit_speed_y=1

food = pygame.Rect(random.randint(0, screen.get_width()-30), -30, 30, 30)
food_speed = 2


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rabiit_speed_x = -5
            elif event.key == pygame.K_RIGHT:
                rabiit_speed_x = 5

        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                rabiit_speed_x = 0

    rabiit.x += rabiit_speed_x
    rabiit.y += rabiit_speed_y

    if rabiit.x < 0:
        rabiit.x = 0
    if rabiit.x > WIDTH - rabiit.width:
        rabiit.x = WIDTH - rabiit.width

    food.y += food_speed

    if food.y > screen.get_height() or rabiit.colliderect(food):
        food.x = random.randint(0, WIDTH - food.width)
        food.y = -3


    screen.fill((255, 255, 255)) 

        
    screen.blit(rabit_img, rabiit)  # Draw the rabbit image
    pygame.draw.rect(screen, red, food)

    pygame.display.flip()
    clock.tick(60)



     
    
