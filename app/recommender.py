from .data_loader import load_games
from .models import UserData

# Chargement initial du dataset
games_df = load_games()

def generate_recommendations(user_data: UserData):
    """
    Recommande des jeux en fonction des catégories des jeux déjà achetés.
    - 1. Récupère les jeux achetés
    - 2. Déduit leurs catégories
    - 3. Propose d'autres jeux de ces catégories
    """
    purchased_ids = {purchase.game_id for purchase in user_data.purchases}

    # Catégories des jeux achetés
    purchased_categories = games_df[games_df['game_id'].isin(purchased_ids)]['category'].unique()

    # Jeux similaires à recommander
    recommended_games = games_df[
        (games_df['category'].isin(purchased_categories)) &
        (~games_df['game_id'].isin(purchased_ids))
    ]

    # Construction du résultat
    return [
        {
            "game_id": int(row['game_id']),
            "game_name": row['game_name'],
            "category": row['category']
        }
        for _, row in recommended_games.iterrows()
    ]
