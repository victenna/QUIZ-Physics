import pygame,math,sys
pygame.init()
timer = pygame.time.Clock()
screen = pygame.display.set_mode([1105,800])
screen.fill([68,242,244])
keep_going = True
img = pygame.image.load('quest4_images/image1.png')  #image1
img1=pygame.transform.rotate(img,90)
imag,imag1,imag2=[0]*400,[0]*400,[0]*400
    
for i in range(400):
    i1=i%400
    i1=int(i1)
    i2=150*math.sin(6.28*(i1/200))
    i2=int(i2)
    imag[i1]=pygame.transform.scale(img,(50,200+i2))
    imag1[i1]=pygame.transform.scale(img1,(200+i2,50))
    imag2[i1]=pygame.transform.scale(img1,(200-i2,50))

img_text1= pygame.image.load('quest4_images/image2.png')  #image2
img_text2= pygame.image.load('quest4_images/image3.png')   #image3
i=0
font1 = pygame.font.SysFont(None, 30)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
message1 = font1.render('Период колеания маятника с двумя пружинами Т1=', True, BLACK)
message2 = font1.render('введите цифру 1, если Т1>Т;', True, BLACK)
message3 = font1.render('введите цифру 2, если Т1<Т;', True, BLACK)
message4 = font1.render('введите цифру 3, если Т1=Т;', True, BLACK)

font0 = pygame.font.SysFont(None, 70)
question4 = font0.render('Вопрос 4', True, 'navy')
#---------------------------------------------    вставка1
text = ''

A=0
answer=0
s1=0
pi=math.pi
custom_cursor=pygame.image.load('cursor.png')
font = pygame.font.SysFont(None, 48)
wrong = font.render('Ответ неправильный', True, RED)
right = font.render('Ответ Правильный', True, RED)
question_number=4
score4=0


#-----------------------------------------------  end of 1
while True:
    if question_number==4:
        screen.fill([68,242,244])
        i=i+1
        i1=i%400
        i2=150*math.sin(6.28*(i1/200))
        i2=int(i2)

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
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
                    
        if answer==3:
            screen.blit(right,(600,250))
            s1=s1+1
            print('s1=',s1)
            if s1==199:
                score4=1
            if s1==200:
                break
        if answer!=3 and answer!=0:
            screen.blit(wrong,(600,250))
            s1=s1+1
            if s1==200:
                break
        
                   
            
            
        font2 = pygame.font.SysFont(None, 48)
        text_surface = font2.render(text, True, RED)
        screen.blit(text_surface, (880,55))
        pygame.draw.rect(screen, BLACK,[850,50,130,40],4)
        screen.blit(custom_cursor,(870,50))
#------------------------------------------------------ end of 2     
        screen.blit(img_text1,(800,80))                
        screen.blit(img_text2,(550,80))
#--------------------------------------------
         #Vertical spring
        pygame.draw.line(screen,'black',(240,102),(440,102),10)
        pygame.draw.rect(screen,'black',[290,290+i2,47.6,47.6])
        screen.blit(imag[i1],(300,100))
#----------------------------------------------------------------
        #Horizontal spring
        pygame.draw.line(screen,'black',(505,200),(505,385),10)
        pygame.draw.line(screen,'black',(505,380),(950,380),10)
        pygame.draw.rect(screen,'black',[688+i2*0.95,329,47.6,47.6])
        screen.blit(imag1[i1],(500,315))
#----------------------------------------------------------------
        #Horizontal spring  2 (part of double spring)
        pygame.draw.line(screen,'black',(205,570),(205,755),10)
        pygame.draw.line(screen,'black',(205,750),(630,750),10)
        pygame.draw.rect(screen,'black',[388+i2*0.95,690,60,60])
        screen.blit(imag1[i1],(200,690))
#----------------------------------------------------------------
        #Horizontal spring  3  (part of double spring)
        pygame.draw.line(screen,'black',(625,570),(625,755),10)
        screen.blit(imag2[i1],(430+i2*0.95,690,60,60))
#--------------------------------------------
        screen.blit(message1,(500,450))
        screen.blit(message2,(500,475))
        screen.blit(message3,(500,500))
        screen.blit(message4,(500,525))
        screen.blit(question4,(800,750))
        pygame.display.update()
        timer.tick(50)
        
        


           
