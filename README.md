# Car Price Prediction Web Application

This repository contains an end-to-end Machine Learning project designed to predict the resale value of used cars. The project covers the full data science lifecycle, from data cleaning and feature engineering to model deployment using a Flask web interface.

## 🚀 Project Overview
The core objective of this project is to build a predictive model that estimates the price of a used car based on its key features (Company, Name, Year, Kilometers Driven, and Fuel Type).

*   **Model:** Linear Regression
*   **Deployment Framework:** Flask (Python)
*   **Input Handling:** Interactive Web Interface

## 🗂️ Project Structure
```text
car-price-prediction/
├── data/                  # Raw and processed datasets
├── static/                # CSS, JS, and image assets
├── templates/             # HTML files (index.html)
├── app.py                 # Flask server and prediction API
├── carprice.ipynb         # Data analysis and model training notebook
├── LinearRegressionModel.pkl  # Trained model artifact
├── Cleaned_Car_data.csv   # Processed dataset
└── requirements.txt       # Project dependencies
```

## 🛠️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone <your-repository-url>
   cd car-price-prediction
   ```

2. **Create and activate a virtual environment:**
   * **Windows:**
     ```bash
     python -m venv .venv
     .venv\Scripts\activate
     ```
   * **Mac/Linux:**
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 💻 Running the Application

1. **Launch the Flask server:**
   ```bash
   python app.py
   ```
2. **Access the Web Interface:**
   Open your browser and navigate to `http://127.0.0.1:5000`.

## 🧠 Workflow Pipeline

### 1. Data Processing (`carprice.ipynb`)
The raw dataset undergoes rigorous cleaning:
* **String Parsing:** Extracting relevant metadata from unstructured text.
* **Outlier Removal:** Cleaning anomalies in kilometers driven and year.
* **Encoding:** Transforming categorical variables (Company, Fuel Type) for regression input.

### 2. Model Training
* A **Linear Regression** pipeline was trained on cleaned features.
* The model pipeline is serialized into `LinearRegressionModel.pkl` using the `pickle` library, allowing for efficient loading during deployment without re-training.

### 3. Deployment
* **Flask Application (`app.py`):** Acts as the bridge between the web user and the machine learning model.
* **Pipeline:** Captures input from the HTML form, converts it to a pandas DataFrame, invokes `model.predict()`, and renders the estimated price to the dashboard.

## 📈 Future Enhancements
* **Advanced Regressors:** Experimenting with Random Forest or XGBoost to improve prediction accuracy.
* **Enhanced UI:** Integrating Bootstrap/Tailwind for a more responsive and professional dashboard.
* **Data Refresh:** Automating the data scraping pipeline to update price trends in real-time.
