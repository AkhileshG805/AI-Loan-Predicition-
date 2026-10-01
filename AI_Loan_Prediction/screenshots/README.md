# Internship Report Screenshot Guidelines
## Chapter 5: Implementation and Testing

This guide contains the exact screenshots you should capture from this working project to populate **CHAPTER 5 (IMPLEMENTATION AND TESTING)** of your internship report.

---

### 01_project_structure
* **What to Capture**: Capture the file explorer sidebar in VS Code, PyCharm, or Windows Explorer showing the `AI_Loan_Prediction` project directory layout (folders: `dataset/`, `model/`, `notebooks/`, `static/`, `templates/`, and scripts like `app.py`, `train_model.py`).
* **Why it is Important**: Proves that the project is structured according to modular software engineering conventions.
* **Chapter 5 Section**: Section 5.1 - Project Directory Structure.

### 02_dataset
* **What to Capture**: Open the `dataset/loan_data.csv` file in Excel or a text editor and screenshot the first 15 rows showing the header and CSV layout.
* **Why it is Important**: Proves the authenticity of the Kaggle/Analytics Vidhya dataset (614 rows).
* **Chapter 5 Section**: Section 5.2 - Raw Dataset Structure.

### 03_dataset_information
* **What to Capture**: Screenshot the console stdout output under the heading `DATASET INFORMATION` printed when running `train_model.py` (specifically showing the shape and first 5 rows).
* **Why it is Important**: Documents the raw shape and initial state of the loaded dataset.
* **Chapter 5 Section**: Section 5.3 - Initial Data Inspection.

### 04_missing_values
* **What to Capture**: Screenshot the section of the console output of `train_model.py` showing the missing values counts (e.g. `Gender 13`, `Married 3`, `LoanAmount 22`, `Credit_History 50`).
* **Why it is Important**: Shows that the dataset contains missing fields, justifying the need for imputation pipelines.
* **Chapter 5 Section**: Section 5.3.1 - Missing Data Analysis.

### 05_data_preprocessing
* **What to Capture**: Capture the terminal log showing:
  - `Numerical Features: ['ApplicantIncome', ...]`
  - `Categorical Features: ['Gender', ...]`
  - `Preprocessor pipeline saved as 'model/preprocessor.pkl'`
* **Why it is Important**: Proves the successful design and serialization of the pipeline.
* **Chapter 5 Section**: Section 5.4 - Pipeline Preprocessing and Scaling.

### 06_feature_engineering
* **What to Capture**: Capture the terminal output under `DATA PREPROCESSING & FEATURE ENGINEERING` detailing the formulas:
  - `TotalIncome = ApplicantIncome + CoapplicantIncome`
  - `Income_to_Loan_Ratio = TotalIncome / (LoanAmount + 0.001)`
* **Why it is Important**: Proves feature engineering was implemented mathematically.
* **Chapter 5 Section**: Section 5.5 - Feature Engineering.

### 07_eda_loan_distribution
* **What to Capture**: Open and screenshot the pie chart image saved at `static/visualizations/eda_loan_distribution.png` showing the 68.7% vs 31.3% split.
* **Why it is Important**: Visualizes the target class distribution.
* **Chapter 5 Section**: Section 5.6.1 - Class Distribution Analysis.

### 08_eda_credit_history
* **What to Capture**: Screenshot the chart `static/visualizations/eda_credit_history_vs_loan.png`.
* **Why it is Important**: Visually proves that Credit History is the most critical feature in predicting loan approval.
* **Chapter 5 Section**: Section 5.6.2 - Credit History Distribution.

### 09_eda_income
* **What to Capture**: Screenshot the histogram `static/visualizations/eda_applicant_income.png`.
* **Why it is Important**: Visualizes the distribution skewness of applicant income.
* **Chapter 5 Section**: Section 5.6.3 - Financial Attribute Distribution.

### 10_model_training
* **What to Capture**: Screenshot the terminal console log output during model training (showing `Training Logistic Regression...`, `Training K-Nearest Neighbors...`, etc.).
* **Why it is Important**: Proves the actual models were trained in real-time.
* **Chapter 5 Section**: Section 5.7 - Model Training Logs.

### 11_model_evaluation
* **What to Capture**: Screenshot the individual model metrics printout (Accuracy, Precision, Recall, F1, and confusion matrix arrays) printed in the console for each model.
* **Why it is Important**: Documents the raw performance values before compilation.
* **Chapter 5 Section**: Section 5.8 - Model Evaluation Reports.

### 12_confusion_matrix
* **What to Capture**: Open and screenshot `static/visualizations/confusion_matrices.png`.
* **Why it is Important**: Shows the visual grids of True Positives, False Positives, True Negatives, and False Negatives for all classifiers.
* **Chapter 5 Section**: Section 5.8.1 - Confusion Matrix Analysis.

### 13_model_comparison
* **What to Capture**: Open and screenshot the compiled metrics chart at `static/visualizations/model_comparison.png`.
* **Why it is Important**: Shows a clean bar-by-bar comparative layout.
* **Chapter 5 Section**: Section 5.9 - Comparative Performance Bar Chart.

### 14_best_model
* **What to Capture**: Screenshot the terminal log output under `BEST MODEL SELECTION`:
  - `Selected Best Model: Logistic Regression`
  - `Criteria: Highest Validation F1-Score (0.9081)`
  - `Best model successfully saved as 'model/best_model.pkl'`
* **Why it is Important**: Explains the rationale for model selection.
* **Chapter 5 Section**: Section 5.10 - Best Model Export.

### 15_flask_home
* **What to Capture**: Open a browser to `http://127.0.0.1:5000` and screenshot the top portion of the homepage showing the title, project description statistics cards, and the model comparison table.
* **Why it is Important**: Demonstrates the frontend web interface and live dashboard metrics.
* **Chapter 5 Section**: Section 5.11 - Flask Application Dashboard.

### 16_loan_input_form
* **What to Capture**: Scroll down on the homepage and capture a screenshot of the filled-out "New Loan Application" sidebar form (with valid entries like income, loan amount, and credit history selected).
* **Why it is Important**: Shows input fields, selection dropdowns, and button.
* **Chapter 5 Section**: Section 5.12 - Interactive Form Interface.

### 17_prediction_result
* **What to Capture**: Screenshot the result screen loaded at `/predict` showing the green banner "LIKELY APPROVED" (e.g. from Test 1) or red banner "LIKELY NOT APPROVED" (from Test 2), alongside the applicant summary card.
* **Why it is Important**: Proves successful real-time model inference and decision presentation.
* **Chapter 5 Section**: Section 5.13 - Inference Verdict View.

### 18_error_validation
* **What to Capture**: Enter a negative income or leave fields blank, submit, and screenshot the warning alert pop-up (client-side script validation) or redirect flash message.
* **Why it is Important**: Proves the presence of input validation and exception safety checks.
* **Chapter 5 Section**: Section 5.14 - Form Validation & Error Handling.

### 19_final_application
* **What to Capture**: Capture a full-page screen print of the entire dashboard screen showing the correlation heatmap, charts, and leaderboard.
* **Why it is Important**: Demonstrates the final web application.
* **Chapter 5 Section**: Section 5.15 - End-to-End System Demonstration.
