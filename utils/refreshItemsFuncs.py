import pygame
from utils.data import *
from utils.classes import *
from utils.initialSetup import *
from utils.miscFuncs import formatNumber, addApples


pygame.init()


def refreshUpgradeButtons(upgrade, levelOffset, priceOffset, ApsOffset):
    screen.blit(upgrade.surface, upgrade.offset)
    screen.blit(upgrade.levelDisplayText, levelOffset)
    screen.blit(upgrade.priceDisplayText, priceOffset)
    screen.blit(upgrade.ApsDisplayText, ApsOffset)


def refreshAllUpgradeButtons():
    refreshUpgradeButtons(appleUpgrade, (158, 425), (158, 440), (120, 455))
    refreshUpgradeButtons(autoclickerUpgrade, (523, 65), (523, 80), (485, 95))
    refreshUpgradeButtons(farmerJoeUpgrade, (523, 150), (523, 165), (485, 180))
    refreshUpgradeButtons(newtonsTreesUpgrade, (523, 235), (518, 250), (485, 265))


def refreshMainMenu():
    screen.blit(mainMenuBackground, (0, 0))
    screen.blit(mainMenuTitle, (81, 36))
    screen.blit(mainMenuStartButton, (156, 257))


def refreshScreen():
        appleCountText = appleCount.render(f"""Apples: {formatNumber(values["apples"])}""", True, (71, 99, 168))
        totalApsText = totalAps.render(f"""Total APS: {formatNumber(sum(values[upgrade.upgradeName] * upgrade.baseAps * 60 for upgrade in automaticUpgrades))}""", True, (71, 99, 168))
        
        screen.fill((200, 200, 200))
        screen.blit(clickObject, (25, 100))
        screen.blit(appleCountText, (0, 0))
        screen.blit(totalApsText, (0, 47))
        screen.blit(upgradeMenuText, (452, -8))
        screen.blit(saveProgressButton, (310, 425))
        screen.blit(wipeProgressButton, (480, 425))

        refreshAllUpgradeButtons()

        for upgrade in automaticUpgrades:
            addApples(upgrade)