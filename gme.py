'''
Created on Feb 10, 2015

@author: MARIOA
'''
from random import randint

import pygame, sys

pygame.init()
clock = pygame.time.Clock()

#defining colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)


gameDisplay = pygame.display.set_mode((1200, 720))
pygame.display.set_caption("New Python Game")
#updates the game display with the changes added to them

gameExit = False

ball_x = 600
ball_y = 360

lead_y = 300
lead_y_change = 0

lead_y2 = 300
lead_y2_change = 0

if randint(0,1) == 1:
        ball_x += 20
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
            
#Gives movement to the rectangle when the correct key is pressed down
        if event.type == pygame.KEYDOWN:
            if event.key ==pygame.K_UP:
                lead_y_change -= 15
            if event.key == pygame.K_DOWN:
                lead_y_change += 15
            if event.key == pygame.K_w:
                lead_y2_change -= 15
            if event.key == pygame.K_s:
                lead_y2_change += 15
                
    #tells the program to stop the moving rectangle when the key currently being held is let go
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                lead_y2_change = 0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                lead_y_change = 0

    
    if ( (ball_x >= 1170) or (ball_x <= 30) ): # ( (ball_y == lead_y ) or (ball_y == lead_y2) ):
            ball_x *= -1
            print "true"
            
    else:
            ball_x += 20
            print "false"
    
    lead_y += lead_y_change
    lead_y2 += lead_y2_change
    
    
    
    #Gives the black background 
    gameDisplay.fill(black)
    
    #Player 2 location
    pygame.draw.rect(gameDisplay, white, [0, lead_y2, 30, 100])
    
    #Player 1 location
    pygame.draw.rect(gameDisplay, white, [1170, lead_y, 30, 100])
    
    #ball location
    pygame.draw.rect(gameDisplay, white, [ball_x, ball_y, 20, 20])
    pygame.display.update()
    clock.tick(30)
    print event

#exits pygame
pygame.quit()
quit()
sys.exit()
