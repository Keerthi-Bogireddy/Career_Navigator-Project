## Career Navigator
Career Navigator is a web application that predicts a user's ideal career path based on their academic performance, personality traits, hobbies, interests, and financial considerations. Powered by a Random Forest Classifier trained on a dataset of 30,000 entries (icn_dataset_30k.csv), the app provides personalized career recommendations and curated resources to help users pursue their predicted career. The application is built with Flask, Bootstrap, and scikit-learn, offering a user-friendly interface and responsive design.
Features

Career Prediction: Users complete a multi-section form to input details like age, education level, CGPA, personality traits, and hobbies. The app predicts a career (e.g., Software Engineer, Doctor, Teacher, Data Scientist) using a pre-trained Random Forest model.
Resources and Links: The results page displays tailored resources (e.g., online courses, professional organizations) for the predicted career, with a fallback to the careers page for unmapped careers.
Responsive Design: Built with Bootstrap 5.3.3 and custom CSS, ensuring a seamless experience on desktop and mobile devices.
Interactive Form: A progressive form with validation and tooltips guides users through input collection.
Careers Page: A dedicated page for exploring additional career options, linked in the navigation and used as a fallback for unmapped predictions.

## Tech Stack

Backend: Flask (Python web framework)
Frontend: HTML, Bootstrap 5.3.3, Font Awesome 6.5.1, custom CSS
Machine Learning: scikit-learn (Random Forest Classifier, StandardScaler, LabelEncoder)
Data Processing: pandas, joblib
Fonts: Google Fonts (Poppins)
Security: Cloudflare scripts (included in templates)

## Prerequisites

Python 3.8 or higher
pip (Python package manager)
Git (for cloning the repository)
A web browser (e.g., Chrome, Firefox)

## Setup Instructions

Clone the Repository:
git clone https://github.com/your-username/career-navigator.git
cd career-navigator


Create a Virtual Environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install Dependencies:Create a requirements.txt file with the following content:
flask==2.3.3
scikit-learn==1.3.2
pandas==2.0.3
joblib==1.3.2

Then run:
pip install -r requirements.txt


## Prepare the Dataset and Model:

Place icn_dataset_30k.csv in the data/ directory.
Train the model by running:python train_model.py

This generates model.pkl in the project root, containing the trained Random Forest model, scaler, label encoders, and feature columns.


Run the Application:
python app.py

The app will start in debug mode at http://127.0.0.1:5000.


## File Structure
career-navigator/
├── data/
│   └── icn_dataset_30k.csv     # Dataset for training the model
├── static/
│   └── styles.css              # Custom CSS with color variables
├── templates/
│   ├── index.html              # Home page
│   ├── about.html              # About page with styled table
│   ├── careers.html            # Careers exploration page
│   ├── predictor.html          # Form for user input
│   ├── results.html            # Results page with prediction and resources
│   ├── navbar.html             # Navigation bar (included in all pages)
│   └── footer.html             # Footer (included in all pages)
├── app.py                      # Flask application with routes
├── preprocess.py               # Data preprocessing functions
├── train_model.py              # Model training script
├── model.pkl                   # Trained model and preprocessing objects
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation

## Usage

Access the App:Open http://127.0.0.1:5000 in your browser after running app.py.

Navigate to Predictor:Click "Predictor" in the navigation bar to access the career prediction form (/predictor).

## Complete the Form:

The form is divided into sections: Personal Information, Academic Performance, Personality Traits, Study Habits, Extracurricular Activities, Hobbies, Interests, and Financial Information.
Provide inputs like age (15-100), CGPA (0.0-10.0), personality scores (1-10), and select hobbies/interests.
Validation ensures correct input ranges; tooltips provide guidance.
Click "Predict My Career" to submit.


## View Results:

The results page (/results) displays the predicted career (e.g., "Software Engineer") and an optional confidence score.
A "Resources and Links" section provides curated links for mapped careers (e.g., Coursera for Software Engineer, AMA for Doctor).
For unmapped careers, a link to the careers page (/careers) encourages further exploration.
Use "Try Again" to return to the form or "Back to Home" for the main page.


## Explore Careers:

Visit the careers page (/careers) via the navigation bar or fallback link to explore additional career options.



## Dataset

File: icn_dataset_30k.csv
Description: Contains 30,000 entries with features like age, education_level, cgpa, math_score, hobbies, interests, and career_aspiration (target column).
Preprocessing (preprocess.py):
Maps education_level (e.g., "Grade 10" to 10).
Encodes categorical columns (hobbies, interests) with LabelEncoder.
Scales numerical features with StandardScaler.
Splits data into 80% training and 20% testing sets.



## Model

Algorithm: Random Forest Classifier (scikit-learn)
Training (train_model.py):
Trained on preprocessed icn_dataset_30k.csv.
Saves model, scaler, label encoders, and feature columns to model.pkl.


Prediction (app.py):
Uses model.pkl to predict a career based on user inputs.
Outputs a single career label (e.g., "Software Engineer").


## Contributing

Fork the repository.
Create a feature branch (git checkout -b feature/your-feature).
Commit changes (git commit -m "Add your feature").
Push to the branch (git push origin feature/your-feature).
Open a pull request with a description of your changes.

Please ensure code follows PEP 8 standards and include tests for new features.
## License
MIT License
Copyright (c) 2025 
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
Contact
For issues or suggestions, please open an issue on the GitHub repository or contact .

### Happy career navigating!
