import os
import joblib
import pandas as pd
import numpy as np
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

app = Flask(__name__)
app.secret_key = 'loanai_academic_internship_secret_key_2026'

# Global references for loaded machine learning artifacts
model = None
preprocessor = None
model_info = None

def load_model_assets():
    """Loads the pre-trained classification model, preprocessing pipeline, and training metadata."""
    global model, preprocessor, model_info
    try:
        model_path = os.path.join('model', 'best_model.pkl')
        preprocessor_path = os.path.join('model', 'preprocessor.pkl')
        model_info_path = os.path.join('model', 'model_info.pkl')
        
        if os.path.exists(model_path) and os.path.exists(preprocessor_path):
            model = joblib.load(model_path)
            preprocessor = joblib.load(preprocessor_path)
            
            if os.path.exists(model_info_path):
                model_info = joblib.load(model_info_path)
            else:
                model_info = {
                    'total_records': 614,
                    'num_features': 13,
                    'num_models_trained': 4,
                    'best_model_name': 'Logistic Regression',
                    'best_accuracy': 0.8618,
                    'best_f1_score': 0.9081,
                    'metrics_summary': {
                        'Logistic Regression': {'accuracy': 0.8618, 'precision': 0.8400, 'recall': 0.9882, 'f1': 0.9081},
                        'Support Vector Machine': {'accuracy': 0.8455, 'precision': 0.8235, 'recall': 0.9882, 'f1': 0.8984},
                        'Decision Tree': {'accuracy': 0.8455, 'precision': 0.8438, 'recall': 0.9529, 'f1': 0.8950},
                        'K-Nearest Neighbors': {'accuracy': 0.7967, 'precision': 0.7941, 'recall': 0.9529, 'f1': 0.8663}
                    }
                }
            print("[LoanAI] Successfully loaded model, preprocessor, and metadata.")
            return True
        else:
            print("[LoanAI] Error: Model asset pickle files are missing. Please run 'train_model.py'.")
            return False
    except Exception as e:
        print(f"[LoanAI] Exception occurred loading model assets: {str(e)}")
        return False

# Indian Rupee Number Formatter for Authentic Presentation
def format_inr(number):
    """Formats numeric values according to standard Indian numbering format (Lakhs & Crores)."""
    try:
        val = int(round(float(number)))
        neg = val < 0
        s = str(abs(val))
        if len(s) <= 3:
            res = s
        else:
            last3 = s[-3:]
            remaining = s[:-3]
            parts = []
            while len(remaining) > 2:
                parts.append(remaining[-2:])
                remaining = remaining[:-2]
            if remaining:
                parts.append(remaining)
            parts.reverse()
            res = ",".join(parts) + "," + last3
        return ("-" if neg else "") + res
    except Exception:
        return str(number)

app.jinja_env.filters['inr'] = format_inr

# Attempt to load model assets on app initialization
load_model_assets()

