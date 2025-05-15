from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

actual_scores = [175, 165, 180, 170]  # Replace with actual score data
predicted_scores = [178, 160, 182, 165]  # Replace with predicted scores

mae = mean_absolute_error(actual_scores, predicted_scores)
rmse = np.sqrt(mean_squared_error(actual_scores, predicted_scores))

print(f"Mean Absolute Error: {mae:.2f}")
print(f"Root Mean Squared Error: {rmse:.2f}")
