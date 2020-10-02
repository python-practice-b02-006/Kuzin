import pygame
import math


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (154, 154, 154)

ACATEAR = (223, 172, 136)
ACATNOSE = (255, 205, 172)
ACATEYE = (137, 172, 0)
ACATFUR = (201 , 114, 52)

BCATEAR = (244, 216, 216)
BCATNOSE = (211, 186, 186)
BCATEYE = (37, 213, 255)
BCATFUR = (108 , 93, 82)

BROWNGR = (84, 66, 0)
BROWNDAR = (129, 102, 0)
LIGHTBLUE = (214, 255, 231)
DBLUE = (136, 206, 223)

X = 487
Y = 690
NX = X/6
NY = Y/2.2

pygame.init()

scr = pygame.Surface([X,Y], pygame.SRCALPHA)
screen = pygame.display.set_mode([X,Y])

pygame.display.set_caption("Cats")

done = False
clock = pygame.time.Clock()   


#Window (Function that draws Windows) T_W(Window_xcor, Window_ycor_, Windows height, scr)
def T_W(x,y,h,screen):
    pygame.draw.polygon(screen, LIGHTBLUE, [[x, y], [x - h/math.sqrt(2), y], [x - h/math.sqrt(2), y+h], [x, y + h], [x, y]])
    
    x1 = (x - h/(12 * math.sqrt(2)))                                                        
    y1 = y + h/(12 * math.sqrt(2))
    x2 = x + (h/24) * (1/math.sqrt(2)) - h/(2 * math.sqrt(2))
    y2 = y + h/3 + h/(20 * math.sqrt(2))    
    pygame.draw.polygon(screen, DBLUE, [[x1,y1], [x1,y2], [x2,y2], [x2,y1], [x1,y1]]) 
    
    x1 = x - h/(24 * math.sqrt(2)) - h/(2 * math.sqrt(2))
    y1 = y + h/(12 * math.sqrt(2))
    x2 = x + h/(12 * math.sqrt(2)) - h/(math.sqrt(2))
    y2 = y + h/3 + h/(20 * math.sqrt(2))
    pygame.draw.polygon(screen, DBLUE, [[x1,y1], [x1,y2], [x2,y2], [x2,y1], [x1,y1]])     
    
    x1 = x - h/(24 * math.sqrt(2)) - h/(2 * math.sqrt(2))
    y1 = y + h/(24 * math.sqrt(2)) + h/3 + h/(20 * math.sqrt(2))
    x2 = x + h/(12 * math.sqrt(2)) - h/(math.sqrt(2))
    y2 = y + h - h/(20 * math.sqrt(2))
    pygame.draw.polygon(screen, DBLUE, [[x1,y1], [x1,y2], [x2,y2], [x2,y1], [x1,y1]]) 
    
    x1 = (x - h/(12 * math.sqrt(2)))
    y1 = y + h/(24 * math.sqrt(2)) + h/3 + h/(20 * math.sqrt(2))
    x2 = x + (h/24) * (1/math.sqrt(2)) - h/(2 * math.sqrt(2))
    y2 = y + h - h/(20 * math.sqrt(2))
    pygame.draw.polygon(screen, DBLUE, [[x1 , y1], [x1 , y2], [x2 , y2], [x2 , y1], [x1 , y1]]) 


