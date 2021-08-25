#QUIZ START
import pygame,sys,math
quizz=pygame.image.load('quiz2.png')
clock = pygame.time.Clock()
 
BLACK = (0, 0, 0)
RED = (255, 0, 0)

pygame.init()
screen = pygame.display.set_mode((1105,800))
#screen.fill('purple')
rect=screen.get_rect()

global SCORE
from Quiz_control import SCORE
print('Total Score',SCORE)

font2 = pygame.font.SysFont(None, 55)
total1 = font2.render('Число правильных ответов из пяти вопросов=', True, 'white')
total2 = font2.render(str(SCORE), True, 'white')
while True:
    
    screen.blit(quizz,(0,0))
    screen.blit(total1,(80,597))
    screen.blit(total2,(960,600))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    clock.tick(100)
    pygame.display.update()  