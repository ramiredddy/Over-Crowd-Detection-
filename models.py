import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd

class CrowdRiskModel:
    def __init__(self):
        self.model = None
        self.is_trained = False

    def train_model(self, data):
        # Sample training data: features like density, time, location
        # Target: risk level (0: low, 1: medium, 2: high)
        if data is None:
            # Generate synthetic data for training
            np.random.seed(42)
            n_samples = 1000
            density = np.random.uniform(0, 100, n_samples)
            time_of_day = np.random.uniform(0, 24, n_samples)
            location_factor = np.random.uniform(0, 1, n_samples)
            risk = (density > 70).astype(int) + (density > 90).astype(int)  # 0,1,2

            X = np.column_stack([density, time_of_day, location_factor])
            y = risk

            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            self.model = RandomForestClassifier(n_estimators=100, random_state=42)
            self.model.fit(X_train, y_train)

            predictions = self.model.predict(X_test)
            accuracy = accuracy_score(y_test, predictions)
            print(f"Model trained with accuracy: {accuracy:.2f}")
            self.is_trained = True
        else:
            # If real data provided, train on it
            pass

    def predict_risk(self, density, time_of_day, location_factor):
        if not self.is_trained:
            self.train_model(None)
        features = np.array([[density, time_of_day, location_factor]])
        risk_level = self.model.predict(features)[0]
        risk_labels = {0: 'Low', 1: 'Medium', 2: 'High'}
        return risk_labels[risk_level]

# Instantiate the model
crowd_model = CrowdRiskModel()
