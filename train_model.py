from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

def train_model(X_train, X_test, y_train, y_test, model_path="model.pkl"):
    # Initialize the model
    model = RandomForestClassifier(random_state=42)

    # Train the model
    model.fit(X_train, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {accuracy:.2f}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))

    # Save the trained model
    joblib.dump(model, model_path)
    print(f"Model saved to {model_path}")

if __name__ == "__main__":
    # Load preprocessed data
    from preprocess import preprocess_data
    filepath = r"C:\Users\Akshitha Kotte\Desktop\mini_project\Intelligent-Career-Navigator\data\icn_dataset_20k.csv"
    X_train, X_test, y_train, y_test, _, _, _ = preprocess_data(filepath) 

    # print(X_train)

    # Train the model
    train_model(X_train, X_test, y_train, y_test)