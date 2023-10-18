from kedro.pipeline import node, Pipeline
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
    

def load_data():
    data = load_digits()
    X = data['data']
    y = data['target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)
    return X_train, X_test, y_train, y_test

def create_and_train_model(X_train, y_train):
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    value = model.score(X_test, y_test)
    print('The final score is: ', str(value))
    return value