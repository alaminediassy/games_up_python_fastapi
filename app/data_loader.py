import pandas as pd

# Charge les jeux depuis un fichier CSV
def load_games(path="datasets/games.csv"):
    return pd.read_csv(path)
