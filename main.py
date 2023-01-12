import pgzrun
from Vector import Vector
import random
import threading
import time
RADIUS=40

class EmptyObject:
    def __init__(self, x_pose, y_pose, health):
        self.x_pose=x_pose
        self.y_pose=y_pose
        self.actor=Actor('h.png', center=(self.x_pose, self.y_pose ))
     #   self.acceleration=Vector(5,5)


    def draw(self):
        self.actor.draw()
    def hit(self):
        self.health-=1
class Bonus:
    def __init__(self, pose:Vector):
        self.position=pose
        self.actor=Actor('h.png', center=(self.position.x, self.position.y ))
        self.velocity=Vector(0, 90)
    def draw(self):
        self.actor.draw()
    def move(self,dt):
        if self.actor.y+RADIUS>=HEIGHT:
            for HP in bonus:
                bonus.remove(HP)
        self.actor.y+=self.velocity.y*dt
class BonusLenght:
    def __init__(self, pose:Vector):
        self.position=pose
        self.actor=Actor('plus.png', center=(self.position.x, self.position.y ))
        self.velocity=Vector(0, 90)
    def draw(self):
        self.actor.draw()
    def move(self,dt):
        if self.actor.y+RADIUS>=HEIGHT:
            for L in bonusLenght:
                bonusLenght.remove(L)
        self.actor.y+=self.velocity.y*dt

class Heatr1:
    def __init__(self, x_pose, y_pose):
        self.x_pose=x_pose
        self.y_pose=y_pose
        self.actor=Actor('h.png', center=(self.x_pose, self.y_pose ))
    def draw(self):
        self.actor.draw()
class Obstacle:
    def __init__(self,x_Pose, y_Pose, health):
        self.x_Pose=x_Pose
        self.health=health
        self.y_Pose=y_Pose
        self.actor=Actor('obstacle.png', center=(self.x_Pose, self.y_Pose ))
    def draw(self):
        self.actor.draw()
    def hit(self):
        self.health-=1

class HEAVY_Obstacle:
    def __init__(self,x_Pose, y_Pose, health):
        self.health=health
        self.x_Pose=x_Pose
        self.y_Pose=y_Pose
        self.actor=Actor('heavy_obstacle.png', center=(self.x_Pose, self.y_Pose ))
    def draw(self):
        self.actor.draw()
    def hit(self):
        self.health-=1
class Platform:
    def __init__(self, img):
        self.img=img
        #self.position=vector
        #self.velocity=Vector(200,200)
        self.actor=Actor(self.img, center=(300, 380))
    def draw(self):
        self.actor.draw()
    def get_position(self):
        return Vector(self.actor.x, self.actor.y)
    def on_mouse_move(self,pos):
        #print(pos)
        self.actor.x=pos[0]
        if self.actor.x>950:
            self.actor.x=800
        elif self.actor.x<0:
            self.actor.x=0

class Ball:
    def __init__(self):
        # self.position=vector
        self.actor=Actor('b.png', center=(150,150))
        self.velocity=Vector(90,-90)
     #   self.acceleration=Vector(5,5)


    def draw(self):
        self.actor.draw()
    def update(self, dt):
        global HEARTS
       # print(dt)
        if self.actor.y+RADIUS>=HEIGHT:

            HEARTS-=1
            self.actor.x=150
            self.actor.y=150
            #print(HEARTS)
        if self.actor.y-RADIUS  <= 0:
         #   print("Y")
            self.velocity=Vector(self.velocity.x, -self.velocity.y)
        if self.actor.x + RADIUS >= WIDTH:
           # print("X")
            self.velocity=Vector(-self.velocity.x, self.velocity.y)
        if self.actor.x - RADIUS <= 0:
            #print("X")
            self.velocity=Vector(-self.velocity.x, self.velocity.y)



        self.actor.x = self.actor.x + self.velocity.x*dt
        self.actor.y = self.actor.y + self.velocity.y*dt


WIDTH = 940
HEIGHT = 450
HEARTS=1
SCRORE=0
LenghtGET=False
platform=Platform("plat.png")
ball=Ball()

heart1=Heatr1(30,30)
heart2=Heatr1(90,30)
heart3=Heatr1(150,30)

ob1=Obstacle(700, 30,1)
ob2=Obstacle(300, 100,1)
ob3=Obstacle(400, 100,1)
ob4=HEAVY_Obstacle(500, 100,2)
ob5=HEAVY_Obstacle(900,100,2)
ob6=HEAVY_Obstacle(500,300,2)

# Object to make hearts work
hh=EmptyObject(333,-333,1)
ob=[ob1, ob2,ob3,ob4,ob5, ob6]
obj=[heart1, heart2, heart3,hh,hh]
bonus=[]
bonusLenght=[]
#circle=Circle(Vector(200, 200))
def draw():
    screen.clear()
    screen.fill((80,0,70))
    platform.draw()
    ball.draw()

    for HP in bonus:
        HP.draw()
    for L in bonusLenght:
        L.draw()


    if SCRORE<6:
        for el in ob:
            el.draw()
    else:
        screen.draw.text("YOU WIN!!", (100, 40), color="orange")

    if HEARTS==3:
        heart1.draw()
        heart2.draw()
        heart3.draw()
    if HEARTS==2:
        heart1.draw()
        heart2.draw()
    if HEARTS==1:
        heart1.draw()
    if HEARTS<=0:
        screen.draw.text("GAME OVER", (50, 30), color="orange")
def on_mouse_move(pos):
    platform.on_mouse_move(pos)

def sleeep():
    global LenghtGET, platform
    time.sleep(5)
    LenghtGET=False
    platform=Platform("plat.png")
    print("sdcsddsdcsdc")


def update(dt):

    global HEARTS, platform, LenghtGET
    global SCRORE
    global ob
    global bonus
    global start_time

    v=ball.velocity
    if HEARTS>0:
        ball.update(dt)
    if platform.actor.colliderect(ball.actor):
        ball.velocity = Vector(v.x, -v.y)
    for HP in bonus:
        if platform.actor.colliderect(HP.actor):
            if HEARTS<3:
                bonus.remove(HP)
                HEARTS+=1
    for L in bonusLenght:
        if platform.actor.colliderect(L.actor):
            if LenghtGET==False:
                bonusLenght.remove(L)
                LenghtGET=True
                platform=Platform("platlarge.png")
                thr=threading.Thread(target=sleeep, name="thr1")
                thr.start()
    for el in ob:
        if ball.actor.colliderect(el.actor):
            ball.velocity = Vector(-v.x, -v.y)
            el.hit()
            if(el.health<1):
                ob.remove(el)
                SCRORE+=1

    if random.random()<0.002:
        position=Vector(random.randint(120,800),30)
        bonus.append(Bonus(position))
        print(bonus)
    if random.random()<0.002:
        position=Vector(random.randint(120,800),30)
        bonusLenght.append(BonusLenght(position))
        print(bonusLenght)
    for HP in bonus:
        HP.move(dt)
    for L in bonusLenght:
        L.move(dt)

    #print(HEARTS)
pgzrun.go()
