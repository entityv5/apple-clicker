import pygame
from utils.data import *
from utils.classes import *
from utils.initialSetup import *
from utils.miscFuncs import formatNumber


pygame.init()


def checkForClickObjectCollision(mousePosition):
    if clickObjectRect.collidepoint(mousePosition):
        clickSoundEffect.play()
        values["apples"] += appleUpgrade.baseAps + values["appleLevel"]
        appleCountText = appleCount.render(f"""Apples: {formatNumber(values["apples"])}""", True, (71, 99, 168))


def performUpgrade(sprite):
    price = int(sprite.basePrice * 1.15 ** values[sprite.upgradeName])

    if values["apples"] >= price:
        values["apples"] -= price
        values[sprite.upgradeName] += 1

        sprite.levelDisplayText = sprite.levelDisplay.render(f"""Level: {formatNumber(values[sprite.upgradeName])}""", True, (0, 0, 0))
        sprite.priceDisplayText = sprite.priceDisplay.render(f"Price: {formatNumber(sprite.basePrice * 1.15 ** values[sprite.upgradeName])}", True, (0, 0, 0))

        if sprite == appleUpgrade:
            sprite.ApsDisplayText = sprite.ApsDisplay.render(f"""APC: {formatNumber(sprite.baseAps + values[sprite.upgradeName])}""", True, (0, 0, 0))

        else:
            sprite.ApsDisplayText = sprite.ApsDisplay.render(f"""APS: {formatNumber(sprite.baseAps * values[sprite.upgradeName] * 60)}""", True, (0, 0, 0))


def checkForUpgradeButtonClick(mousePosition):
    clickedSprites = [instance for instance, rect in upgradeButton.instances if rect.collidepoint(mousePosition)]

    if clickedSprites:
        sprite = clickedSprites[0]
        performUpgrade(sprite)


def handleUpgrades():
    mousePosition = pygame.mouse.get_pos()

    checkForClickObjectCollision(mousePosition)

    if not clickObjectRect.collidepoint(mousePosition):
        checkForUpgradeButtonClick(mousePosition)