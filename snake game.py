import turtle,time,random
delay=0.1   #reduce speed
#create a window design
window=turtle.Screen()
window.title('SNAKE XANIA')
window.bgcolor('green')
window.setup(width=600,height=600)
window.tracer(0)


#create a snake head
head=turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('black')
head.goto(0,0)
head.direction='stop' #position to move snake head 
head.penup() #remove trace

#snake food
food=turtle.Turtle()
food.speed(0)
food.color('pink')
food.shape('circle')
food.penup()
food.goto(0,90)

#score
pen=turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color('white')
pen.penup()
pen.goto(0,260)#change position score(260,260) right side
pen.hideturtle()
pen.write("SCORE:0",align="center",font=('bold',28,'normal'))


def move():
    if head.direction =='up':
        y=head.ycor()
        head.sety(y+20) #head position up
    if head.direction =='down':
        y=head.ycor()
        head.sety(y-20) #head position down
    if head.direction =='right':
        x=head.xcor()
        head.setx(x+20) #move right
    if head.direction =='left':
        x=head.xcor()
        head.setx(x-20) #move left
def go_up():
    if head.direction !='down':
        head.direction='up'
def go_down():
     if head.direction !='up':
         head.direction='down'
def go_right():
     if head.direction !='left':
         head.direction='right'
def go_left():
     if head.direction !='right':
         head.direction='left'

window.listen()#listen key in keyboard
window.onkeypress(go_up,'Up')#use 1st letter-capital(common for all)
window.onkeypress(go_down,'Down')#use 1st letter-capital(common for all)
window.onkeypress(go_right,'Right')#use 1st letter-capital(common for all)
window.onkeypress(go_left,'Left')#use 1st letter-capital(common for all)
body=[]
score=0

while True:
    window.update()#collision
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.direction='stop'
        head.goto(0,0)
        for i in body:#body collision 
            i.goto(1000,1000)
        body.clear()
        score,delay=0,0.1
        pen.clear()
        pen.write(f"SCORE:{score}",align="center",font=('bold',28,'normal'))

    if head.distance(food)<20:#food position 
        x=random.randint(-290,290)#value lower to higher
        y=random.randint(-290,290)
        food.goto(x,y)
        new_body=turtle.Turtle()#adding new body
        new_body.speed(0)
        new_body.color('grey')
        new_body.shape('square')
        new_body.penup()
        body.append(new_body)
        score+=1
        pen.clear()
        pen.write(f"SCORE:{score}",align="center",font=('bold',28,'normal'))
    for i in range(len(body)-1,0,-1):
        x=body[i-1].xcor()
        y=body[i-1].ycor()
        body[i].goto(x,y)
    if len(body)>0:
        x=head.xcor()
        y=head.ycor()
        body[0].goto(x,y)
    delay-=0.0001
    time.sleep(delay)
    move()
    for i in body:#collision if snake touch body it will stop
        if i.distance(head)<20:
            time.sleep(0)
            head.direction='stop'
            head.goto(0,0)
            for i in body:
                i.goto(1000,1000)
            body.clear()
            score,delay=0,0.1
            pen.clear()
            pen.write(f"SCORE:{score}",align="center",font=('bold',28,'normal'))




        
    
