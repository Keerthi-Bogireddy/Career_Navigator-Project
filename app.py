from flask import Flask, render_template, request
import pandas as pd
import joblib
from flask import Flask, render_template
app = Flask(__name__)

# Load the trained model and preprocessing objects
def load_model_and_preprocessors():
    data = joblib.load('model.pkl')  # Path to your model.pkl file
    return data['model'], data['scaler'], data['label_encoders'], data['feature_columns']

# Home route
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/careers')
def careers():
    return render_template('careers.html')

# Predictor route - Form for user input
@app.route('/predictor', methods=['GET', 'POST'])
def predictor():
    if request.method == 'POST':
        # Collecting form data
        user_data = request.form
        age = int(user_data['age'])
        education_level = user_data['education_level']
        cgpa = float(user_data['cgpa'])
        math_score = int(user_data['math_score'])
        physics_score = int(user_data['physics_score'])
        biology_score = int(user_data['biology_score'])
        history_score = int(user_data['history_score'])
        openness = int(user_data['openness'])
        conscientiousness = int(user_data['conscientiousness'])
        extraversion = int(user_data['extraversion'])
        agreeableness = int(user_data['agreeableness'])
        neuroticism = int(user_data['neuroticism'])
        weekly_self_study_hours = int(user_data['weekly_self_study_hours'])
        extracurricular_activities = int(user_data['extracurricular_activities'])
        hobbies = user_data.getlist('hobbies[]')
        interests = user_data['interests']
        budget = float(user_data['budget'])
        career_demand_score = int(user_data['career_demand_score'])

        # Education level mapping
        education_level_mapping = {
            "Grade 10": 10,
            "Grade 11": 11,
            "Grade 12": 12,
            "UG": 13,
            "PG": 14
        }

        # Creating a DataFrame with the input data
        input_data = pd.DataFrame([{
            'age': age,
            'education_level': education_level_mapping.get(education_level, 13),  # Map education_level
            'cgpa': cgpa,
            'math_score': math_score,
            'physics_score': physics_score,
            'biology_score': biology_score,
            'history_score': history_score,
            'openness': openness,
            'conscientiousness': conscientiousness,
            'extraversion': extraversion,
            'agreeableness': agreeableness,
            'neuroticism': neuroticism,
            'weekly_self_study_hours': weekly_self_study_hours,
            'extracurricular_activities': extracurricular_activities,
            'hobbies': ', '.join(hobbies),  # Convert list of hobbies into a string
            'interests': interests,
            'budget': budget,
            'career_demand_score': career_demand_score
        }])

        # Load model and preprocessors
        model, scaler, label_encoders, feature_columns = load_model_and_preprocessors()

        # Encode categorical variables
        categorical_columns = [col for col in input_data.columns if input_data[col].dtype == 'object']
        for col in categorical_columns:
            if col in label_encoders:
                try:
                    input_data[col] = label_encoders[col].transform(input_data[col])
                except ValueError:
                    # Handle unseen categories (e.g., new hobbies/interests)
                    input_data[col] = 0  # Or assign a default encoded value

        # Scale numerical features
        numerical_columns = [col for col in input_data.columns if col not in categorical_columns]
        input_data[numerical_columns] = scaler.transform(input_data[numerical_columns])

        # Ensure input_data has the same columns as training data
        input_data = input_data[feature_columns]

        # Make prediction
        prediction = model.predict(input_data)

        # Return result page with prediction
        return render_template('results.html', career=prediction[0])

    return render_template('predictor.html')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)