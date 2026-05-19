import pickle
import pandas as pd
from sklearn.linear_model import LogisticRegression

def train_model():
    print("Training Logistic Regression model...")
    # Features: [length, dots, https]. Fake data for now because scraping 10,000 URLs at 2AM sounded awful.
    # Will swap this for the real Kaggle dataset later.
    X_train = [
        [20, 1, 1],
        [85, 4, 0],
        [30, 2, 1],
        [150, 5, 0]
    ]
    y_train = [0, 1, 0, 1] # 0 = Safe, 1 = Phishing
    
    model = LogisticRegression()
    model.fit(X_train, y_train)
    
    with open('phishing_model.pkl', 'wb') as f:
        pickle.dump(model, f)
    
    print("Model saved to phishing_model.pkl")

if __name__ == "__main__":
    train_model()
