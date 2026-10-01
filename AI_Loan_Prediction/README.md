# LoanAI — AI-Based Loan Approval Prediction & Decision Support System

An academic internship project that predicts loan application sanctioning using supervised Machine Learning classification algorithms. The project features an interactive Flask application (**LoanAI**), an executive analytics dashboard, dynamic feature engineering, real-time prediction reports, and viva voce preparation guides.

---

## 1. Project Overview
LoanAI serves as an intelligent credit risk decision-support utility. By analyzing applicant demographics (gender, marital status, dependents, education, employment), credit guidelines compliance, and loan-to-income metrics, it assists underwriting teams in assessing credit sanctioning likelihood with verifiable accuracy.

### Key Highlights:
- **Brand Identity**: Professional **LoanAI** interface in a clean Navy, Slate, and Emerald palette.
- **Trained Classifiers**: Logistic Regression, Support Vector Machine (SVM), Decision Tree, and K-Nearest Neighbors (KNN).
- **Anti-Leakage Pipeline**: Scikit-Learn `ColumnTransformer` (Median/Mode imputation, StandardScaler, OneHotEncoder).
- **Mathematical Feature Engineering**: `TotalIncome` and `Income_to_Loan_Ratio`.
- **Dynamic Prediction Report**: Instant decision verdict, calculated model confidence, submitted parameter breakdown, and print-ready PDF styling.
- **Academic Integrity**: Prominent disclaimers emphasizing that the system is an educational simulation, not an actual bank credit granting engine.

---

## 2. Directory Architecture

```text
AI_Loan_Prediction/
│
├── dataset/
│   └── loan_data.csv                   # Authentic benchmark dataset (614 rows, 13 columns)
│
├── model/
│   ├── best_model.pkl                  # Serialized production classifier (Logistic Regression)
│   ├── preprocessor.pkl                # Fitted ColumnTransformer pipeline
│   └── model_info.pkl                  # Training metadata, confusion matrices, and metrics
│
├── notebooks/
│   └── loan_prediction_analysis.ipynb  # Interactive Jupyter notebook for report review
│
├── screenshots/
│   └── README.md                       # Comprehensive Chapter 5 report screenshot capture guide
│
├── static/
│   ├── css/
│   │   └── style.css                   # Modern financial design system and print report stylesheet
│   ├── js/
│   │   └── script.js                   # Client-side validation, live calculation preview, and print action
│   └── visualizations/                 # 8 Programmatically exported charts (Heatmap, ROC/CM, EDA)
│
├── templates/
│   ├── base.html                       # Universal master layout with navbar, alerts, and footer
│   ├── index.html                      # Executive analytics dashboard & model leaderboard
│   ├── predict.html                    # Standalone loan prediction form with quick-fill demo buttons
│   ├── result.html                     # Official decision report with confidence score and PDF print action
│   ├── analytics.html                  # Visualizations & Exploratory Data Analysis gallery
│   ├── about.html                      # 15-Day curriculum mapping and faculty viva Q&A guide
│   └── error.html                      # Clean HTTP 404 / 500 error view
│
├── app.py                              # Flask application controller & inference engine
├── train_model.py                      # Multi-model training, pipeline fitting, and evaluation script
├── run_app.bat                         # One-click Windows batch launcher
├── run_app.ps1                         # One-click PowerShell launcher
├── requirements.txt                    # Project dependencies
├── UI_TESTING.md                       # Complete integration and UI test logs (All 14 test cases PASS)
├── PROJECT_DOCUMENTATION.md            # Comprehensive academic technical writeup
└── README.md                           # Quick start guide
```

---

## 3. Actual Model Benchmark Results

Models were trained and evaluated on an identical stratified split (80% train, 20% test) with `random_state=42`:

| Classifier Algorithm | Validation Accuracy | Precision | Recall | F1-Score | Status |
|:---|:---:|:---:|:---:|:---:|:---:|
| **Logistic Regression** | **86.18%** | **84.00%** | **98.82%** | **90.81%** | **Selected Best Model** |
| Support Vector Machine (SVM) | 84.55% | 82.35% | 98.82% | 89.84% | Evaluated |
| Decision Tree Classifier | 84.55% | 84.38% | 95.29% | 89.50% | Evaluated |
| K-Nearest Neighbors (KNN) | 79.67% | 79.41% | 95.29% | 86.63% | Evaluated |

**Selection Rationale**: **Logistic Regression** achieved the highest F1-Score of **90.81%** and a recall of **98.82%**. For credit risk modeling with class imbalance (~68.7% approved), F1-Score prevents majority-class bias and ensures maximum retention of creditworthy applicants.

---

## 4. How to Run the Application

### Option A: One-Click Launchers (Windows)
- Double-click **`run_app.bat`** (or execute `.\run_app.ps1` in PowerShell).
- The script automatically detects the local environment, starts Flask, and opens `http://127.0.0.1:5000` in your default browser.

### Option B: Manual Command Line Execution
1. Install dependencies (if not already installed):
   ```bash
   pip install -r requirements.txt
   ```
2. (Optional) Re-train models and regenerate charts:
   ```bash
   python train_model.py
   ```
3. Start the Flask server:
   ```bash
   python app.py
   ```
4. Open your browser and navigate to:
   **`http://127.0.0.1:5000`**

> **Note on Jinja Rendering:** Never open HTML templates directly via static servers (such as VS Code Live Server on port 5500). Flask's `render_template()` is required to process dynamic Jinja tags and perform inference.

---

## 5. Application Pages & Features

* **Dashboard (`/`)**: Displays dataset KPIs, model evaluation comparison table, underwriting feature dynamics, and visual charts.
* **Predict Loan (`/predict`)**: 3-section structured application form featuring live client-side calculation of `TotalIncome` and `Income_to_Loan_Ratio`, plus quick-fill demo buttons for viva presentations.
* **Decision Report (`/predict` - POST)**: Real-time verdict (`LIKELY APPROVED` or `LIKELY NOT APPROVED`), confidence score, applicant profile snapshot, risk factors, and **Print / Save PDF Report** action.
* **Analytics & EDA (`/analytics`)**: High-resolution embedded visualization gallery covering confusion matrices, correlation heatmap, income distribution, and property area impact.
* **About & Viva Guide (`/about`)**: Complete 15-day internship curriculum mapping, anti-leakage architecture diagrams, and top viva voce questions with model answers.

---

## 6. Academic Disclaimer
This project is developed exclusively for educational demonstration as part of a 15-day AI & Data Science internship curriculum. It does not represent an actual banking or financial institution's credit underwriting platform.
