import numpy as np
import pygame as pg
from random import randint

pg.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

SCREEN_SIZE = (800, 600)


class Gun():
    def __init__(self, coord=[30, SCREEN_SIZE[1]//2], min_pow=10, max_pow=30):
        self.coord = coord
        self.angle = 0
        self.min_pow = min_pow
        self.max_pow = max_pow
        self.power = min_pow
        self.active = False

    def strike(self):
        vel = [int(self.power * np.cos(self.angle)), int(self.power * np.sin(self.angle))]
        self.active = False
        self.power = self.min_pow
        return Ball(list(self.coord), vel)
        
    def move(self):
        if self.active and self.power < self.max_pow:
            self.power += 1

    def draw(self, screen):
        gun_shape = []
        v1 = np.array([int(5*np.cos(self.angle - np.pi/2)), int(5*np.sin(self.angle - np.pi/2))])
        v2 = np.array([int(self.power*2*np.cos(self.angle)), int(self.power*2*np.sin(self.angle))])
        gun_pos = np.array(self.coord)
        gun_shape.append((gun_pos + v1).tolist())
        gun_shape.append((gun_pos + v1 + v2).tolist())
        gun_shape.append((gun_pos + v2 - v1).tolist())
        gun_shape.append((gun_pos - v1).tolist())
        pg.draw.polygon(screen, BLUE, gun_shape)

    def set_angle(self, mouse_pos):
        self.angle = np.arctan2(mouse_pos[1] - self.coord[1], 
                                mouse_pos[0] - self.coord[0])   
    
class Ball():
    def __init__(self, coord, vel=[0,0], rad=15, color=None):
        if color == None:
            color = (randint(0, 255), randint(0, 255), randint(0, 255))
        self.color = color
        self.coord = coord
        self.vel = vel
        self.rad = rad
        self.delete = False
        
        
    def draw(self, screen):
        pg.draw.circle(screen, self.color, self.coord, self.rad)
    
    def move(self, t_step=1., a=1):
        self.vel[1] += a*t_step
        for i in range(2):
            self.coord[i] += int(self.vel[i] * t_step)
        self.check_walls()
        
        if self.vel[0]**2 + self.vel[1]**2 < 2**2 and self.coord[1] > SCREEN_SIZE[1] - 2*self.rad:
            self.delete = True
        
    def check_walls(self):
        n = [[1, 0], [0, 1]]
        for i in range(2):
            if self.coord[i] < self.rad:
                self.coord[i] = self.rad
                self.flip_vel(n[i])
            elif self.coord[i] > SCREEN_SIZE[i] - self.rad:
                self.coord[i] = SCREEN_SIZE[i] - self.rad
                self.flip_vel(n[i])
                
    def flip_vel(self, axis, coef_perp = 0.8, coef_par = .9):
        vel = np.array(self.vel)
        n = np.array(axis)
        n = n / np.linalg.norm(n)
        vel_perp = vel.dot(n) * n
        vel_par = vel - vel_perp
        ans = -vel_perp * coef_perp + vel_par * coef_par
        self.vel = ans.astype(np.int).tolist()
        
class Target():
    def __init__(self, coord=None, color=GREEN, rad=30):
        coord = [randint(rad, SCREEN_SIZE[0] - rad), randint(rad, SCREEN_SIZE[1] - rad)]
        self.coord = coord
        self.rad = rad
        self.color = color
        
    def check_ball(self,ball):
        dist = sum([(self.coord[i] - ball.coord[i])**2 for i in range(2)])**0.5
        min_dist = self.rad + ball.rad
        return dist <= min_dist    
            
    def draw(self, screen):
        pg.draw.circle(screen, self.color, self.coord, self.rad)
       
class Obstacle():
    def __init__(self, coord=None, color=RED, rad=90):
        coord = [randint(90, SCREEN_SIZE[0] - 90), randint(90, SCREEN_SIZE[1] - 90)]
        angle = [randint(0,360)]
        self.coord = coord
        self.rad = rad
        self.color = color
        self.angle = angle
        self.mid = (self.rad*np.cos(self.angle)/2 + self.coord[0] ,self.rad*np.sin(self.angle)/2 + self.coord[1])
        
        self.coord2 = (self.rad*np.cos(self.angle) + self.coord[0] ,self.rad*np.sin(self.angle) + self.coord[1])
            
    def draw(self, screen):
        pg.draw.line(screen, self.color, self.coord, self.coord2, 1)

    
class Table():
    def __init__(self, t_destr=0, b_used=0):
        self.t_destr = t_destr
        self.b_used = b_used
        self.font = pg.font.SysFont("Ariel", 50)

    def score(self):
        return self.t_destr - self.b_used
    
    def draw(self,screen):
        surf = []
        surf.append(self.font.render("Score: {}".format(self.score()), True, BLUE))
        screen.blit(surf[0], [10, 10])
        


class Manager():

    def __init__(self):
        self.gun = Gun()
        self.table = Table()
        self.balls = []
        self.targets = []
        self.obstacles = []
        self.new_targets()
         
    def new_targets(self):
        self.targets.append(Target())
        if len(self.obstacles) > 0: 
            self.obstacles.pop(0)        
        self.obstacles.append(Obstacle())
        
    def process(self, events, screen):
        done = self.handle_events(events)
        self.move()
        self.draw(screen)
        self.collide()  
        if len(self.targets) == 0 and len(self.balls) == 0:
            self.new_targets()
        return done

             
    def draw(self, screen):
        screen.fill(BLACK)
        
        for ball in self.balls:
            ball.draw(screen)
            
        self.gun.draw(screen)
        
        for obstacle in self.obstacles:
            obstacle.draw(screen)
        
        self.table.draw(screen)
        
        for target in self.targets:
            target.draw(screen)
        
    def move(self):
        dead_balls = []
        for ball in self.balls:
            ball.move()
        for i, ball in enumerate(self.balls):
            if ball.delete:
                dead_balls.append(i)
        for i in reversed(dead_balls):
            self.balls.pop(i)
        self.gun.move()
        
    def collide(self):
        collisions = []
        targets_c = []
        for i, ball in enumerate(self.balls):
            for j, target in enumerate(self.targets):
            
                if target.check_ball(ball):
                    targets_c.append(j)
                    
            for obstacle in self.obstacles:
            
                distance = ((obstacle.mid[0] - ball.coord[0])*np.sin(obstacle.angle) - (obstacle.mid[1] - ball.coord[1])*np.cos(obstacle.angle),
                           -(obstacle.mid[1] - ball.coord[1])*np.sin(obstacle.angle) - (obstacle.mid[0] - ball.coord[0])*np.sin(obstacle.angle))

                if  np.abs(distance[0]) < ball.rad and np.abs(distance[1]) < obstacle.rad/2: 
                    self.obstacles.pop(0)
                    ball.vel[1] = 0.5*ball.vel[1]
                    ball.vel[0] = 0.5*ball.vel[0]
                            
        targets_c.sort()
        for j in reversed(targets_c):                                                                                                     
            self.table.t_destr += 1
            self.targets.pop(j)   
    
    
    def handle_events(self, events):
        done = False
        for event in events:
            if event.type == pg.QUIT:
                done = True
                
            elif event.type == pg.KEYDOWN:
                
                if event.key == pg.K_UP:
                    self.gun.coord[1] -= 5
                elif event.key == pg.K_DOWN:
                    self.gun.coord[1] += 5
                    
            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.gun.active = True
            elif event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:
                    self.balls.append(self.gun.strike())
        
        if pg.mouse.get_focused():
            mouse_pos = pg.mouse.get_pos()
            self.gun.set_angle(mouse_pos)
            
        return done


        
screen = pg.display.set_mode(SCREEN_SIZE)
pg.display.set_caption("The gun of Kolganov")

done = False
clock = pg.time.Clock()

mgr = Manager()

while not done:
    clock.tick(20)

    done = mgr.process(pg.event.get(), screen)

    pg.display.flip()


pg.quit()