@app.route('/')
def home():
    """Main Dashboard View: Displays key dataset metrics, leaderboard, and overview."""
    if model is None or preprocessor is None:
        load_model_assets()
    return render_template('index.html', model_info=model_info, active_page='dashboard')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    """
    GET: Renders the loan application form.
    POST: Processes applicant data, applies feature engineering and preprocessing, 
          executes model inference, and renders the result report.
    """
    if model is None or preprocessor is None:
        assets_loaded = load_model_assets()
        if not assets_loaded:
            flash("Model assets are not initialized. Please ensure model files are present.", "danger")
            return redirect(url_for('home'))

    # If accessed via GET, render the standalone application form page
    if request.method == 'GET':
        return render_template('predict.html', model_info=model_info, active_page='predict')

    # POST: Process form submission
    try:
        # 1. Retrieve Form Inputs
        gender = request.form.get('Gender', '').strip()
        married = request.form.get('Married', '').strip()
        dependents = request.form.get('Dependents', '').strip()
        education = request.form.get('Education', '').strip()
        self_employed = request.form.get('Self_Employed', '').strip()
        
        applicant_income_raw = request.form.get('ApplicantIncome', '').strip()
        coapplicant_income_raw = request.form.get('CoapplicantIncome', '').strip()
        loan_amount_raw = request.form.get('LoanAmount', '').strip()
        loan_amount_term_raw = request.form.get('Loan_Amount_Term', '').strip()
        credit_history_raw = request.form.get('Credit_History', '').strip()
        property_area = request.form.get('Property_Area', '').strip()
        
        # 2. Basic Validation (Check missing values)
        required_fields = {
            'Gender': gender,
            'Married': married,
            'Dependents': dependents,
            'Education': education,
            'Self Employed': self_employed,
            'Applicant Income': applicant_income_raw,
            'Coapplicant Income': coapplicant_income_raw,
            'Loan Amount': loan_amount_raw,
            'Loan Term': loan_amount_term_raw,
            'Credit History': credit_history_raw,
            'Property Area': property_area
        }
        
        for field_name, value in required_fields.items():
            if value is None or value == '':
                flash(f"Validation Error: '{field_name}' is a required field.", "warning")
                return redirect(url_for('predict'))
                
        # 3. Numeric Conversion and Bounds Checking
        try:
            applicant_income = float(applicant_income_raw)
            coapplicant_income = float(coapplicant_income_raw)
            loan_amount = float(loan_amount_raw)
            loan_amount_term = float(loan_amount_term_raw)
            credit_history = float(credit_history_raw)
        except ValueError:
            flash("Validation Error: Income, Loan Amount, Loan Term, and Credit History must be valid numbers.", "warning")
            return redirect(url_for('predict'))
            
        if applicant_income < 0 or coapplicant_income < 0 or loan_amount < 0 or loan_amount_term < 0:
            flash("Validation Error: Financial values and term duration cannot be negative.", "warning")
            return redirect(url_for('predict'))

        if loan_amount == 0:
            flash("Validation Error: Requested Loan Amount must be greater than zero.", "warning")
            return redirect(url_for('predict'))

        # Smart unit normalization:
        # If user entered full dollar amount e.g. 150000 instead of 150 (in thousands),
        # convert to thousands to match the training dataset schema.
        if loan_amount >= 1000:
            loan_amount = loan_amount / 1000.0

        # If user entered loan term in years (e.g. 30 instead of 360), convert to months
        if 0 < loan_amount_term <= 50:
            loan_amount_term = loan_amount_term * 12.0
            
        # 4. Feature Engineering
        # Calculate engineered features using the exact same formulas as in training
        total_income = applicant_income + coapplicant_income
        income_to_loan_ratio = total_income / (loan_amount + 0.001)
        
        # 5. Create DataFrame for Preprocessor Pipeline
        # Feature columns and order must match the training set exactly
        input_data = pd.DataFrame([{
            'Gender': gender,
            'Married': married,
            'Dependents': dependents,
            'Education': education,
            'Self_Employed': self_employed,
            'ApplicantIncome': float(applicant_income),
            'CoapplicantIncome': float(coapplicant_income),
            'LoanAmount': float(loan_amount),
            'Loan_Amount_Term': float(loan_amount_term),
            'Credit_History': float(credit_history),
            'Property_Area': property_area,
            'TotalIncome': float(total_income),
            'Income_to_Loan_Ratio': float(income_to_loan_ratio)
        }])
        
        # Cast categorical columns to object type to match training pipeline input types
        categorical_features = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'Credit_History', 'Property_Area']
        for col in categorical_features:
            input_data[col] = input_data[col].astype(object)
            
        # 6. Apply Preprocessor Transformation and Predict
        transformed_input = preprocessor.transform(input_data)
        prediction_val = int(model.predict(transformed_input)[0])
        
        # 7. Calculate Real Prediction Probability (Confidence) if supported by the model
        probability = None
        if hasattr(model, 'predict_proba'):
            prob_scores = model.predict_proba(transformed_input)[0]
            probability = float(prob_scores[prediction_val])
            
        # Map output to label
        result_label = "LIKELY APPROVED" if prediction_val == 1 else "LIKELY NOT APPROVED"
        
        applicant_summary = {
            'gender': gender,
            'married': married,
            'dependents': dependents,
            'education': education,
            'self_employed': self_employed,
            'applicant_income': int(applicant_income),
            'coapplicant_income': int(coapplicant_income),
            'total_income': int(total_income),
            'loan_amount': int(loan_amount),
            'loan_term': int(loan_amount_term),
            'credit_history': "Meets Guidelines (1.0)" if credit_history == 1.0 else "Guidelines Not Met (0.0)",
            'property_area': property_area,
            'income_to_loan_ratio': round(income_to_loan_ratio, 2)
        }
        
        best_model_name = model_info.get('best_model_name', 'Logistic Regression') if model_info else 'Logistic Regression'
        
        return render_template(
            'result.html', 
            result=result_label, 
            summary=applicant_summary, 
            probability=probability,
            best_model_name=best_model_name,
            active_page='predict'
        )
                               
    except Exception as e:
        print(f"[LoanAI] Prediction error: {str(e)}")
        flash(f"An unexpected error occurred during prediction: {str(e)}", "danger")
        return redirect(url_for('predict'))

@app.route('/analytics')
def analytics():
    """Analytics View: Displays generated EDA charts, confusion matrices, and model comparison."""
    if model is None or preprocessor is None:
        load_model_assets()
    return render_template('analytics.html', model_info=model_info, active_page='analytics')

@app.route('/about')
def about():
    """Redirects to dashboard as About & Viva is removed from the visible interface."""
    return redirect(url_for('home'))

@app.route('/api/model-info')
def api_model_info():
    """REST API endpoint returning current model status and metrics as JSON."""
    if model_info:
        return jsonify({
            'status': 'ready',
            'best_model': model_info.get('best_model_name'),
            'accuracy': model_info.get('best_accuracy'),
            'f1_score': model_info.get('best_f1_score'),
            'total_records': model_info.get('total_records'),
            'models_trained': model_info.get('num_models_trained'),
            'metrics_summary': model_info.get('metrics_summary')
        })
    return jsonify({'status': 'uninitialized'}), 503

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', error_code=404, message="The requested page could not be found."), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('error.html', error_code=500, message="An internal server error occurred."), 500

if __name__ == '__main__':
    # Localhost development server on port 5000
    print("[LoanAI] Starting server on http://127.0.0.1:5000 ...")
    app.run(host='127.0.0.1', port=5000, debug=True)
