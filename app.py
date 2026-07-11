from flask import Flask, render_template, request
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load the trained pipeline model
model = pickle.load(open('LinearRegressionModel.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Capture inputs from the HTML Form
    car_name = request.form.get('name')
    company = request.form.get('company')
    year = int(request.form.get('year'))
    kms_driven = int(request.form.get('kms_driven'))
    fuel_type = request.form.get('fuel_type')

    # Construct DataFrame structural input matching the training set format
    input_data = pd.DataFrame({
        'name': [car_name],
        'company': [company],
        'year': [year],
        'kms_driven': [kms_driven],
        'fuel_type': [fuel_type]
    })

    # Execute Model Evaluation step
    prediction = model.predict(input_data)
    output = int(prediction[0])

    return render_template('index.html', prediction_text=f'Estimated Price: ₹{output:,}')

if __name__ == "__main__":
    app.run(debug=True)