import pygame
from pygame.draw import *
from random import randint, uniform
import math


pygame.init()

FPS = 60

#Screen dimensional
SCRX = 900
SCRY = 600

screen = pygame.display.set_mode((SCRX, SCRY))


#Records
f = open("file1.txt",'r+')
Records = f.readlines()


#Scoring
Score=0

#Number of balls
number_of_balls = 5
#(number of balls)

#Number of square
number_of_squares = 3
#(number of squares)

#Counter
j=0
i=0

#Colors
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

#Function that draws squares
def new_cube(k):

    pygame.draw.polygon(screen, CCOL[k], [[CXCOR[k], CYCOR[k]], [CXCOR[k]+L[k], CYCOR[k]], [CXCOR[k]+L[k], CYCOR[k]+L[k]], [CXCOR[k], CYCOR[k]+L[k]]])

    t = A[k] / 10 * math.pi
    DX = CVY[k] * math.cos(t)
    DY = CVX[k] * math.sin(t)

    CXCOR[k] += int(DX)
    CYCOR[k] += int(DY)
        
    if CXCOR[k] >= SCRX-40:
        CVX[k] = -CVX[k] 
    if CXCOR[k] <= 0:
        CVX[k] = -CVX[k]
    
    if CYCOR[k] >= SCRY-50:
        CVY[k] = -CVY[k]-0.5
    if CYCOR[k] <= 0:
        CVY[k] = -CVY[k]-0.5
    A[k]+=1        
    
#Square center coords, and length
CXCOR = [randint(50,SCRX-50) for i in range(number_of_squares)]
CXCORS = CXCOR
CYCOR = [randint(50,SCRY-50) for i in range(number_of_squares)]
L = [randint(30,50) for i in range(number_of_squares)]

#Square counter
A = [0 for i in range(number_of_squares)]

#Square velocity
CVX = [3 * uniform(-2, 2) for i in range(number_of_squares)]
CVY = [3 * uniform(-2, 2) for i in range(number_of_squares)]

#Square color
CCOL =  [COLORS[randint(0, 5)] for i in range(number_of_squares)]



#Function that draws circles
def new_ball(k):
    circle(screen, COL[k], (XCOR[k], YCOR[k]), R[k])
    XCOR[k]+=int(VX[k])
    YCOR[k]+=int(VY[k])
    
    if XCOR[k] >= SCRX-30:
        VX[k] = -VX[k]
    if XCOR[k] <= 30:
        VX[k] = -VX[k]
    
    if YCOR[k] >= SCRY-30:
        VY[k] =- VY[k]
    if YCOR[k] <= 30:
        VY[k] =- VY[k]

#Circle center coords and radius
XCOR = [randint(50,SCRX-50) for i in range(number_of_balls)]
YCOR = [randint(50,SCRY-50) for i in range(number_of_balls)]
R = [randint(30,50) for i in range(number_of_balls)]

#Circle velocity
VX = [3*uniform(-2, 2) for i in range(number_of_balls)]
VY = [3*uniform(-2, 2) for i in range(number_of_balls)]

#Circle color
COL =  [COLORS[randint(0, 5)] for i in range(number_of_balls)]


pygame.display.update()
clock = pygame.time.Clock()
finished = False


#Main function
while not finished:
    clock.tick(FPS)
           
    for event in pygame.event.get(): 
        pos = pygame.mouse.get_pos()    
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            while j < number_of_balls:
                #Distance between click point and circle center (squared)
                h = (XCOR[j] - pos[0])**2 + (YCOR[j] - pos[1])**2
                #Circle radius squared
                rh = R[j]**2 
                if h <= rh:
                    print('Gotcha!')
                    Score += 1
                    XCOR[j] = randint(50,SCRX-50)
                    YCOR[j] = randint(50,SCRY-50)
                    VX[j] = 3*uniform(-2, 2)
                    VY[j] = 3*uniform(-2, 2)
                    COL[j] = COLORS[randint(0, 5)]
                    
                j+=1
            j=0 
            
            while j < number_of_squares:
                if pos[0]>CXCOR[j] and pos[1]>CYCOR[j] and pos[0]<CXCOR[j]+L[j] and pos[1]<CYCOR[j]+L[j]:
                    print('Gotcha!')
                    Score += 5

                    CXCOR[j] = randint(50,SCRX-50)
                    CYCOR[j] = randint(50,SCRY-50)
                    L[j] = randint(30,50)
                    
                    A[j] = 0
                    CVX[j] = 10 * uniform(-2, 2)
                    CVY[j] = 10 * uniform(-2, 2)
                    
                    CCOL[j] = COLORS[randint(0, 5)]
                j+=1
            j=0  

    f1 = pygame.font.Font(None, 36)  
    text1 = f1.render('Scoring: ' + str(Score), 1, (180, 0, 0))       
    screen.blit(text1, (SCRX-200, 10)) 
    
    f1 = pygame.font.Font(None, 36)  
    text1 = f1.render('Previous records:', 1, (180, 0, 0))       
    screen.blit(text1, (10, 10))
    
    f1 = pygame.font.Font(None, 36)  
    text1 = f1.render(Records[0], 1, (180, 0, 0))       
    screen.blit(text1, (10, 40))
    
    f1 = pygame.font.Font(None, 36)  
    text1 = f1.render(Records[1], 1, (180, 0, 0))       
    screen.blit(text1, (10, 70))
    
    f1 = pygame.font.Font(None, 36)  
    text1 = f1.render(Records[2], 1, (180, 0, 0))       
    screen.blit(text1, (10, 100))
    
    while j < number_of_balls:
        new_ball(j)
        j+=1
    j=0 
 
    while j < number_of_squares:
        new_cube(j)
        j+=1
    j=0   


    pygame.display.update()
    screen.fill(BLACK)
  
Records.append(Score)

for i in range(len(Records)):
    Records[i] = int(Records[i])
Records.sort(reverse = True)

for i in range(len(Records)):
    Records[i] = str(Records[i])
    
f.seek(0)

for  el in Records:
    f.write(el + '\n')
    
pygame.quit()       