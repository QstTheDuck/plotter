from ast import Load
from gettext import find
import time
from tracemalloc import start
from turtle import goto, home, pencolor, pendown, penup, update
from numpy import moveaxis, square
import pygame
from scipy.spatial import distance
import re
import turtle


line_color = (255, 255, 255)
pen_brick_sizeX_ = 60
pen_brick_sizeY_ = 60
pen_color = (0, 0, 0)
running = True
background_color_ = (71, 71, 71)
screenX_ = 1000
screenY = 1000
sample_list = [1, 2, True, None, False, None, 'Python', None]

screen = pygame.display.set_mode((screenX_, screenY))
screen.fill(background_color_)
pygame.display.set_caption('Plotter')
pygame.display.flip()


def Home():
    find

def PenDown():
    turtle.down()



def PenUp():
    turtle.up()


def Load_fig(Name_fig):
    gcode_L = []
    file = 'SVG/' + Name_fig + ".ngc"
    with open(file) as gcode:
        for line in gcode:
            line = line.strip()
            coord = re.findall(r'[XY].?\d+.\d+', line)
            if coord:
                if "M" in line:
                    find
                else:
                    gcode_L.append("{} {}".format(coord[0], coord[1]))
            if "M" in line:
                if "G" in line:
                    find
                else:
                    gcode_L.append(line)
            if "G61" in line:
                gcode_L.append(line)
    return gcode_L


def MoveCalc(muisX, muisY, pen_brick_sizeX, pen_brick_sizeY, screenX, background_color, screen):

    # clear
    screen.fill(background_color)

    # pen

    # pygame.draw.rect(screen, (0, 0, 0),(muisX, muisY, 60, 60))
    # pygame.draw.line(screen,(255, 255, 255), (muisX, muisY), (0, 0))
    # pygame.draw.line(screen,(255, 255, 255), (muisX + pen_brick_sizeX, muisY), (screenX, 0))

    # pygame.display.flip()
    # bereken lengte van stepper 1
    line1_1 = (muisX, muisY)
    line1_2 = (0, 0)
    line1 = distance.euclidean(line1_1, line1_2)

    # goto(muisX, muisY)

    # print(line1)

    # bereken lengte van stepper 2
    line2_1 = (muisX + pen_brick_sizeX, muisY)
    line2_2 = (screenX, 0)
    line2 = distance.euclidean(line2_1, line2_2)

    # print(line2)


def Start(Sel, pen_brick_sizeX_, pen_brick_sizeY_, screenX_, background_color_, screen):

    # calculate time it takes to complete the drawing
    # store current time in variable
    start_time = time.time()
    gcode = Load_fig(Sel)

    for x in range(len(gcode)):
        # print(gcode[x])
        if "G61" in gcode[x]:
            print("homing")
            PenUp()
            Home()
        elif "M3" in gcode[x]:
            print("pen down")
            PenDown()
        elif "M5" in gcode[x]:
            print("pen up")
            PenUp()
        elif "X" in gcode[x]:
            #print("moving pen:")
            coord = re.findall(r'[XY].?\d+.\d+', gcode[x])
            #print("X: " + gcode[x][1:8] + " Y: " + gcode[x][10:18])
            pos_x = float(coord[0].replace("X", "").replace(",", "."))
            pos_y = float(coord[1].replace("Y", "").replace(",", "."))
            # print(pos_x)
            # print(pos_y)
            MoveCalc(pos_x, pos_y, pen_brick_sizeX_, pen_brick_sizeY_,
                     screenX_, background_color_, screen)
        # print progress bar and time to complete
        print("---Progress: " + str(x) + "/" + str(len(gcode)) +
              " %s seconds ---" % (time.time() - start_time))


PenUp()
Start(input("name of gcode file:"), pen_brick_sizeX_,
      pen_brick_sizeY_, screenX_, background_color_, screen)


while running:

    pygame.display.flip()
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
