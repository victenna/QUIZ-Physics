#QUIZ START
import pygame,sys,math
quiz=pygame.image.load('quiz1.png')
clock = pygame.time.Clock()
 
BLACK = (0, 0, 0)
RED = (255, 0, 0)

pygame.init()
screen = pygame.display.set_mode((1105,800))
screen.fill('purple')
rect=screen.get_rect()

s=0
while s<402:
    s=s+1
    print('s=',s)
    if s==400:
        #import Quiz_control
        break
    screen.fill('purple')
    rect=quiz.get_rect(center=(550,400))
    screen.blit(quiz,rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    pygame.display.update()
    clock.tick(40)

