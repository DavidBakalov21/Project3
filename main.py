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
class Obstacle:
    def __init__(self,x_Pose, y_Pose):
        self.x_Pose=x_Pose
        self.y_Pose=y_Pose
        self.actor=Actor('obstacle.png', center=(self.x_Pose, self.y_Pose ))
    def draw(self):
        self.actor.draw()
class Platform:
    def __init__(self):
        #self.position=vector
        #self.velocity=Vector(200,200)
        self.actor=Actor('plat.png', center=(300, 450))
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
        if self.actor.y-RADIUS  <= 0:
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

WIDTH = 940
HEIGHT = 450
HEARTS=0
SCRORE=0
platform=Platform()
ball=Ball()

heart1=Heatr1(0,0)
heart2=Heatr1(50,0)
heart3=Heatr1(100,0)

ob1=Obstacle(700, 30)
ob2=Obstacle(300, 100)
ob3=Obstacle(400, 100)
ob4=Obstacle(500, 100)
ob5=Obstacle(900,100)
ob6=Obstacle(500,300)

# Object to make hearts work
hh=EmptyObject(Vector(333,-333))
ob=[ob1, ob2,ob3,ob4,ob5, ob6]
obj=[heart1, heart2, heart3,hh,hh]
#circle=Circle(Vector(200, 200))
def draw():
    screen.clear()
    screen.fill((80,0,70))
    platform.draw()
    ball.draw()

    if SCRORE<6:
        for el in ob:
            el.draw()
    else:
        screen.draw.text("YOU WIN!!", (100, 40), color="orange")

    if HEARTS<3:
        for el in obj:
            el.draw()
    else:
        screen.draw.text("GAME OVER", (50, 30), color="orange")





def on_mouse_move(pos):
    platform.on_mouse_move(pos)



def update(dt):

    global HEARTS
    global SCRORE
    global ob
    v=ball.velocity
    # distance=(ball.position-platform.get_position()).magnitude()
   # if distance<90 and v.y>0:
    #    ball.velocity=Vector(v.x, -v.y)



    #print("UPD")

    print(ob)


    if HEARTS<3:
        ball.update(dt)
    if platform.actor.colliderect(ball.actor):
        print("YES")
        ball.velocity = Vector(v.x, -v.y)

    for el in ob:
        if ball.actor.colliderect(el.actor):
            SCRORE+=1
            ob.remove(el)
            ball.velocity = Vector(v.x, -v.y)





pgzrun.go()
