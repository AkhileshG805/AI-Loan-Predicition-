# System Testing & Verification Report

This document records the system tests conducted on the **AI-Based Loan Approval Prediction & Decision Support System** Flask web application.

---

## 1. Test Environment
- **Python Runtime**: Portable Python 3.11.9
- **Server Address**: `http://127.0.0.1:5000`
- **Trained Model**: Logistic Regression (Accuracy = 86.18%, F1-Score = 90.81%)
- **Data Preprocessing**: Pre-fitted Scikit-Learn `ColumnTransformer` pipeline

---

## 2. Test Execution Logs

### Test 1: Valid Applicant with Positive Credit History
- **Description**: Verify prediction for a standard low-risk applicant who meets credit guidelines.
- **Input Parameters**:
  - `Gender`: Male
  - `Married`: Yes
  - `Dependents`: 0
  - `Education`: Graduate
  - `Self_Employed`: No
  - `ApplicantIncome`: 5000
  - `CoapplicantIncome`: 2000
  - `LoanAmount`: 150 (for $150,000)
  - `Loan_Amount_Term`: 360 (30 Years)
  - `Credit_History`: 1.0 (Good)
  - `Property_Area`: Urban
- **Expected Outcome**: HTTP 200, output prediction displays `LIKELY APPROVED`.
- **Actual Outcome**: HTTP 200, result displays **`LIKELY APPROVED`** (Confidence probability: 81.33%).
- **Status**: **PASS**

---

### Test 2: Valid Applicant with Negative Credit History
- **Description**: Verify prediction for an applicant with similar financial parameters but who has previously defaulted or does not meet credit guidelines.
- **Input Parameters**:
  - `Gender`: Male
  - `Married`: Yes
  - `Dependents`: 0
  - `Education`: Graduate
  - `Self_Employed`: No
  - `ApplicantIncome`: 5000
  - `CoapplicantIncome`: 2000
  - `LoanAmount`: 150
  - `Loan_Amount_Term`: 360
  - `Credit_History`: 0.0 (Bad)
  - `Property_Area`: Urban
- **Expected Outcome**: HTTP 200, output prediction displays `LIKELY NOT APPROVED`.
- **Actual Outcome**: HTTP 200, result displays **`LIKELY NOT APPROVED`** (Confidence probability: 90.54%).
- **Status**: **PASS**

---

### Test 3: High Income and Loan Amount (Alternative Financial Profile)
- **Description**: Verify prediction for a self-employed individual with a substantial monthly income and a large requested capital amount.
- **Input Parameters**:
  - `Gender`: Female
  - `Married`: No
  - `Dependents`: 1
  - `Education`: Graduate
  - `Self_Employed`: Yes
  - `ApplicantIncome`: 9000
  - `CoapplicantIncome`: 0
  - `LoanAmount`: 300 (for $300,000)
  - `Loan_Amount_Term`: 360
  - `Credit_History`: 1.0 (Good)
  - `Property_Area`: Semiurban
- **Expected Outcome**: HTTP 200, output prediction displays `LIKELY APPROVED`.
- **Actual Outcome**: HTTP 200, result displays **`LIKELY APPROVED`** (Confidence probability: 80.91%).
- **Status**: **PASS**

---

### Test 4: Missing Required Inputs (Form Validation)
- **Description**: Verify that the application intercepts empty form submissions and redirects gracefully instead of throwing a python traceback.
- **Input Parameters**:
  - `Gender`: Male
  - `ApplicantIncome`: "" (Empty string)
  - *Other parameters standard*
- **Expected Outcome**: HTTP 302 redirecting to `/#application-form`, and a flashed alert message displaying "Validation Error: 'Applicant Income' is a required field."
- **Actual Outcome**: HTTP 302, redirect header location is **`/#application-form`**. Flash message displays correctly.
- **Status**: **PASS**

---

### Test 5: Invalid Numerical Input (Data Type Verification)
- **Description**: Verify that alphabetic strings submitted to numerical fields (like income or loan amount) are caught by type checks.
- **Input Parameters**:
  - `ApplicantIncome`: "abc" (String value)
  - *Other parameters standard*
- **Expected Outcome**: HTTP 302 redirecting to `/#application-form`, and a flashed alert message displaying "Validation Error: Income, Loan Amount, Loan Term, and Credit History must be valid numbers."
- **Actual Outcome**: HTTP 302, redirect header location is **`/#application-form`**. Flash message displays correctly.
- **Status**: **PASS**

---

### Test 6: Normal Prediction through User Interface (System Integration)
- **Description**: Submit a valid applicant record through the frontend HTML form inputs and review UI rendering.
- **Verification Steps**:
  1. Open `http://127.0.0.1:5000` in the browser.
  2. Complete the form inputs.
  3. Click "Predict Loan Approval".
- **Expected Outcome**: The page redirects to `/predict`, rendering the result card (`LIKELY APPROVED` or `LIKELY NOT APPROVED`), the input summary block, the educational disclaimer, and the return button.
- **Actual Outcome**: The page redirects, showing the result view with confidence probability and full summary list matching the input parameters.
- **Status**: **PASS**