#Cat (Function that draws cat) T_C(Cat_corx, Cat_cory, Cat_Length, Cat fur color, cat ear color, cat nose color, cat eye color, scr)  
def T_C(x,y,L,CATFUR,CATEAR,CATNOSE,CATEYE,screen): 
    #Tail
    surface = pygame.Surface([L/4, L/2], pygame.SRCALPHA)
    pygame.draw.ellipse(surface, CATFUR, [0, 0, L/6, L/2])
    surface_rot = pygame.transform.rotate(surface, 45)    
    screen.blit(surface_rot, [x + L/1.2, y + L/5])
    
    surface = pygame.Surface([L/4, L/2], pygame.SRCALPHA)
    pygame.draw.ellipse(surface, BLACK, [0, 0, L/6, L/2], 1)
    surface_rot = pygame.transform.rotate(surface, 45)    
    screen.blit(surface_rot, [x + L/1.2, y + L/5])
    
    #Body and paws
    pygame.draw.ellipse(screen, CATFUR, [x, y, L, L*3/5]) 
    pygame.draw.ellipse(screen, BLACK, [x, y, L, L*3/5], 1) 
    
    pygame.draw.ellipse(screen, CATFUR, [x - L/20, y + L/20, L/4, L/2])
    pygame.draw.ellipse(screen, BLACK, [x - L/20, y + L/20, L/4, L/2], 1) 

    pygame.draw.ellipse(screen, CATFUR, [x + L/5, y + L/2.3, L/3, L/5])
    pygame.draw.ellipse(screen, BLACK, [x + L/5, y + L/2.3, L/3, L/5], 1) 
    
    pygame.draw.ellipse(screen, CATFUR, [x + L/1.5, y + L/3, L/3, L/3])
    pygame.draw.ellipse(screen, BLACK, [x + L/1.5, y + L/3, L/3, L/3], 1) 
    
    pygame.draw.ellipse(screen, CATFUR, [x + L/1.5 + L/5, y + L/3 + L/6, L/7, L/3])
    pygame.draw.ellipse(screen, BLACK, [x + L/1.5 + L/5, y + L/3 + L/6, L/7, L/3], 1) 
        
    #Head
    pygame.draw.ellipse(screen, CATFUR, [x - L/10, y - L/20, L/2, L/2])
    pygame.draw.ellipse(screen, BLACK, [x - L/10, y - L/20, L/2, L/2], 1) 
    
    #Eyes
    pygame.draw.ellipse(screen, CATEYE, [x - L/36, y + L/10, L/6.5, L/6])
    pygame.draw.ellipse(screen, BLACK, [x - L/36, y + L/10, L/6.5, L/6], 1)
    pygame.draw.ellipse(screen, CATEYE, [x + L/6, y + L/10, L/6.5, L/6])
    pygame.draw.ellipse(screen, BLACK, [x + L/6, y + L/10, L/6.5, L/6], 1) 
    
    pygame.draw.ellipse(screen, BLACK, [x - L/36 + L/12, y + L/10, L/36, L/6.025])
    pygame.draw.ellipse(screen, BLACK, [x + L/6 + L/12, y + L/10, L/36, L/6.025])    
    
    alpha = 45
    
    surface = pygame.Surface([L/36, L/12], pygame.SRCALPHA)
    pygame.draw.ellipse(surface, WHITE, [0, 0, L/36, L/12])
    surface_rot = pygame.transform.rotate(surface, 45)    
    screen.blit(surface_rot, [x, y+L/10])   
    
    surface = pygame.Surface([L/36, L/12], pygame.SRCALPHA)
    pygame.draw.ellipse(surface, WHITE, [0, 0, L/36, L/12])
    surface_rot = pygame.transform.rotate(surface, 45)    
    screen.blit(surface_rot, [x+L/5, y+L/10])
    
    #Nose
    x1 = x + L/7 - L/40
    y1 = y + L/4
    x2 = x + L/7 + L/40
    y3 = y + L/4 + L/40
    x3 = x + L/7  
    pygame.draw.polygon(screen, CATNOSE, [[x1 , y1], [x2 , y1], [x3 , y3], [x1 , y1]])
    #Mouth
    pygame.draw.line(screen, BLACK, [x3 ,y3], [x3 ,y3+L/20], 1) 
    pygame.draw.line(screen, BLACK, [x3 ,y3 + L/20], [x3 - L/30 ,y3 + L/15], 1) 
    pygame.draw.line(screen, BLACK, [x3 ,y3 + L/20], [x3 + L/30 ,y3 + L/15], 1)
    pygame.draw.line(screen, BLACK, [x3 - L/30 ,y3 + L/15], [x3-L/15 ,y3 + L/20], 1) 
    pygame.draw.line(screen, BLACK, [x3 + L/30 ,y3 + L/15], [x3+L/15 ,y3 + L/20], 1)
    
    pygame.draw.line(screen, BLACK, [x3 - L/30 ,y3 + L/28], [x3-L/7 ,y3], 1) 
    pygame.draw.line(screen, BLACK, [x3 + L/30 ,y3 + L/28], [x3+L/7 ,y3], 1) 
    pygame.draw.line(screen, BLACK, [x3 - L/30 ,y3 + L/24], [x3-L/7 ,y3 + L/60], 1) 
    pygame.draw.line(screen, BLACK, [x3 + L/30 ,y3 + L/24], [x3+L/7 ,y3 + L/60], 1) 
    pygame.draw.line(screen, BLACK, [x3 - L/30 ,y3 + L/20], [x3-L/7 ,y3 + L/26], 1) 
    pygame.draw.line(screen, BLACK, [x3 + L/30 ,y3 + L/20], [x3+L/7 ,y3 + L/26], 1) 
    
    #Ears
    pygame.draw.polygon(screen, CATFUR, [[x3 - L/4 ,y3 - L/4 - 3*L/30], [x3 - L/4 + 9*L/60 ,y3 - L/4 - L/60], [x3 - L/4 + 2*L/60 ,y3 - L/4 + L/9  - L/30]])
    pygame.draw.polygon(screen, CATFUR, [[x3 + L/4 ,y3 - L/4 - 3*L/30], [x3 + L/4 - 9*L/60 ,y3 - L/4 - L/60], [x3 + L/4 - 2*L/60 ,y3 - L/4 + L/9 - 2*L/60]])
    
    pygame.draw.polygon(screen, CATEAR, [[x3 - L/4 + L/30 ,y3 - L/4 - L/15], [x3 - L/4 + 7*L/60 ,y3 - L/4 - L/60], [x3 - L/4 + 3*L/60 ,y3 - L/4 + L/9 - L/15]])
    pygame.draw.polygon(screen, CATEAR, [[x3 + L/4 - L/30 ,y3 - L/4 - L/15], [x3 + L/4 - 7*L/60 ,y3 - L/4 - L/60], [x3 + L/4 - 3*L/60 ,y3 - L/4 + L/9 - L/15]])

    pygame.draw.polygon(screen, BLACK, [[x3 - L/4 ,y3 - L/4 - 3*L/30], [x3 - L/4 + 9*L/60 ,y3 - L/4 - L/60], [x3 - L/4 + 2*L/60 ,y3 - L/4 + L/9  - L/30]], 1)
    pygame.draw.polygon(screen, BLACK   , [[x3 + L/4 ,y3 - L/4 - 3*L/30], [x3 + L/4 - 9*L/60 ,y3 - L/4 - L/60], [x3 + L/4 - 2*L/60 ,y3 - L/4 + L/9 - L/30]], 1)
    screen = pygame.transform.flip(screen, True, False) 
    scr.blit(screen, [X,0])
