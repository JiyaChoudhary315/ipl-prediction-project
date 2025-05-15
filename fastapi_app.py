from fastapi import FastAPI
# import joblib  # Uncomment this later when you have your model

app = FastAPI()

# model = joblib.load("match_model.pkl")  # Comment this out for now if the model is not ready

@app.get("/predict/")
def predict(team1: str, team2: str, venue: str):
    # Dummy response for now
    return {"winner": "Team A", "score_prediction": "175-165"}
