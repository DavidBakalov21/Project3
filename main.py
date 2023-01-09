import pgzrun
from Vector import Vector

RADIUS=40
class EmptyObject:
    def __init__(self, vector:Vector):
        self.position=vector
     #   self.acceleration=Vector(5,5)


    def draw(self):
        screen.draw.filled_circle((self.position.x, self.position.y), RADIUS, (80,0,70))

class Heatr1:
    def __init__(self, x_pose, y_pose):
        self.x_pose=x_pose
        self.y_pose=y_pose
        self.actor=Actor('h.png', center=(self.x_pose, self.y_pose ))
    def draw(self):
        self.actor.draw()
class Platform:
    def __init__(self):
        #self.position=vector
        #self.velocity=Vector(200,200)
        self.actor=Actor('plat.png', center=(300, 550))
    def draw(self):
        self.actor.draw()
    def get_position(self):
        return Vector(self.actor.x, self.actor.y)
    def on_mouse_move(self,pos):
        #print(pos)
        self.actor.x=pos[0]
        if self.actor.x>800:
            self.actor.x=800
        elif self.actor.x<0:
            self.actor.x=0

class Ball():
    def __init__(self):
        # self.position=vector
        self.actor=Actor('b.png', center=(150,150))
        self.velocity=Vector(300,-300)
     #   self.acceleration=Vector(5,5)


    def draw(self):
        self.actor.draw()
    def update(self, dt):
        global HEARTS
       # print(dt)
        if self.actor.y+RADIUS>=HEIGHT:
            obj.remove(obj[HEARTS])
            HEARTS+=1
            self.actor.x=150
            self.actor.y=150
            print(HEARTS)
        if self.actor.y  <= 0:
            print("Y")
            self.velocity=Vector(self.velocity.x, -self.velocity.y)
        if self.actor.x + RADIUS >= WIDTH:
            print("X")
            self.velocity=Vector(-self.velocity.x, self.velocity.y)
        if self.actor.x - RADIUS <= 0:
            print("X")
            self.velocity=Vector(-self.velocity.x, self.velocity.y)


        print(self.velocity)
        self.actor.x = self.actor.x + self.velocity.x*dt
        self.actor.y = self.actor.y + self.velocity.y*dt
        print(self.actor.x, self.actor.y)

WIDTH = 800
HEIGHT = 600
HEARTS=0
platform=Platform()
ball=Ball()

heart1=Heatr1(0,0)
heart2=Heatr1(50,0)
heart3=Heatr1(100,0)

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
    # distance=(ball.position-platform.get_position()).magnitude()
   # if distance<90 and v.y>0:
    #    ball.velocity=Vector(v.x, -v.y)



    #print("UPD")



    if HEARTS<3:
        ball.update(dt)
    if platform.actor.colliderect(ball.actor):
        print("YES")
        ball.velocity = Vector(v.x, -v.y)


pgzrun.go()
