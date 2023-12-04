import pandas as pd

# Create the dataframe
games = pd.DataFrame({
    "id": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "team": ["Milano 3", "Offanengo", "Crema", "Somaglia", "Borghebasket", "Locate", "Dresano", "Baby Santos", "Canottieri"],
    "at_home": [1, 0, 1, 0, 1, 0, 1, 0, 0],
    "points_gsqsa": [63, 71, 83, 73, 62, 81, 64, 72, 64],
    "points_opponent": [54, 66, 53, 59, 52, 61, 22, 70, 55],
    "win": [1, 1, 1, 1, 1, 1, 1, 1, 1],
})

# save on github
games.to_csv("db/games.csv", sep=";", index=False)
