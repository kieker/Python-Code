import random
import pygame
from pygame.locals import *
from player import Player
from Mole import Mole

pygame.init()

# Variables

debug_mode = True
display_width = 800
display_height = 600

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 200, 0)
lightgreen = (0,255,0)

largefont = pygame.font.SysFont(None, 48)
font = pygame.font.SysFont(None, 32)
smallfont = pygame.font.SysFont(None, 24)

score = 0
clock = pygame.time.Clock()
fps = 30
max_mole = 4
time = 30
timeleft = time

# Functions

def disp_message(msg,color,disp = (0,0),size = "small"):
    if size == "small":
        textSurface = smallfont.render(msg,True,color)
    elif size == "med":
        textSurface = font.render(msg,True,color)
    else:
        textSurface = largefont.render(msg,True,color)

    textsurface_rect = textSurface.get_rect()
    textsurface_rect.center = (display_width/2+disp[0],display_height/2+disp[1])
    gamesurface.blit(textSurface,textsurface_rect)

def score_display():
    message_surface = font.render('Score : ' + str(score), True, black)
    gamesurface.blit(message_surface, [5, 15])


def time_display(timeleft):
    timeleftmultiplier = 100/time
    print(timeleftmultiplier)
    pygame.draw.rect(gamesurface,black,(display_width-130, 15,100,20),0)
    pygame.draw.rect(gamesurface, green, (display_width - 130, 15, timeleft*timeleftmultiplier, 20), 0)
    timer_surface = font.render('Time : ' + str(int(timeleft)), True, black)
    gamesurface.blit(timer_surface, [display_width-230, 15])


def game_over_display():
    pygame.mouse.set_visible(True)

    disp_message("Game Over",red,(0,-80),"large")
    disp_message("Your score is : " + str(score),white,(0,0))

    button("Play again",display_width/2-150,display_height/2+70,100,50,green,white,gameLoop)
    button("Quit", display_width / 2+10, display_height / 2+70, 100, 50, red, white,quit)

    pygame.display.update()


def generateRandomPos(mole):
        PosX = random.randrange(display_width - mole.rect.width)
        PosY = random.randrange(display_height - mole.rect.height)
        return PosX, PosY

def button(msg,x,y,w,h,ac,ic,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if w-10 <= len(msg):
        w = len(msg)+ 40

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gamesurface,ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gamesurface,ic,(x,y,w,h))

    buttonsurface = smallfont.render(msg,True,black)
    buttonsurface_pos = buttonsurface.get_rect()
    buttonsurface_pos.center = ((x+(w/2)), (y+(h/2)))
    gamesurface.blit(buttonsurface,buttonsurface_pos)



gamesurface = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Whack a Mole")
bg = pygame.image.load("images/ground-bgv2.jpg")


player1 = Player(gamesurface)
moleListIndex = 0


# mole_loop = 1
# while not moles_not_collide:
#     for mole in molelist:
#         if mole.detect_collision(molelist[mole_loop],debug_mode):
#             molelist[mole_loop].x, molelist[mole_loop].y = generateRandomPos()
#     mole_loop += 1
#     moles_not_collide = True

#TODO detect collision with other moles and regenerate position if needed


def gameIntro():
    intro = True
    gamesurface.fill(white)
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                    intro = False
                    gameLoop()

        disp_message("Whack-a-Mole",black,(0,-90),"large")
        disp_message("The goal of the game is to hit as many moles as you can within the time limit.", black, (0, -40),"med")
        disp_message("1 mole = 10 points", black,(0,0),"small")
        disp_message("Press enter or click the play button to begin",black,(0,50),"normal")
        button("Play!",display_width/2-75, display_height/2+150,150,50,lightgreen,green,gameLoop)

        pygame.display.update()
        clock.tick(15)

def endScreen():
    end = True
    while end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    gameLoop()

        gamesurface.fill(black)
        game_over_display()

def gameLoop():
    gameover = False
    gameExit = False

    global score
    global time
    score = 0
    time = 20

    start_ticks = pygame.time.get_ticks()

    molelist = [Mole(gamesurface) for i in range(max_mole)]

    for mole in molelist:
        mole.rect.x, mole.rect.y = generateRandomPos(mole)
        mole.time = random.randrange(100)

    while not gameExit:
        while gameover:
            endScreen()

        seconds = (pygame.time.get_ticks()-start_ticks)/1000

        timeleft = time - seconds
        if timeleft <= 0:
            gameover = True

        gamesurface.fill(white)
        gamesurface.blit(bg, (0,0))

        moleListIndex = 0
        pygame.mouse.set_visible(False)
        mousecoords = pygame.mouse.get_pos()


        while moleListIndex < len(molelist):
            currentmole = molelist[moleListIndex]
            currentmole.time += 1

            if currentmole.time - pygame.time.get_ticks()/1000 >= 200:
                if debug_mode:
                    print('mole will be deleted')
                del molelist[moleListIndex]
            moleListIndex += 1

        # Check if more moles should be generated
        if len(molelist) <= max_mole:
            molelist.append(Mole(gamesurface))
            i = len(molelist)-1
            molelist[i].rect.x, molelist[i].rect.y = generateRandomPos(molelist[i])
            molelist[i].time = pygame.time.get_ticks()/1000

        for mole in molelist:
            hit = player1.detect_collision(mole,debug_mode)
            mole.spriteanim()
            mole.spritehover(hit)

            if debug_mode:
                pass
                # print("Time: " + str(pygame.time.get_ticks()/1000) + " Mole time : " + str(mole.time) + " Mole pos x: " + str(mole.x) + " Mole pos y " + str(mole.y) )
            molecoords = (mole.rect.x, mole.rect.y)
            if mole.hp > 0:
                mole.drawmole(molecoords)
            else:
                del mole

        # Event Handling
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEMOTION:
                player1.placePlayer(mousecoords)
            if event.type == pygame.MOUSEBUTTONDOWN:
                player1.hitMallet(90, mousecoords)

            #TODO better handling of mole hit
            if event.type == pygame.MOUSEBUTTONUP:
                player1.hitMallet(-90, mousecoords)
                for mole in molelist:
                    if player1.detect_collision(mole, False):
                        mole.hp -= 1
                        if mole.hp <= 0:
                            score += 10
                            print('mole Hit!')


        #TODO Implement big mole enemies, and boss with loads of health

        score_display()
        time_display(timeleft)
        player1.placePlayer(mousecoords)
        pygame.display.update()

        clock.tick(fps)

    pygame.quit()
    quit()

gameIntro()
gameLoop()

