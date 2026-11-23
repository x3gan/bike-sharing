from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split


def adatok_elokeszitese():
    fajl = Path(__file__).resolve().parent / "data" / "hour.csv"
    adatok = pd.read_csv(fajl)
    adatok = adatok.sort_values(["dteday", "hr"]).reset_index(drop=True)

    X = adatok.drop(columns=["instant", "dteday", "casual", "registered", "cnt"])
    y = adatok["cnt"]

    return train_test_split(X, y, test_size=0.2, shuffle=False)

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder


def elofeldolgozo_letrehozasa():
    kategoriak = ["season", "mnth", "hr", "weekday", "weathersit"]

    return ColumnTransformer(
        [("kategoriak", OneHotEncoder(handle_unknown="ignore"), kategoriak)],
        remainder="passthrough",
    )
