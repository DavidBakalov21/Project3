import pgzrun
from Vector import Vector
RADIUS=25
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
        print(pos)
        self.position.x=pos[0]
        if self.position.x>649:
            self.position.x=649
        elif self.position.x<0:
            self.position.x=0

class Ball():
    def __init__(self, vector:Vector):
        self.position=vector
        self.velocity=Vector(200,200)
     #   self.acceleration=Vector(5,5)


    def draw(self):
        screen.draw.filled_circle((self.position.x, self.position.y), RADIUS, "red")

WIDTH = 800
HEIGHT = 600
platform=Platform(Vector(300, 450))
ball=Ball(Vector(90,500))
#circle=Circle(Vector(200, 200))
def draw():
    screen.clear()
    screen.fill((80,0,70))
    platform.draw()
    ball.draw()





def on_mouse_move(pos):
    platform.on_mouse_move(pos)



def update(dt):
    v=ball.velocity
    distance=(ball.position-platform.get_position()).magnitude()
    if distance<75 and v.y>0:
        ball.velocity=Vector(v.x, -v.y)




    if ball.position.y>=HEIGHT-RADIUS and v.y>0:
        ##print("Y")
        ball.velocity=Vector(v.x, -v.y)
    if ball.position.y<=0 and v.y<0:
        print("Y")
        ball.velocity=Vector(v.x, -v.y)
    if ball.position.x>=WIDTH-RADIUS and v.x>0:
        ball.velocity=Vector(-v.x, v.y)
    if ball.position.x<=0 and v.x<0:
        ball.velocity=Vector(-v.x, v.y)


    ball.position+=Vector(v.x*dt,v.y*dt)


pgzrun.go()

