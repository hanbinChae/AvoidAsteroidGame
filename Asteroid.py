import turtle
import time

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300

def outline():
    tline = turtle.Turtle()
    
    tline.up()
    tline.goto(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    tline.down()
    
    tline.goto(-SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    tline.goto(-SCREEN_WIDTH/2,-SCREEN_HEIGHT/2)
    print(-SCREEN_WIDTH/2,-SCREEN_HEIGHT/2)
    tline.goto(SCREEN_WIDTH/2,-SCREEN_HEIGHT/2)
    tline.goto(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)

outline()

loc=[[0,0],[0,0]]
vel=[[10,7],[-5,9]]
asteroid_list = []
startTime = time.time()

for i in range(len(loc)):
    t = turtle.Turtle()
    t.shape("circle")
    t.goto(loc[i][0],loc[i][1])
    asteroid_list.append(t)

for i in range(200):
   for i in range(len(loc)):
        loc[i][0]+=vel[i][0]
        loc[i][1]+=vel[i][1]
        
        asteroid_list[i].goto(loc[i][0],loc[i][1])
        
        if loc[i][0]>=SCREEN_WIDTH/2:
            vel[i][0] = -vel[i][0]
        
        if loc[i][0]<=-SCREEN_WIDTH/2:
            vel[i][0] = -vel[i][0]
        
        if loc[i][1]>=SCREEN_HEIGHT/2:
            vel[i][1] = -vel[i][1]
        
        if loc[i][1]<=-SCREEN_HEIGHT/2:
            vel[i][1]= -vel[i][1]
            
timeDiff = time.time()-startTime
turtle.write(timeDiff)

turtle.exitonclick()
turtle.bye()