# GamesUP - API de Recommandation (FastAPI + Python)

## Description
Ce module Python fait partie du projet GamesUP. Il expose une API de recommandation de jeux à partir de l'historique d'achat d'un utilisateur, grâce à FastAPI. 

Les données sont chargées depuis un fichier CSV simulant la base des jeux. L'algorithme de recommandation est basé sur la similarité de catégorie des jeux déjà achetés.

---

## Stack utilisée
- Python 3.13
- FastAPI
- Uvicorn (serveur)
- Pandas

---

## Structure du projet

```
CodeApiPython/
├── app/
│   ├── __init__.py                  # Dossier reconnu comme package
│   ├── main.py                      # API FastAPI
│   ├── models.py                    # Modèles Pydantic
│   ├── recommendation.py            # Algorithme principal
│   └── data_loader.py               # Chargement du dataset
│
├── datasets/
│   └── games.csv                  # Données simulées des jeux (game_id, name, category)
│
├── venv/                            # Environnement virtuel Python (non versionné)
├── requirements.txt                # Dépendances Python
└── README.md                     # Documentation (ce fichier)
```

---

## Installation et lancement

### 1. Cloner le projet et se placer dans le dossier :
```bash
cd CodeApiPython
```

### 2. Créer et activer un environnement virtuel :
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Installer les dépendances :
```bash
pip install -r requirements.txt
```

### 4. Lancer l'API FastAPI :
```bash
uvicorn app.main:app --reload
```

- Accueil : [http://localhost:8000](http://localhost:8000)
- Swagger : [http://localhost:8000/docs](http://localhost:8000/docs)

---

## Endpoint principal

### `POST /recommendations`
Retourne des recommandations de jeux similaires à ceux achetés (même catégorie).

#### Exemple de body JSON :
```json
{
  "user_id": 1,
  "purchases": [
    { "game_id": 1, "rating": 4.5 },
    { "game_id": 3, "rating": 5.0 }
  ]
}
```

#### Exemple de réponse :
```json
{
  "recommendations": [
    { "game_id": 2, "game_name": "Carcassonne", "category": "Stratégie" },
    { "game_id": 5, "game_name": "7 Wonders", "category": "Stratégie" },
    { "game_id": 6, "game_name": "Splendor", "category": "Famille" }
  ]
}
```

---

## Détail de l'algo actuel (`recommendation.py`)

- Récupère les `game_id` achetés par l'utilisateur
- Détermine leurs catégories depuis le `games.csv`
- Retourne tous les jeux de ces catégories (hors ceux déjà achetés)

---

## 📖 Exemple de contenu `datasets/games.csv`
```csv
game_id,game_name,category
1,Catan,Stratégie
2,Carcassonne,Stratégie
3,Dixit,Famille
4,Azul,Abstrait
5,7 Wonders,Stratégie
6,Splendor,Famille
```
