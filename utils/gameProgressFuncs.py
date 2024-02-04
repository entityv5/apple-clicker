from utils.data import *
from utils.classes import *
from utils.initialSetup import *
from utils.refreshItemsFuncs import refreshAllUpgradeButtons
from utils.miscFuncs import formatNumber


def saveProgress():
    df.loc[0, "apples"] = values["apples"]
    df.loc[0, "fractionalApples"] = values["fractionalApples"]
    df.loc[0, "appleLevel"] = values["appleLevel"]
    df.loc[0, "autoclickers"] = values["autoclickers"]
    df.loc[0, "farmerJoes"] = values["farmerJoes"]
    df.loc[0, "newtonsTrees"] = values["newtonsTrees"]

    df.to_csv("assets/saveData.csv", index=False)


def wipeProgress():
    for value in values:
        values[value] = 0

    for upgrade in allUpgrades:
        upgrade.levelDisplayText = upgrade.levelDisplay.render(f"""Level: {formatNumber(values[upgrade.upgradeName])}""", True, (0, 0, 0))
        upgrade.priceDisplayText = upgrade.priceDisplay.render(f"Price: {formatNumber(upgrade.basePrice * 1.15 ** values[upgrade.upgradeName])}", True, (0, 0, 0))
        
        if upgrade == appleUpgrade:
            upgrade.ApsDisplayText = upgrade.ApsDisplay.render(f"""APC: {formatNumber(upgrade.baseAps + values[upgrade.upgradeName])}""", True, (0, 0, 0))
        
        else: upgrade.ApsDisplayText = upgrade.ApsDisplay.render(f"""APS: {formatNumber(upgrade.baseAps * values[upgrade.upgradeName] * 60)}""", True, (0, 0, 0))


    saveProgress()
    refreshAllUpgradeButtons()


def handleGameProgressButtonClicks():
    mousePosition = pygame.mouse.get_pos()

    if saveProgressButtonRect.collidepoint(mousePosition):
        saveProgress()

    elif wipeProgressButtonRect.collidepoint(mousePosition):
        wipeProgress()