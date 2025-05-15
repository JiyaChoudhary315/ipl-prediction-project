import joblib
import os

model_path = os.path.join(os.path.dirname(__file__), 'model.pkl')
model = joblib.load(model_path)

def predict_winner(data):
    prediction = model.predict([data])
    return prediction[0]
