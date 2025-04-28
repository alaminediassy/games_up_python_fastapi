from fastapi import FastAPI, HTTPException
from app.models import UserData
from app.recommendation import generate_recommendations

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API de recommandation opérationnelle"}

@app.post("/recommendations/")
def get_recommendations(data: UserData):
    try:
        result = generate_recommendations(data)
        return {"recommendations": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
