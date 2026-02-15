import pygame
import sys
import math

pygame.init()
width,height = 800,700
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("2D TRANSFORMATION VISUALIZER")
white =(255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)

clock = pygame.time.Clock()

center_x = width//2
center_y = height//2

# Drawing the co-ordinate axes(i.e. X and Y axis)
def draw_coordinate_axes():
    pygame.draw.line(screen,"white",(0,height/2),(width,height/2))
    pygame.draw.line(screen,"white",(width/2,0),(width/2,height),2)

#GET THE SHAPE YOU WANT

def get_shape(shape_name):
    if shape_name == "triangle":
        return [(0,60),(60,-60),(-60,-60)]
    
    elif shape_name == "square":
        return [(-50,50),(50,50),(50,-50),(-50,-50)]
    
    elif shape_name == "pentagon":
        return [(0,60), (55,20), (35,-60), (-35,-60), (-55,20)]
    
    else:
        return[]
    
# TRANSLATION FUNCTION

def translate(points,tx,ty):
    new_points =[]

    for point in points:
        x = point[0]
        y = point[1]

        new_x = x+tx
        new_y = y+ty
        new_points.append((new_x,new_y))

    return new_points

# SCALING FUNCTION

def scaling(points,sx,sy):
    new_points =[]

    for point in points:
        x = point[0]
        y = point[1]

        new_x = x*sx
        new_y = y*sy
        new_points.append((new_x,new_y))

    return new_points

# ROTATION FUNCTION

def rotation(points,angle_deg):
    ang_rad = math.radians(angle_deg)

    cos_value = math.cos(ang_rad)
    sin_value = math.sin(ang_rad)

    new_points = []

    for point in points:
        x = point[0]
        y = point[1]

        new_x = (x*cos_value)-(y*sin_value)
        new_y = (x*sin_value)+(y*cos_value)

        new_points.append((new_x,new_y))

    return new_points


# DRAW SHAPE FUNCTION

def draw_shape(points,colour, cent_x,cent_y):

    screen_points = []

    for x,y in points:
        screen_x = cent_x+x
        screen_y = cent_y-y
        screen_points.append((screen_x,screen_y))

    pygame.draw.polygon(screen,colour,screen_points,2)


# DEFAULT SHAPE AND TRANSFORMATINON FACTORS
#  
shape_type = "triangle"

tx,ty = 0,0
sx,sy = 1,1
angle_deg = 0


# THE MAIN LOOP OF THE PROGRAM

running =True

while running:
    screen.fill(black)
    draw_coordinate_axes()

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # PRESS THE SUITABLE KEY FOR THE SHAPE YOU WANT

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_1:
                shape_type = "triangle"
            
            elif event.key == pygame.K_2:
                shape_type = "square"
            
            elif event.key == pygame.K_3:
                shape_type = "pentagon"

            # TRANSLATION

            elif event.key == pygame.K_RIGHT:
                tx += 10
            
            elif event.key == pygame.K_LEFT:
                tx -= 10

            elif event.key == pygame.K_UP:
                ty += 10
            
            elif event.key == pygame.K_DOWN:
                ty -= 10

            # SCALING

            elif event.key == pygame.K_l:
                sx += 0.1
                sy += 0.1
            
            elif event.key == pygame.K_s:
                sx -= 0.1
                sy -= 0.1

            # ROTATION

            elif event.key == pygame.K_r:
                angle_deg +=10

            elif event.key == pygame.K_a:
                angle_deg -=10

            # RESET THE TRANSFORMATION

            elif event.key == pygame.K_SPACE:
                tx,ty = 0,0
                sx,sy = 1,1
                angle_deg = 0
    
    original_shape = get_shape(shape_type)

    transformed_shape = original_shape

    draw_shape(original_shape,red,center_x,center_y)

    transformed_shape = scaling(transformed_shape,sx,sy)
    transformed_shape = rotation(transformed_shape,angle_deg)
    transformed_shape = translate(transformed_shape,tx,ty)

    draw_shape(transformed_shape,green,center_x,center_y)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()

