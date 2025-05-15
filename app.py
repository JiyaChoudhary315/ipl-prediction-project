from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('ipl-prediction/ipl_match_winner_model.joblib')


# Define the request format
class MatchInput(BaseModel):
    team1_encoded: int
    team2_encoded: int

# Create the FastAPI app
app = FastAPI()

# Define the prediction endpoint
@app.post("/predict")
def predict_winner(input_data: MatchInput):
    data = pd.DataFrame([[input_data.team1_encoded, input_data.team2_encoded]],
                        columns=['team1_encoded', 'team2_encoded'])
    prediction = model.predict(data)
    return {"predicted_winner": prediction[0]}
