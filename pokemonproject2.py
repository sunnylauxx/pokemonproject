import pygame
import random


pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A bit Racey')

pokemonImg = pygame.image.load('pikachu.png')
playerImg = pygame.image.load('player.png')

pygame.display.set_icon(playerImg)

def pok(x, y):
    #gameDisplay.blit(pokemonImg, (x, y))
    gameDisplay.blit(pygame.transform.scale(pokemonImg, (100,100)),(x,y))

def pla(x, y):
    gameDisplay.blit(pygame.transform.scale(playerImg, (75, 150)), (x, y))

def caught():
    fg = 250, 240, 230
    bg = 5, 5, 5
    text = "congratulations! You caught the pokemon!"
    font = pygame.font.Font(None, 80)
    ren = font.render(text, 0, fg, bg)
    gameDisplay.blit(ren,(10,10))





def game_loop():

    ############

    ############
    x = (display_width * 0.45)
    y = (display_height * 0.3)

    x_change = 0
    y_change = 0

    px = (display_width * 0.30)
    py = (display_height * 0.50)

    px_change = 0
    py_change = 0



    gameExit = False
    catch = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_change = -5
                if event.key == pygame.K_DOWN:
                    y_change = 5
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_p:
                    pause = True
                   # paused()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0


        x += x_change
        gameDisplay.fill(white)
        y += y_change

        px_change = random.randrange(-50,50)
        py_change = random.randrange(-50, 50)
        px += px_change
        py += py_change

        if x > px and x < px+100 and y > py and y < py+100:
            catch = True
        if catch == True:
            caught()
        pok(px, py)
        pla(x,y)





        pygame.display.update()


game_loop()