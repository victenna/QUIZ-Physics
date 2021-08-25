import pygame,sys,time,math
pygame.init()
screen = pygame.display.set_mode((1105,800))
clock = pygame.time.Clock()
X, Y = 100, 100
smallfont = pygame.font.SysFont('Corbel',35)

Q=10
x,y=[340,500,339,633,402,628,402,430,430,875],[270,370,222,305,548,650,525,650,550,300]
images=[0]*Q
img=[0]*Q
rect=[0]*Q
for m in range(10):
    folder='quest5_images/'
    name='image'
    m1=str(m)
    ext='.png'
    images[m]=folder+name+m1+ext



def base(i,scalex,scaley,angle):
    img[i]=pygame.image.load(images[i])
    img[i]=pygame.transform.scale(img[i],(scalex,scaley))
    img[i]=pygame.transform.rotate(img[i],angle)
    rect[i]=img[i].get_rect(center=(x[i],y[i]))
    screen.blit(img[i],rect[i])
delta,delta1=1,0
t,i,a,angle1,angle2=0,-1,0,-40,0
X1,Y1=480,592
plotPoints=[(480,592),(496,592.1)]
dX1=8

BLACK = (0, 0, 0)
font1 = pygame.font.SysFont(None, 25)
message1 = font1.render('Тело обьемом 2 Метра кубических ', True, BLACK)
message2 = font1.render('погружено в воду.', True, BLACK)
message3 = font1.render('Найдите Архимедову силу,', True, BLACK)
message4 = font1.render('действующую на тело.', True, BLACK)
message5 = font1.render('Введите только цифровой результат.', True, BLACK)

BLACK = (0, 0, 0)
RED = (255, 0, 0)
a=1

font0 = pygame.font.SysFont(None, 70)
question5 = font0.render('Вопрос 5', True, 'navy')
#---------------------------------------------    вставка1
text = ''
push=0
A=0
answer=0
s,s1,s2=0,0,0
pi=math.pi

custom_cursor=pygame.image.load('cursor.png')
font = pygame.font.SysFont(None, 48)
wrong = font.render('Ответ неправильный', True, RED)
right = font.render('Ответ правильный', True, RED)
question_number=5
score5=0
#-----------------------------------------------  end of 1
while True:
    
    screen.fill('white')
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
            
    if answer==20:
        screen.blit(right,(40,50))
        s1=s1+1
        print('s1=',s1)
        if s1==199:
            score5=1
        if s1==200:
            break
    if answer!=20 and answer!=0:
        screen.blit(wrong,(40,50))
        s1=s1+1
        if s1==200:
            break
            
    if a==1:
        if y[0]<420:
            y[0]=y[0]+delta
            y[6]=y[6]+delta
            print('y[0]=',y[0])
            y[2]=y[2]+delta
        else: delta=0
        
        base(1,1000,800,0)
        base(0,270,515,0)
        base(2,37,162,angle1);
        base(3,37,162,angle2)
        base(5,162,21,0)
        base(6,100,145,0)

        if y[0]>340:
            if y[0]>350:
                y[5]=y[5]-delta/3
            if y[0]>350 and y[0]<420:
                angle1=angle1+1/5
                angle2=angle2-1/5
                y[4]=y[4]+delta*0.5
                delta1=delta1+delta
                base(4,20,delta1,0)
            if y[0]>419:
                base(4,21,delta1,0)
                base(7,50,50,0)
                base(8,50,50,0)
                base(9,250,307,0)
            i=i+1
            X1=X1+dX1
            Y1=592+(dX1*i)*(dX1*i)*0.002
            if i<25:
                plotPoints.append([X1,Y1])
    if y[0]<420:
        pygame.draw.lines(screen,(44,207,255),False,plotPoints,5)

    font2 = pygame.font.SysFont(None, 48)
    text_surface = font2.render(text, True, RED)
    screen.blit(text_surface, (880,55))
    pygame.draw.rect(screen, BLACK,[850,50,130,40],4)
    screen.blit(custom_cursor,(870,50))
    screen.blit(message1,(650,480))
    screen.blit(message2,(650,505))
    screen.blit(message3,(650,530))
    screen.blit(message4,(650,555))
    screen.blit(message5,(650,580))
    screen.blit(question5,(800,750))
    clock.tick(100)
    pygame.display.update()      