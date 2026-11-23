# Bike Sharig

TÉMA: A féléves feladat során az UCI Machine Learning Repository nyilvános Bike Sharing Dataset adathalmazát felhasználva vizsgáljuk, hogy az időjárási körülmények, az évszakok, a napszakok és a munkanapok milyen hatással vannak a kerékpárkölcsönzések számára. A feladat során különböző regressziós gépi tanulási modelleket (lineáris regresszió, döntési fa, Random Forest) alkalmazunk, majd a modellek előrejelzési teljesítményét MAE, RMSE és R² metrikák segítségével értékeljük és hasonlítsuk össze.

## Az eddigi program futtatása

A program Python 3.13-mal készült. A parancsokat a projekt mappájában kell futtatni.

macOS és Linux:

```bash
python3.13 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python 01_adatok_megnezese.py
```

A Jupyter Notebook indítása ugyanebből a mappából:

```bash
.venv/bin/python -m notebook
```

Windows:

```powershell
py -3.13 -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe 01_adatok_megnezese.py
```

A Jupyter Notebook indítása Windows alatt:

```powershell
.venv\Scripts\python.exe -m notebook
```

## Az adatok átadása a modelleknek

Az `adatok_megismerese.ipynb` notebook tartalmazza az adatok ellenőrzését és az ábrákat. A mentett ábrák a `figures/` mappában találhatók.

A `data_preparation.py` az időrendben szétválasztott adatokat és a kategóriák kódolásához szükséges előfeldolgozót biztosítja:

```python
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline

from data_preparation import adatok_elokeszitese, elofeldolgozo_letrehozasa

X_tanito, X_teszt, y_tanito, y_teszt = adatok_elokeszitese()
modell = Pipeline([
    ("elofeldolgozas", elofeldolgozo_letrehozasa()),
    ("modell", LinearRegression()),
])
modell.fit(X_tanito, y_tanito)
```

Az előfeldolgozót a modell pipeline-jában kell használni, hogy időrendi keresztvalidáció során minden körben csak az adott tanítórészből tanuljon. A végső tesztadatok a modellválasztás után használhatók a kiértékeléshez.

## Adatforrás

Az óránkénti adatokat a `data/hour.csv` fájl tartalmazza. Forrás: Fanaee-T, H. (2013), [Bike Sharing](https://doi.org/10.24432/C5W894), UCI Machine Learning Repository. Az adathalmaz licence CC BY 4.0. Az eredeti leírás a `data/Readme.txt` fájlban található.
