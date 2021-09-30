import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random
WIDTH=600
HEIGHT=400
PAD_WIDTH= 5
PAD_HEIGHT=80
ball_position=[WIDTH/2,HEIGHT/2]
ball_radius=10
ball_velocity=[-random.randrange(60,180)/60, random.randrange(120,240)/60]
paddle1_position = HEIGHT/2
paddle2_position = HEIGHT/2
score1=0
score2=0
paddle1_vel=0
paddle2_vel=0

def draw(c):
    global score1, score2, paddle1_vel, paddle2_vel, paddle1_position, paddle2_position
    if paddle1_position < PAD_HEIGHT/2 + PAD_WIDTH and paddle1_vel < 0:
        paddle1_vel=0
    if paddle2_position < PAD_HEIGHT/2 + PAD_WIDTH and paddle2_vel<0:
        paddle2_vel = 0
    if paddle1_position > ( HEIGHT - PAD_HEIGHT/2 - PAD_WIDTH ) and paddle1_vel > 0:
        paddle1_vel = 0
    if paddle2_position > ( HEIGHT - PAD_HEIGHT/2 - PAD_WIDTH ) and paddle2_vel > 0:
        paddle2_vel = 0

    paddle1_position += paddle1_vel
    paddle2_position += paddle2_vel

    ball_position[0] += ball_velocity[0]
    ball_position[1] += ball_velocity[1]
    if (ball_position[1] >= HEIGHT- PAD_WIDTH - ball_radius) or ball_position[1] <= ( PAD_WIDTH+ ball_radius ):
        ball_velocity[1]= -ball_velocity[1]
    if ( ball_position[0] <= ( 2*PAD_WIDTH + ball_radius ) ):
        if( ball_position[1] < (paddle1_position - PAD_HEIGHT/2 )) or (ball_position[1] > (paddle1_position + PAD_HEIGHT/2) ):
            ball_reset(False)
            score2+= 1
        else:
            ball_velocity[0] = -ball_velocity[0] * 1.1
    if ( ball_position[0] >= ( WIDTH-PAD_WIDTH-ball_radius ) ):
        if ball_position[1] < (paddle2_position - PAD_HEIGHT/2) or ball_position[1] > (paddle2_position + PAD_HEIGHT/2):
            ball_reset(True)
            score1 += 1
        else:
            ball_velocity[0] = -ball_velocity[0] * 1.1

    c.draw_line([WIDTH/2 ,PAD_WIDTH], [WIDTH/2, HEIGHT-PAD_WIDTH],1, "WHITE")
    c.draw_line([PAD_WIDTH, PAD_WIDTH],[PAD_WIDTH, HEIGHT-PAD_WIDTH],1,"WHITE")
    c.draw_line([WIDTH-PAD_WIDTH,PAD_WIDTH],[WIDTH-PAD_WIDTH,HEIGHT-PAD_WIDTH],1,"WHITE")
    c.draw_line([PAD_WIDTH,PAD_WIDTH],[WIDTH-PAD_WIDTH,PAD_WIDTH],1,"WHITE")
    c.draw_line([PAD_WIDTH,HEIGHT-PAD_WIDTH],[WIDTH-PAD_WIDTH,HEIGHT-PAD_WIDTH],1,"WHITE")
    c.draw_circle(ball_position, ball_radius, 2,"BLUE","BLUE")
    c.draw_text(str(score1), ( 170, 50 ), 25,"RED")
    c.draw_text(str(score2), ( 400, 50),25,"BLUE")
    c.draw_polygon([(PAD_WIDTH, paddle1_position-PAD_HEIGHT/2), (PAD_WIDTH, paddle1_position+PAD_HEIGHT/2), (2*PAD_WIDTH, paddle1_position+PAD_HEIGHT/2),(2*PAD_WIDTH,paddle1_position-PAD_HEIGHT/2)], PAD_WIDTH-1, "Red","Red")
    c.draw_polygon([(WIDTH-2*PAD_WIDTH, paddle2_position-PAD_HEIGHT/2), (WIDTH-2*PAD_WIDTH, paddle2_position+PAD_HEIGHT/2), (WIDTH-PAD_WIDTH, paddle2_position+PAD_HEIGHT/2),(WIDTH-PAD_WIDTH,paddle2_position-PAD_HEIGHT/2)], PAD_WIDTH-1, "Blue","Blue")

def reset():
    global paddle1_position, paddle2_position, paddle1_vel, paddle2_vel
    global score1, score2
    paddle1_position=HEIGHT/2
    paddle2_position=HEIGHT/2
    paddle1_vel=0
    paddle2_vel=0
    score1=0
    score2=0
    ball_reset(00==random.randrange(0,10)%2)

def ball_reset(Right):
    global ball_position, ball_velocity
    ball_position =[WIDTH/2, HEIGHT/2]
    ball_velocity[1] = -random.randrange(60, 180)/60
    if Right==True:
        ball_velocity[0]= random.randrange(120,240)/60
    elif Right==False:
        ball_velocity[0]= -random.randrange(120,240)/60

def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = -4
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel = 4
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel = -4
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel = 4
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel = 0
   


    
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Reset", reset, 200)

frame.start()
