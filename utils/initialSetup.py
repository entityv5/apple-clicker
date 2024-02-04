import pygame
from utils.data import *
from utils.classes import *
from utils.miscFuncs import formatNumber


pygame.init()

screen = pygame.display.set_mode((640, 480))

mainMenu = pygame.surface.Surface((640, 480), pygame.SRCALPHA)
mainMenuBackground = pygame.image.load("assets/images/mainMenu/background.png")
mainMenuTitle = pygame.image.load("assets/images/mainMenu/title.png")
mainMenuStartButton = pygame.image.load("assets/images/mainMenu/startButton.png")
startButtonRect = mainMenuStartButton.get_rect(topleft = (156, 257))
mainMenu.blit(mainMenuBackground, (0, 0))
mainMenu.blit(mainMenuTitle, (0, 0))
mainMenu.blit(mainMenuStartButton, (0, 0))

clickObject = pygame.surface.Surface((243, 263), pygame.SRCALPHA)
clickObjectImage = pygame.image.load("assets/images/game/clickObject.png")
clickSoundEffect = pygame.mixer.Sound("assets/clickSound.wav")
clickObjectRect = clickObject.get_rect(topleft = (25, 100))
clickObject.blit(clickObjectImage, (0, 0))

appleCount = pygame.font.Font("assets/Dosis.ttf", 36)
totalAps = pygame.font.Font("assets/Dosis.ttf", 24)
upgradeMenu = pygame.font.Font("assets/Dosis.ttf", 37)
appleCountText = appleCount.render(f"""Apples: {formatNumber(values["apples"])}""", True, (71, 99, 168))
totalApsText = totalAps.render(f"""Total APS: {formatNumber(sum(values[upgrade.upgradeName] * upgrade.baseAps * 60 for upgrade in automaticUpgrades))}""", True, (71, 99, 168))
upgradeMenuText = upgradeMenu.render("Upgrades", True, (135, 93, 156))

saveProgressButton = pygame.surface.Surface((150, 50))
wipeProgressButton = pygame.surface.Surface((150, 50))
saveProgressImage = pygame.image.load("assets/images/game/saveProgressButton.png")
wipeProgressImage = pygame.image.load("assets/images/game/wipeProgressButton.png")
saveProgressButtonRect = saveProgressButton.get_rect(topleft = (310, 425))
wipeProgressButtonRect = wipeProgressButton.get_rect(topleft = (480, 425))
saveProgressButton.blit(saveProgressImage, (0, 0))
wipeProgressButton.blit(wipeProgressImage, (0, 0))