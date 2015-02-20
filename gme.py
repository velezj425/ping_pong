### Skeleton code for pong game

import pygame, sys
from pygame.locals import *

# Number of frames per second
# Change this value to speed up or slow down your game
FPS = 200

#Global Variables to be used through our program
WINDOWWIDTH = 400
WINDOWHEIGHT = 300
LINETHICKNESS = 10
PADDLESIZE = 50
PADDLEOFFSET = 20

# Set up the colours
BLACK     = (0  ,0  ,0  )
WHITE     = (255,255,255)

#Draws the arena the game will be played in. 
def drawArena():
    DISPLAYSURF.fill((0,0,0))
    #Draw outline of arena
    pygame.draw.rect(DISPLAYSURF, WHITE, ((0,0),(WINDOWWIDTH,WINDOWHEIGHT)), LINETHICKNESS*2)
    #Draw centre line
    pygame.draw.line(DISPLAYSURF, WHITE, ((WINDOWWIDTH/2),0),((WINDOWWIDTH/2),WINDOWHEIGHT), (LINETHICKNESS/4))

#Draws the paddle
def drawPaddle(paddle):
    #Stops paddle moving too low
    if paddle.bottom > WINDOWHEIGHT - LINETHICKNESS:
        paddle.bottom = WINDOWHEIGHT - LINETHICKNESS
    #Stops paddle moving too high
    elif paddle.top < LINETHICKNESS:
        paddle.top = LINETHICKNESS
    #Draws paddle
    pygame.draw.rect(DISPLAYSURF, WHITE, paddle)
  
#draws the ball
def drawBall(ball):
    pygame.draw.rect(DISPLAYSURF, WHITE, ball)

#Main function
def main():
    pygame.init()
    global DISPLAYSURF

    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT)) 
    pygame.display.set_caption('Pong')

    #Initiate variable and set starting positions
    #any future changes made within rectangles
    ballX = WINDOWWIDTH/2 - LINETHICKNESS/2
    ballY = WINDOWHEIGHT/2 - LINETHICKNESS/2
    playerOnePosition = (WINDOWHEIGHT - PADDLESIZE) /2
    playerTwoPosition = (WINDOWHEIGHT - PADDLESIZE) /2

    #Creates Rectangles for ball and paddles.
    paddle1 = pygame.Rect(PADDLEOFFSET,playerOnePosition, LINETHICKNESS,PADDLESIZE)
    paddle2 = pygame.Rect(WINDOWWIDTH - PADDLEOFFSET - LINETHICKNESS, playerTwoPosition, LINETHICKNESS,PADDLESIZE)
    ball = pygame.Rect(ballX, ballY, LINETHICKNESS, LINETHICKNESS)

    #Draws the starting position of the Arena
    drawArena()
    drawPaddle(paddle1)
    drawPaddle(paddle2)
    drawBall(ball)

    while True: #main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        drawArena()
        drawPaddle(paddle1)
        drawPaddle(paddle2)
        drawBall(ball)

        pygame.display.update()
        FPSCLOCK.tick(FPS)

# this is a prototype code for the start menu in the pong game:
#It will have 4 options; Single Player (AI controlled), Multiplayer (Same keyboard), High Scores (From MongoDB), Options (Player colors, Difficulty(?) )

