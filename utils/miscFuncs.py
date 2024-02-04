from utils.data import *


def formatNumber(number):
    suffixes = ["", "k", "m", "b"]

    index = 0

    if number >= 1000:
        while number >= 1000:
            number /= 1000
            index += 1

        return f"{number:.3f}{suffixes[index]}"
    
    else: return int(number)


def addApples(upgrade):
        if upgrade.baseAps * values[upgrade.upgradeName] < 1:
            values["fractionalApples"] += upgrade.baseAps * values[upgrade.upgradeName]
        
        else:
            values["apples"] += int(upgrade.baseAps * values[upgrade.upgradeName])

        if values["fractionalApples"] >= 1:
            values["apples"] += int(values["fractionalApples"])
            values["fractionalApples"] -= values["fractionalApples"]