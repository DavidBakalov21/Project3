import pgzrun
from Vector import Vector
RADIUS=25
class Platform:
    def __init__(self):
        self.actor=Actor('platform.png', center=(300, 550))
    def draw(self):
        self.actor.draw()
    def get_position(self):
        return Vector(self.actor.x, self.actor.y)
    def on_mouse_move(self,pos):
       # print(pos)
        self.actor.x=pos[0]
        if self.actor.x>545:
            self.actor.x=545
        elif self.actor.x<185:
            self.actor.x=185

class Ball():
    def __init__(self, vector:Vector):
        self.position=vector
        self.velocity=Vector(200,200)
     #   self.acceleration=Vector(5,5)


    def draw(self):
        screen.draw.filled_circle((self.position.x, self.position.y), RADIUS, "red")

WIDTH = 800
HEIGHT = 600
platform=Platform()
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
    if distance<100 and v.y>0:
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

