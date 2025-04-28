from .data_loader import load_games
from .models import UserData

# Chargement initial du dataset de jeux
games_df = load_games()


def generate_recommendations(user_data: UserData):
    """
    Génère une liste de jeux recommandés à partir des catégories des jeux achetés.

    Étapes :
    - 1. Récupérer les IDs des jeux achetés par l'utilisateur
    - 2. Identifier les catégories associées à ces jeux
    - 3. Recommander d'autres jeux dans ces catégories non encore achetés
    """

    # IDs des jeux achetés
    purchased_ids = {purchase.game_id for purchase in user_data.purchases}

    # Catégories correspondant aux jeux achetés
    purchased_categories = games_df[games_df['game_id'].isin(purchased_ids)]['category'].unique()

    # Sélection des jeux recommandés : même catégorie, pas encore achetés
    recommended_games = games_df[
        (games_df['category'].isin(purchased_categories)) &
        (~games_df['game_id'].isin(purchased_ids))
        ]

    # Construction du résultat sous forme de liste de dictionnaires
    return [
        {
            "game_id": int(row['game_id']),
            "game_name": row['game_name'],
            "category": row['category']
        }
        for _, row in recommended_games.iterrows()
    ]
