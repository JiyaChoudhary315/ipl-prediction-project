from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# Load the saved model
model = joblib.load('ipl_match_winner_model.joblib')

# Create a FastAPI instance
app = FastAPI()

# Define a request body model
class MatchInput(BaseModel):
    team1: str
    team2: str

# Create an endpoint for prediction
@app.post("/predict")
def predict_match_winner(match: MatchInput):
    # Prepare the input data (encode team names)
    teams = pd.DataFrame([[match.team1, match.team2]], columns=['team1', 'team2'])
    teams['team1_encoded'] = teams['team1'].astype('category').cat.codes
    teams['team2_encoded'] = teams['team2'].astype('category').cat.codes
    X = teams[['team1_encoded', 'team2_encoded']]
    
    # Predict the winner
    prediction = model.predict(X)
    return {"predicted_winner": prediction[0]}
