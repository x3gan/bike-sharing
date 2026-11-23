import pandas as pd

adatok = pd.read_csv("data/hour.csv")

print("Sorok és oszlopok száma:", adatok.shape)
print(adatok[["dteday", "hr", "temp", "cnt"]].head())
