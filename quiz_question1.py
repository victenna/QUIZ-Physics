#Question 1 Машина на чертовом колесе
import pygame,sys,math,time
bg11=pygame.image.load('quest1_images/loop_.png')
car=pygame.image.load('quest1_images/car.png')
clock = pygame.time.Clock()
 
BLACK = (0, 0, 0)
RED = (255, 0, 0)
teta=-90
N=0
X0,Y0=600,395
R=225

pygame.init()
screen = pygame.display.set_mode((1105,800))
rect=screen.get_rect()

font0 = pygame.font.SysFont(None, 70)
question1 = font0.render('Вопрос 1', True, 'blue')

score1=0
#global score1
#-------------------------------------------------------------Вставка 1
text = ''
push=0
A=0
answer=0

pi=math.pi
custom_cursor=pygame.image.load('cursor.png')
font = pygame.font.SysFont(None, 48)
wrong = font.render('Ответ неправильный', True, RED)
right = font.render('Ответ правильный', True, RED)
global question_number
question_number=1
s1=0

#------------------------------------------------------------- Вставка 1(конец)
while True:
    

    if question_number==1:
        teta=teta+2
        rect=bg11.get_rect(center=(600,400))
        screen.blit(bg11,rect)

        X,Y=X0+R*math.cos(pi*teta/180),Y0-R*math.sin(pi*teta/180)
        car=pygame.transform.scale(car,(110,100))
        car1=pygame.transform.rotate(car,teta+90)
        rect=car1.get_rect(center=(X,Y))
        screen.blit(car1,rect)
#---------------------------------------------        
    
    txt_surface = font.render(text, True, 'red')
    screen.blit(txt_surface, (880,55))
    pygame.draw.rect(screen, 'black',[850,50,130,40],4)
    screen.blit(custom_cursor,(870,50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                text = text[:-1]
            else:
                text += event.unicode
                A=text
            if event.key == pygame.K_RETURN:
                    answer=int(A)
                    text=''
#----------------------------------------------------
    if answer==7:
        #print ('score1=',score1)
        #time.sleep(0.1)
        
        screen.blit(right,(400,300))
        s1=s1+1
        print('s1=',s1)
        if s1==199:
            score1=1
        if s1==200:
            #print ('score1=',score1)
            
            #import quiz_question2
            break
            
    if answer!=7 and answer!=0:
        screen.blit(wrong,(400,300))
        s1=s1+1
        if s1==200:
            break
            #import quiz_question2
                
#---------------------------------------------------
    #if s1==200:
        #print ('score1=',score1)
        #break
    #print ('score1=',score1)
    screen.blit(question1,(100,750))
    pygame.display.update()
    clock.tick(40)