def Main_Menu():
    #Menu triggers, when true, the program should call the function that corresponds to the option (single = single player, multi = multiplayer etc.)
    single = False
    multi = False
    Scores = False
    Settings = False

    #Sets the screen size and updates accordingly
    #DisplaySurface(or whatever variable name is decided upon) should be a global variable so that we are all using the same display and not creating different ones
    DisplaySurface = pygame.display.set_mode((1280, 720))
    pygame.display.update()

    #Gives the main menu colors (White for text, Red for arrows) named attributes
    White = (255, 255, 255)
    Red = (255, 0, 0)

    #Declares DisplaySurface as global so the screen size does not change from function to function
    global DisplaySurface

    #FPS clock, may be different from method/function FPS clocks
    FPStimer = pygame.time.Clock()

    DisplaySurface.fill((0, 0, 0))

    Arrow_Position1 = 220
    Arrow_Position2 = 210
    Arrow_Position3 = 230
    Arrow_Position4 = 200 

    #Menu loop
    while single == False and multi == False and Scores == False and Settings == False:
        #Draws the title above the menu
            #Draws the 'P' in pong master
            DisplaySurface.fill((0, 0, 0))
            pygame.draw.rect(DisplaySurface, White, ( (213, 150), (854, 20) ) )

            #Sets the font for the title to 86 pixels high and standard font
            font = pygame.font.Font(None, 86)
    
            #prints the title
            text = font.render("Ping Pong Master", False, White, (0, 0, 0))
    
            #sets the subtext for the title to 32 pixels high
            font = pygame.font.Font(None, 32)
            font.set_italic(True)
            Extreme = font.render("Game of the Year Edition", False, White, (0, 0, 0) )
    
        #Sets the font size for the rest of the menu items to 72px
            font = pygame.font.Font(None, 72)
            Single_Player = font.render("Single Player", False, White, (0, 0, 0) )
    
            Multiplayer = font.render("Multiplayer", False, White, (0, 0, 0) )
    
            High_Scores = font.render("High Scores", False, White, (0, 0, 0) )
    
            Options = font.render("Options", False, White, (0, 0, 0) )
    
            DisplaySurface.blit(Options, (500, 500))
            DisplaySurface.blit(High_Scores, (500, 400) )
            DisplaySurface.blit(Multiplayer, (500, 300))
            DisplaySurface.blit(Single_Player, (500, 200))
            DisplaySurface.blit(text, (213, 100))
            DisplaySurface.blit(Extreme, (727, 120))
    
            #Draws the red selection arrow and determines the location with Arrow_Position
            pygame.draw.rect(DisplaySurface, Red, ( ( 400, Arrow_Position1), (70, 10) ) )
            pygame.draw.rect(DisplaySurface, Red, ( ( 400, Arrow_Position2), (60, 10) ) )
            pygame.draw.rect(DisplaySurface, Red, ( ( 400, Arrow_Position3), (60, 10) ) )
            pygame.draw.rect(DisplaySurface, Red, ( ( 440, Arrow_Position4), (10, 50) ) )
            pygame.display.update()
    
    
            for event in pygame.event.get():
                #Senses when a key is pressed
                if event.type == pygame.KEYDOWN:
                    #Allows downward movement of the arrow and restricts movement past the last item in the screen (Options)
                    if event.key == pygame.K_DOWN and Arrow_Position1 != 520:
                        Arrow_Position1 += 100
                        Arrow_Position2 += 100
                        Arrow_Position3 += 100
                        Arrow_Position4 += 100
            
                        #Allow upward movement of the arrow and restricts movement past the first item in the screen (Single Player)
                    elif event.key == pygame.K_UP and Arrow_Position1 != 220:
                        Arrow_Position1 -= 100
                        Arrow_Position2 -= 100
                        Arrow_Position3 -= 100
                        Arrow_Position4 -= 100
                
                        #Determines what option the user picked when they hit enter(return) on their keyboard 
                    elif event.key == pygame.K_RETURN and Arrow_Position1 == 220:
                        single = True
                    elif event.key == pygame.K_RETURN and Arrow_Position1 == 320:
                        multi = True
                    elif event.key == pygame.K_RETURN and Arrow_Position1 == 420:
                        Scores = True
                    elif event.key == pygame.K_RETURN and Arrow_Position1 == 520:
                        Settings = True
            
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

    #When the single player in built, this function will call it at this point. When the single player match ends, a menu should appear saying something like:
    #"Rematch or Main Menu" at which point it will call this function all over again.

if __name__=='__main__':
    main()