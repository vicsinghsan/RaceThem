import pygame
import time
import random

pygame.init()

display_width=800
display_hieght=600

black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
car_width=73
car_hieght=170

disp=pygame.display.set_mode((display_width,display_hieght))
pygame.display.set_caption("Race!!")
clock=pygame.time.Clock()

cimg=pygame.image.load("car.png")

def car(x,y):
    disp.blit(cimg,(x,y))
    
def things(thingx,thingy,thingw,thingh,color):
    pygame.draw.rect(disp,color,[thingx,thingy,thingw,thingh])

def text_objects(text,font):
    textsurface=font.render(text,True,red)
    return textsurface,textsurface.get_rect()

def message_display(text):
    largeText=pygame.font.Font("freesansbold.ttf",40)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center=((display_width/2),(display_hieght/2))
    disp.blit(TextSurf,TextRect)
    pygame.display.update()
    time.sleep(3)
    game_loop() 

def crash():
    message_display("Miss Nancy. You Crashed!! ")

    
def game_loop():
    x=(display_width * 0.33)
    y=(display_hieght * 0.8)

    x_change=0
    y_change=0
    thing_startx=random.randrange(0,display_width)
    thing_starty=-600
    thing_speed=7
    thing_width=100
    thing_hieght=100


    gameExit=False
    while not gameExit:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key ==pygame.K_UP:
                    y_change = -5
                if event.key ==pygame.K_DOWN:
                    y_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0


                

        x+=x_change
        y+=y_change

                
        disp.fill(white)
        things(thing_startx,thing_starty,thing_width,thing_hieght,black)
        thing_starty +=thing_speed

        
        car(x,y)
        
        if x>display_width-car_width or x<0:
            crash()

        if thing_starty>display_hieght:
            
            thing_starty=0-thing_hieght
            thing_startx=random.randrange(0,display_width)
            
        pygame.display.update()
        clock.tick(70)
game_loop()
pygame.quit()
quit()
