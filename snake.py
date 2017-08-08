import turtle
import random

turtle.tracer(1, 0)
turtle.bgcolor('orange')
SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X, SIZE_Y)
turtle.penup()
box_x = 700
box_y = 400
box = turtle.clone()
box.penup()
box.speed = 800
box.goto(-350, 0)
box.pendown()
box.goto(-350, 200)
box.goto(350, 200)
box.goto(350, -200)
box.goto(-350, -200)
box.goto(-350, 0)
box.hideturtle()


SQUARE_SIZE=20
START_LENGTH=1

pos_list = []
stamp_list = []
food_pos = []
food_stamps = []
score = []

snake = turtle.clone()
snake.shape('square')
turtle.hideturtle()
turtle.colormode(255)

for i in range(START_LENGTH):
    x_pos=snake.pos()[0]
    y_pos=snake.pos()[1]

    x_pos+=SQUARE_SIZE

    my_pos=(x_pos, y_pos)
    snake.goto(x_pos, y_pos)

    pos_list.append(my_pos)

    a = snake.stamp()
    stamp_list.append(a)
UP_ARROW = 'Up'
LEFT_ARROW = 'Left'
RIGHT_ARROW = 'Right'
DOWN_ARROW = 'Down'
TIME_STEP = 100

SPACEBAR = 'space'

UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3

direction = UP
TOP_EDGE = 200
BOTTOM_EDGE = -200
RIGHT_EDGE = 350
LEFT_EDGE = -350
def up():
    global direction
    if direction != DOWN:
        direction=UP
        print('you pressed up key')

def down():
    global direction
    if direction != UP:
        direction=DOWN
        print('you pressed down key')

def right():
    global direction
    if direction != LEFT:
        direction=RIGHT
        print('you pressed right key')

def left():
    global direction
    if direction != RIGHT:
        direction=LEFT
        print('you pressed left key')
    
turtle.onkeypress(up, UP_ARROW)
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)
turtle.listen()

def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]

    def random_color():
        rgbl=[255,0,0]
        random.shuffle(rgbl)
        return tuple(rgbl)
    snake.color(random_color())

    if direction==RIGHT:
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print('you moved right')
    elif direction==LEFT:
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print('you moved left')
    elif direction==UP:
        snake.goto(x_pos, y_pos + SQUARE_SIZE)
        print('you moved up')
    elif direction==DOWN:
        snake.goto(x_pos, y_pos - SQUARE_SIZE)
        print('you moved down')

    my_pos = snake.pos()
    pos_list.append(my_pos)
    new_stamp = snake.stamp()
    stamp_list.append(new_stamp) ########special place
    global food_stamps, food_pos, score
    if snake.pos() in food_pos:
        food_ind = food_pos.index(snake.pos())
        food.clearstamp(food_stamps[food_ind])
        w = snake.stamp()
        stamp_list.append(w)
        pos_list.append(w)
        food_pos.pop(food_ind)
        score.append(food_ind)
        food_stamps.pop(food_ind)
        print('You have eaten the food!')
        make_food()
        turtle.clear()
        turtle.pencolor(random_color())
        turtle.write(len(score) - 1 + START_LENGTH, font=("ariel", 16))
    old_stamp = stamp_list.pop(0)
    snake.clearstamp(old_stamp)
    pos_list.pop(0)
    #GRAB POSITION OF THE SNAKE
    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]

    if new_x_pos>= RIGHT_EDGE:
        print('You hit the right edge! Game over')
        quit()
    if new_x_pos<= LEFT_EDGE:
        print('You hit the left edge! game over')
        quit()
    if new_y_pos>= TOP_EDGE:
        print('You hit the top wall! game over')
        quit()
    if new_y_pos<= BOTTOM_EDGE:
        print('You hit the bottom wall! game over')
        quit()
    #
    if snake.pos() in pos_list[0:-2]:
        print('You hit yourself! game over')
        quit()
    turtle.ontimer(move_snake,TIME_STEP)
move_snake()
    
#turtle.register_shape('circle')    
food = turtle.clone()
food.shape('circle')
food_pos = [(100,100), (-100,100), (-100,-100), (100, -100)]
food_stamps = []
for i in food_pos:
    food.goto(i)
    f1 = food.stamp()
    food_stamps.append(f1)
def make_food():
    min_x=-int(box_x/2/SQUARE_SIZE)+5
    max_x=int(box_x/2/SQUARE_SIZE)-5
    min_y=-int(box_y/2/SQUARE_SIZE)+5
    max_y=int(box_y/2/SQUARE_SIZE)-5

    food_x = random.randint(min_x, max_x)*SQUARE_SIZE
    food_y = random.randint(min_y, max_y)*SQUARE_SIZE
    food_x_y = (food_x, food_y)
    
    if food_x_y not in pos_list: # food is on snake
        
        food.goto(food_x, food_y)
        food_pos.append(food_x_y)
        f2 = food.stamp()
        food_stamps.append(f2)