#Ball (Function that draws balls) T_B(Ball_xcor, Ball_ycor, Ball height, scr)  
def T_B(x,y,h,screen):      
    pygame.draw.ellipse(screen, GRAY, [x, y , h, h])
    pygame.draw.ellipse(screen, BLACK, [x, y , h, h], 1)
    x=h/12 + x
    pygame.draw.line(screen, BLACK, [x + h/2 - 4*h/14, y + h/2 + 5*h/12],[x + h/2 - h/14,y + h/2 + 2*h/12]) 
    pygame.draw.line(screen, BLACK, [x + h/2 - 5*h/14, y + h/2 + 4*h/12],[x + h/2 - 2*h/14,y + h/2 + h/12]) 
    pygame.draw.line(screen, BLACK, [x + h/2 - 6*h/14, y + h/2 + 3*h/12],[x + h/2 - 3*h/14,y + h/2 - h/12]) 
    x=x - h/12
    pygame.draw.line(screen, BLACK, [x + h/2 - h/12, y + h/2 - h/6],[x + h/2 + h/12,y + h/2 + h/6]) 
    pygame.draw.line(screen, BLACK, [x + h/2, y + h/2 - 2*h/6],[x + h/2 + 2*h/12,y + h/2 + h/6]) 
    pygame.draw.line(screen, BLACK, [x + h/2 + h/12, y + h/2 - 2.9*h/6],[x + h/2 + 3*h/12,y + h/2]) 
    
    pygame.draw.line(screen, BLACK, [x + h/2, y + 0.98*h],[x + 1.1*h,y + 0.98*h]) 
    
while not done:
    clock.tick(10)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    #Background
    pygame.draw.polygon(scr, BROWNDAR, [[0, 0], [X, 0], [X, 0.45*Y], [0, 0.45*Y], [0, 0]])
    pygame.draw.polygon(scr, BROWNGR, [[0, 0.45*Y], [0, Y], [X, Y], [X, 0.45*Y], [0, 0.45*Y]])
    
    #Windows
    T_W(450, 50, 200, scr)
    T_W(260, 50, 200, scr)
    T_W(80, 50, 200, scr)
    
    #Screen horizontal flip
    scr = pygame.transform.flip(scr, True, False) 
    
    #Reversed Cats and Balls
    T_B(50, 400, 100,scr)   
    T_B(300, 630, 50,scr)       
    
    T_C(110, 450, 100, BCATFUR, BCATEAR, BCATNOSE, BCATEYE, scr)   
    T_C(140, 630, 40, BCATFUR, BCATEAR, BCATNOSE, BCATEYE, scr) 
    T_C(200, 700, 100, ACATFUR, ACATEAR, ACATNOSE, ACATEYE, scr)   
    T_C(400, 350, 40, ACATFUR, ACATEAR, ACATNOSE, ACATEYE, scr)          

    #Screen horizontal flip
    scr = pygame.transform.flip(scr, True, False) 
    
    #Normal Cats and Balls
    T_B(50, 350, 100, scr)   
    T_B(200, 630, 50, scr) 
    
    T_C(300,300,100,BCATFUR,BCATEAR,BCATNOSE,BCATEYE, scr)   
    T_C(200,630,80,BCATFUR,BCATEAR,BCATNOSE,BCATEYE, scr) 
    T_C(200,550,100,ACATFUR,ACATEAR,ACATNOSE,ACATEYE, scr)   
    T_C(400,400,40,ACATFUR,ACATEAR,ACATNOSE,ACATEYE, scr)   
     
    screen.blit(scr, [0, 0])  
    pygame.display.flip()
    
pygame.quit()                 