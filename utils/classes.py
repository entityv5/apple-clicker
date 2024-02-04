import pygame
from utils.data import *
from utils.miscFuncs import formatNumber


pygame.init()

# APS = apples per second
# APC = apples per click
# game runs at 60fps so whenever Aps is mentioned outside of the game, it will be 60 times less than what it actually is
class upgradeButton:
    instances = []

    def __init__(self, upgradeName, surfaceSize, imagePath, offset, basePrice, baseAps):
        self.upgradeName = upgradeName
        self.surfaceSize = surfaceSize
        self.imagePath = imagePath
        self.offset = offset
        self.basePrice = basePrice
        self.baseAps = baseAps

        self.surface = pygame.surface.Surface(self.surfaceSize)
        self.image = pygame.image.load(self.imagePath)
        self.rect = self.surface.get_rect(topleft = self.offset)
        self.surface.blit(self.image, (0, 0))
        self.levelDisplay = pygame.font.Font(None, 16)
        self.priceDisplay = pygame.font.Font(None, 16)
        self.ApsDisplay = pygame.font.Font(None, 16)
        self.levelDisplayText = self.levelDisplay.render(f"""Level: {formatNumber(values[self.upgradeName])}""", True, (0, 0, 0))
        self.priceDisplayText = self.priceDisplay.render(f"Price: {formatNumber(self.basePrice * 1.15 ** values[self.upgradeName])}", True, (0, 0, 0))

        if self.upgradeName != "appleLevel":
            self.ApsDisplayText = self.ApsDisplay.render(f"""APS: {formatNumber(self.baseAps * values[self.upgradeName] * 60)}""", True, (0, 0, 0))
        
        else: self.ApsDisplayText = self.ApsDisplay.render(f"""APC: {formatNumber(self.baseAps + values[self.upgradeName])}""", True, (0, 0, 0))
        
        self.__class__.instances.append((self, self.rect))


appleUpgrade = upgradeButton("appleLevel", (250, 75), "assets/images/game/appleUpgrade.png", (20, 400), 50, 1) # baseAps will act as a baseApc for this upgrade
autoclickerUpgrade = upgradeButton("autoclickers", (250, 75), "assets/images/game/autoclickerUpgrade.png", (385, 40), 100, 0.0167)
farmerJoeUpgrade = upgradeButton("farmerJoes", (250, 75), "assets/images/game/farmerJoeUpgrade.png", (385, 125), 540, 0.0667)
newtonsTreesUpgrade = upgradeButton("newtonsTrees", (250, 75), "assets/images/game/newtonsTreeUpgrade.png", (385, 210), 1700, 0.2)

automaticUpgrades = [autoclickerUpgrade, farmerJoeUpgrade, newtonsTreesUpgrade]
allUpgrades = [appleUpgrade, autoclickerUpgrade, farmerJoeUpgrade, newtonsTreesUpgrade]