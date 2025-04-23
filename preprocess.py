import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder

def preprocess_data(filepath):
    # Load the dataset
    df = pd.read_csv(filepath)

    # Drop rows with missing values
    df.dropna(inplace=True)

    print(df.columns)

    # Map or encode 'education_level' manually
    education_level_mapping = {
        "Grade 10": 10,
        "Grade 11": 11,
        "Grade 12": 12,
        "UG": 13,
        "PG": 14
    }
    if 'education_level' in df.columns:
        df['education_level'] = df['education_level'].map(education_level_mapping)
        # Check for unmapped or missing values in education_level
        if df['education_level'].isnull().any():
            print("Warning: Some 'education_level' values could not be mapped. Dropping these rows.")
            df.dropna(subset=['education_level'], inplace=True)
            
    # Separate numerical and categorical columns
    numerical_columns = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    categorical_columns = df.select_dtypes(include=['object']).columns.tolist()

    # Remove target column from categorical columns if present
    if 'career_aspiration' in categorical_columns:
        categorical_columns.remove('career_aspiration')

    # Encode categorical variables
    label_encoders = {}
    for col in categorical_columns:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        label_encoders[col] = le

    # Define features and target
    X = df.drop(columns=['career_aspiration'], errors='ignore')  # Drop target column
    y = df['career_aspiration']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Scale numerical features
    scaler = StandardScaler()
    X_train[numerical_columns] = scaler.fit_transform(X_train[numerical_columns])
    X_test[numerical_columns] = scaler.transform(X_test[numerical_columns])

    return X_train, X_test, y_train, y_test, scaler, label_encoders, X.columns