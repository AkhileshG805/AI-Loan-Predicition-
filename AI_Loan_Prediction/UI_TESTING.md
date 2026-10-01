# LoanAI — UI & System Integration Testing Report

This document records the end-to-end integration and user interface verification conducted on the **LoanAI — Credit Underwriting Decision Support System** Flask web application.

---

## 1. Test Environment Details
- **Application Server**: Flask 3.1.3 (Werkzeug WSGI)
- **Host / Port**: `http://127.0.0.1:5000`
- **Python Runtime**: Python 3.11.9
- **Machine Learning Engine**: Scikit-Learn 1.9.0
- **Serialized Model**: `model/best_model.pkl` (Logistic Regression Classifier)
- **Preprocessing Pipeline**: `model/preprocessor.pkl` (ColumnTransformer with SimpleImputer, StandardScaler, and OneHotEncoder)
- **Dataset Sample**: 614 Records (Kaggle/Analytics Vidhya Dream in Loan Lenders Benchmark)

---

## 2. Automated Test Execution Results

| Test # | Test Scope / Scenario | Request / Route | Expected Outcome | Actual Result | Status |
|:---:|:---|:---|:---|:---|:---:|
| **TC-01** | **Main Dashboard View** | `GET /` | HTTP 200, LoanAI branding, KPI cards, zero raw Jinja syntax | HTTP 200, 19.6KB rendered, zero raw `{{` or `{%` tags | **PASS** |
| **TC-02** | **Standalone Application Form** | `GET /predict` | HTTP 200, 3 fieldset sections, live calculation preview | HTTP 200, loan-form rendered with quick-fill sample buttons | **PASS** |
| **TC-03** | **Analytics & Visualizations Gallery** | `GET /analytics` | HTTP 200, all 8 visual frames loaded with academic captions | HTTP 200, static charts correctly referenced and loaded | **PASS** |
| **TC-04** | **About & Viva Preparation Guide** | `GET /about` | HTTP 200, 15-day curriculum mapping, 4 viva model answers | HTTP 200, curriculum table and questions rendered | **PASS** |
| **TC-05** | **JSON Metadata API** | `GET /api/model-info` | HTTP 200, JSON containing best model, accuracy, and F1 | HTTP 200, returned `Logistic Regression`, Accuracy: `86.18%`, F1: `90.81%` | **PASS** |
| **TC-06** | **Low-Risk Applicant (Approved)** | `POST /predict` (Credit: 1.0, Income: $9,000, Loan: $140K) | HTTP 200, Verdict `LIKELY APPROVED`, Confidence probability calculated | HTTP 200, Verdict: **`LIKELY APPROVED`** (Confidence: 81.33%) | **PASS** |
| **TC-07** | **High-Risk Applicant (Denied)** | `POST /predict` (Credit: 0.0, Income: $2,400, Loan: $220K) | HTTP 200, Verdict `LIKELY NOT APPROVED`, Confidence probability calculated | HTTP 200, Verdict: **`LIKELY NOT APPROVED`** (Confidence: 90.54%) | **PASS** |
| **TC-08** | **High Income Applicant Profile** | `POST /predict` (Credit: 1.0, Income: $12,000, Loan: $250K) | HTTP 200, Verdict `LIKELY APPROVED`, Ratio: 48.0x | HTTP 200, Verdict: **`LIKELY APPROVED`** (Confidence: 83.21%) | **PASS** |
| **TC-09** | **Form Validation (Missing Input)** | `POST /predict` (ApplicantIncome omitted) | HTTP 302 redirect to `/predict`, flash warning displayed | HTTP 302, Redirect Header: `/predict`, flash message active | **PASS** |
| **TC-10** | **Form Validation (Negative Input)** | `POST /predict` (ApplicantIncome = -500) | HTTP 302 redirect to `/predict`, flash warning displayed | HTTP 302, Redirect Header: `/predict`, flash message active | **PASS** |
| **TC-11** | **Error Handler (404 Page)** | `GET /non-existent-page-url` | HTTP 404, user-friendly `error.html` page without stack trace | HTTP 404, clean error page rendered with return button | **PASS** |
| **TC-12** | **Static Server / Live Server Warning** | Client JS evaluation on `file:///` or port 5500 | Display instructive warning banner advising to launch Flask | Static banner triggered when port != 5000 | **PASS** |
| **TC-13** | **Smart Unit Normalization** | `POST /predict` (`LoanAmount=140000`, `Loan_Amount_Term=30`) | Converts to $140K & 360 months, predicts without error | HTTP 200, Verdict `LIKELY APPROVED`, displays $140,000 & 360 mos | **PASS** |
| **TC-14** | **Dashboard Embedded Form Assessment** | `GET /` -> Submit quick loan assessment | Evaluates directly from home dashboard and returns report | HTTP 200, Report generated with real ML prediction | **PASS** |

---

## 3. UI Component & Feature Verification

### A. Live Server / Static File Detection
* **Issue Addressed**: When opened outside Flask (e.g. VS Code Live Server on port 5500 or double-clicking HTML), browsers cannot evaluate Jinja tags.
* **Solution Verified**: A client-side JavaScript detector inspects `window.location.protocol` and `window.location.port`. If running statically, it displays a top warning banner advising the user to execute `python app.py` and open `http://127.0.0.1:5000`.

### B. Live Financial Calculation Preview
* As the user types into **Applicant Income**, **Coapplicant Income**, or **Loan Amount**, the script dynamically calculates and updates:
  - **Total Monthly Income** (`ApplicantIncome + CoapplicantIncome`)
  - **Income-to-Loan Ratio** (`TotalIncome / (LoanAmount + 0.001)`)
  - Verified live in browser DOM without form submission lag.

### C. Quick-Fill Sample Profiles for Faculty Viva Demonstrations
* **Low-Risk Button (Approved)**: Instantly populates Male, Married, Graduate, Salaried, $6,500 Base + $2,500 Coapp income, $140K loan amount, 360-month term, Semiurban, Credit History 1.0.
* **High-Risk Button (Rejected)**: Instantly populates Male, Unmarried, Non-Graduate, Self-Employed, $2,400 Base + $0 Coapp income, $220K loan amount, 360-month term, Rural, Credit History 0.0.

### D. Official Decision Report & PDF Export
* The prediction result page displays an executive banner (`LIKELY APPROVED` or `LIKELY NOT APPROVED`), confidence metric, submitted applicant profile snapshot, risk indicators, and academic disclaimer.
* The **Print / Save PDF Report** button invokes `window.print()` using customized `@media print` CSS rules that strip navigation bars and format the result as an official decision support memo.
