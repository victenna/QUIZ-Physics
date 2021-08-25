#Quesion 3 Брусок катится с наклонной плоскости
import pygame,sys,math
pygame.init()
screen = pygame.display.set_mode((1105,800))
rect=screen.get_rect()
Main_image=pygame.image.load('quest3_images/Image1.png')
arrow_img0=pygame.image.load('quest3_images/arrow7_.png')
arrow_img1=pygame.image.load('quest3_images/arrow5_.png')
brick_img1=pygame.image.load('quest3_images/brick4.png')
timer=pygame.time.Clock()
screen.fill('violet')
teta,delta=5,0 
X0,Y0=100,1000
X1,Y1=900,Y0
Point0=(X0,Y0)
Width=5
dX=0
q=1

BLACK = (0, 0, 0)
RED = (255, 0, 0)

font0 = pygame.font.SysFont(None, 70)
question3 = font0.render('Вопрос 3', True, 'gold')
#---------------------------------------------    вставка1
text = ''
push=0
A=0
answer=0
s=0
s1,s2=0,0
pi=math.pi
custom_cursor=pygame.image.load('cursor.png')
font = pygame.font.SysFont(None, 48)
wrong = font.render('Ответ неправильный', True, RED)
right = font.render('Ответ правильный', True, RED)
question_number=3
score3=0
#-----------------------------------------------
while True:
    if question_number==3:
        screen.fill('violet')
        teta=teta+0.5*q
        if teta>30:
            q=0
        X2,Y2=X0,Y0-(X1-X0)* math.tan(3.14159/180*teta)
        X3,Y3=X0+delta,Y2+delta*math.tan(teta*3.14159/180)
        dX=dX+1
        if teta<30:
            dX=0
        X=X3+dX
        Y=Y3+dX*math.tan(teta*3.14159/180)

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
#--------------------------------------------------------- вставка 2
                    
                if event.type == pygame.KEYDOWN:
                    
                    if event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
                        A=text
                    if event.key == pygame.K_RETURN:
                        answer=int(A)
                        text=''
        if answer==17:
            screen.blit(right,(400,100))
            s1=s1+1
            print('s1=',s1)
            if s1==199:
                score3=1
            if s1==200:
                break
        if answer!=17 and answer!=0:
            screen.blit(wrong,(400,100))
            s1=s1+1
            if s1==200:
                break

        font2 = pygame.font.SysFont(None, 48)
        text_surface = font2.render(text, True, RED)
        screen.blit(text_surface, (880,55))
        pygame.draw.rect(screen, BLACK,[850,50,130,40],4)
        screen.blit(custom_cursor,(870,50))
    #------------------------------------------------------ end of 2                 
        rect=Main_image.get_rect(center=(550,400))
        screen.blit(Main_image,rect)
        brick_img2=pygame.transform.rotate(brick_img1,-teta)
        arrow_img2=pygame.transform.rotate(arrow_img1,-teta)
        rect_brick=brick_img2.get_rect(topleft=(X,Y-42))
        rect_arrow0=arrow_img0.get_rect(center=(X+55,Y+10))
        rect_arrow=arrow_img2.get_rect(center=(X+55,Y+10))
        Point1=(X1,Y1)
        Point2=(X2,Y2)
        pygame.draw.polygon(screen, 'blue', (Point0,Point1,Point2))
        screen.blit(brick_img2,rect_brick)
        screen.blit(arrow_img0,rect_arrow0)
        screen.blit(arrow_img2,rect_arrow)
        if X>700:
            dX,teta,q=0,10,1
        screen.blit(question3,(800,750))
        timer.tick(50)
        pygame.display.update()
    
