import joblib
from sklearn.metrics import accuracy_score, confusion_matrix
import pandas as pd

# Load your trained model (replace with your actual model path)
model = joblib.load('path_to_your_model_file.pkl')

# Load your test data (replace with your actual test file path)
test_data = pd.read_csv('path_to_test_data.csv')

# Split your data into features and target (replace 'target_column' with the actual name)
X_test = test_data.drop('target_column', axis=1)
y_test = test_data['target_column']

# Predict the results from the model
predictions = model.predict(X_test)

# Evaluate the accuracy
accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy}")

# Confusion Matrix to see where the model is making errors
conf_matrix = confusion_matrix(y_test, predictions)
print(f"Confusion Matrix:\n{conf_matrix}")
