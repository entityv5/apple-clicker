import pygame
from utils.initialSetup import *
from utils.upgradeFuncs import handleUpgrades
from utils.gameProgressFuncs import handleGameProgressButtonClicks
from utils.refreshItemsFuncs import refreshMainMenu, refreshScreen
from utils.gameProgressFuncs import saveProgress


def main():
    pygame.init()

    # initial setup in utils/initalSetup.py

    clock = pygame.time.Clock()
    running = True
    onMainMenu = True
    tick = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               running = False

            elif event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                handleUpgrades()
                handleGameProgressButtonClicks()

        
        while onMainMenu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    onMainMenu = False
                    running = False

                elif event.type == pygame.VIDEORESIZE:
                    screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mousePosition = pygame.mouse.get_pos()

                    if startButtonRect.collidepoint(mousePosition):
                        onMainMenu = False


            refreshMainMenu()
            pygame.display.update()

            clock.tick(60)

        # save game every 30 seconds
        tick += 1
         
        if tick >= 1800:
            saveProgress()
            tick = 0


        refreshScreen()
        pygame.display.update()
        
        clock.tick(60)


    pygame.quit()


if __name__ == "__main__":
    main()
