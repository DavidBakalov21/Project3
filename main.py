import pgzrun
from Vector import Vector
RADIUS=25
class EmptyObject:
    def __init__(self, vector:Vector):
        self.position=vector
     #   self.acceleration=Vector(5,5)


    def draw(self):
        screen.draw.filled_circle((self.position.x, self.position.y), RADIUS, (80,0,70))

class Heatr1:
    def __init__(self):
        self.actor=Actor('h.png', center=(0, 0))
    def draw(self):
        self.actor.draw()

class Heatr2:
    def __init__(self):
        self.actor=Actor('h.png', center=(50, 0))
    def draw(self):
        self.actor.draw()

class Heatr3:
    def __init__(self):
        self.actor=Actor('h.png', center=(100, 0))
    def draw(self):
        self.actor.draw()

class Platform:
    def __init__(self,vector:Vector):
        self.position=vector
        self.velocity=Vector(200,200)
        #self.actor=Actor('platform.png', center=(300, 550))
    def draw(self):
        screen.draw.filled_rect(Rect((self.position.x, self.position.y),(150,50)), (200, 0, 0))
    def get_position(self):
        return Vector(self.position.x, self.position.y)
    def on_mouse_move(self,pos):
        #print(pos)
        self.position.x=pos[0]
        if self.position.x>649:
            self.position.x=649
        elif self.position.x<0:
            self.position.x=0

class Ball():
    def __init__(self, vector:Vector):
        self.position=vector
        self.velocity=Vector(400,-400)
     #   self.acceleration=Vector(5,5)


    def draw(self):
        screen.draw.filled_circle((self.position.x, self.position.y), RADIUS, "red")

WIDTH = 800
HEIGHT = 600
HEARTS=0
platform=Platform(Vector(300, 450))
ball=Ball(Vector(0,0))

heart1=Heatr1()
heart2=Heatr2()
heart3=Heatr3()

# Object to make hearts work
hh=EmptyObject(Vector(333,-333))

obj=[heart1, heart2, heart3,hh,hh]
#circle=Circle(Vector(200, 200))
def draw():
    screen.clear()
    screen.fill((80,0,70))
    platform.draw()
    ball.draw()
    if HEARTS<3:
        for el in obj:
            el.draw()
    else:
        screen.draw.text("GAME OVER", (50, 30), color="orange")





def on_mouse_move(pos):
    platform.on_mouse_move(pos)



def update(dt):

    global HEARTS
    v=ball.velocity
    distance=(ball.position-platform.get_position()).magnitude()
    if distance<90 and v.y>0:
        ball.velocity=Vector(v.x, -v.y)




    if HEARTS<3:
        if ball.position.y>=HEIGHT-RADIUS and v.y>0:
        ##print("Y")
            #ball.velocity=Vector(v.x, -v.y)
            obj.remove(obj[HEARTS])
            HEARTS+=1
            ball.position.x=0
            ball.position.y=0
            print(HEARTS)
    if ball.position.y<=0 and v.y<0:
        print("Y")
        ball.velocity=Vector(v.x, -v.y)
    if ball.position.x>=WIDTH-RADIUS and v.x>0:
        ball.velocity=Vector(-v.x, v.y)
    if ball.position.x<=0 and v.x<0:
        ball.velocity=Vector(-v.x, v.y)


    ball.position+=Vector(v.x*dt,v.y*dt)


pgzrun.go()

