import pandas as pd


df = pd.read_csv("assets/saveData.csv")

values = {
    "apples": df["apples"].iloc[0],
    "fractionalApples": df["fractionalApples"].iloc[0],
    "appleLevel": df["appleLevel"].iloc[0],
    "autoclickers": df["autoclickers"].iloc[0],
    "farmerJoes": df["farmerJoes"].iloc[0],
    "newtonsTrees": df["newtonsTrees"].iloc[0]
}