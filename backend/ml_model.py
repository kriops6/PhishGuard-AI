import pickle
import numpy as np

# Placeholder for the ML model (WIP)
class PhishingModel:
    def __init__(self, model_path=None):
        self.model = None
        if model_path:
            self.load_model(model_path)
            
    def load_model(self, path):
        with open(path, 'rb') as f:
            self.model = pickle.load(f)
            
    def extract_features(self, url):
        # extract features from url for the model
        length = len(url)
        dots = url.count('.')
        has_https = 1 if url.startswith('https') else 0
        return np.array([[length, dots, has_https]])
        
    def predict(self, url):
        if self.model is None:
            return 0 # Fallback if model not loaded
        features = self.extract_features(url)
        prediction = self.model.predict_proba(features)[0][1] # Probability of phishing
        return int(prediction * 100)
