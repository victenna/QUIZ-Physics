#Question 2 Колесо с горы
import pygame,sys,math
pygame.init()
screen = pygame.display.set_mode([1105,800])
img = pygame.image.load('quest2_images/hoop1.png')
background=pygame.image.load('quest2_images/background6.png')

arrow_img=pygame.image.load('quest2_images/arrow.png')
arrow_img=pygame.transform.scale(arrow_img,(90,30))

img1=pygame.transform.scale(img,(75,75))# заявляю изображение
rect=screen.get_rect()
clock = pygame.time.Clock()

BLACK = (0, 0, 0)
RED = (255, 0, 0)
X,Y=102,681
delta=5
angle=0
N=0
i=-1

font0 = pygame.font.SysFont(None, 70)
question2 = font0.render('Вопрос 2', True, 'gold')
score2=0
answer=0

font1 = pygame.font.SysFont(None, 32)
message1 = font1.render('Колесо скатывается с горы высотой H=10м.', True, BLACK)
message2 = font1.render('Определите скорость колеса', True, BLACK)
message3 = font1.render('у подножия горы', True, BLACK)
message4 = font1.render('Введите только цифровой результат,', True, BLACK)
message5 = font1.render('округлив его до ближайшего целого', True, BLACK)

#--------------------------------------------- вставка 1
text = ''
#push=0
pi=math.pi
custom_cursor=pygame.image.load('cursor.png')
s1=0
font = pygame.font.SysFont(None, 48)
wrong = font.render('Ответ неправильный', True, RED)
right = font.render('Ответ правильный', True, RED)
question_number=2

#--------------------------------------------------------
while True:
    
    if question_number==2:
    
        i=i+1
        i1=i%220
        i2=math.pow(i1,1/2)
        angle=angle+5
        screen.blit(background,(-105,-65))
        
    #--------------------------------------------------------вставка 2

        txt_surface = font.render(text, True, 'red')
        screen.blit(txt_surface, (880,55))
        pygame.draw.rect(screen, 'black',[850,50,130,40],4)
        screen.blit(custom_cursor,(870,50))  
    #--------------------------------------------------------
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    #-------------------------------------------------------- вставка 3
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode
                    A=text
                if event.key == pygame.K_RETURN:
                        
                        answer=int(A)
                        text=''
                    
    if answer==10:
        #time.sleep(0.1)
        
        screen.blit(right,(400,200))
        s1=s1+1
        print('s1=',s1)
        if s1==199:
            score2=1
        if s1==200:
            break
            #import quiz_question3
            
    if answer!=10 and answer!=0:
        screen.blit(wrong,(400,200))
        s1=s1+1
        if s1==200:
            break
            #import quiz_question3
    #--------------------------------------------------------
    X=170+i1*delta
    if i1<120:
        Y=360-200*math.cos(pi*i1*delta/700)
        YY=360-200*math.cos(pi*(i1+1)*delta/700)
        angle1=(YY-Y)*9
        if i1==119:
            angle1=0
        Y1=Y
        arrow_img1=pygame.transform.scale(arrow_img,((1+i1),30))
        arrow_img2=pygame.transform.rotate(arrow_img1,-angle1)
        rect_arrow=arrow_img2.get_rect(center=(X,Y))
        i3=1+i1
        
    if i1>118:
        Y=Y1
        angle1=0
        rect_arrow=arrow_img2.get_rect(center=(X,Y1))
        
    img2=pygame.transform.rotate(img1,-angle*(1+i2)/5)
    rect=img2.get_rect(center=(X,Y))
    screen.blit(img2,rect)
    screen.blit(arrow_img2,rect_arrow)
    if i1==219:
        angle=0
        
    screen.blit(message1,(600,280))
    screen.blit(message2,(650,305))
    screen.blit(message3,(650,330))
    screen.blit(message4,(650,355))
    screen.blit(message5,(650,380))
    screen.blit(question2,(50,700))
    #print ('score2=',score2)
    pygame.display.update()
    clock.tick(60)