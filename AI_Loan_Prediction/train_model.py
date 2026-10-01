import os
import json
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

def check_directories():
    os.makedirs('dataset', exist_ok=True)
    os.makedirs('model', exist_ok=True)
    os.makedirs('static/visualizations', exist_ok=True)

def inspect_dataset(df):
    print("=" * 60)
    print("DATASET INFORMATION")
    print("=" * 60)
    print(f"Dataset Shape: {df.shape}")
    print("\nFirst 5 Rows:")
    print(df.head())
    print("\nLast 5 Rows:")
    print(df.tail())
    print("\nColumn Names and Data Types:")
    print(df.dtypes)
    print("\nMissing Values Count:")
    print(df.isnull().sum())
    print("\nStatistical Summary:")
    print(df.describe(include='all'))
    print("\nTarget Distribution (Loan_Status):")
    print(df['Loan_Status'].value_counts())
    print(df['Loan_Status'].value_counts(normalize=True))
    print("-" * 60)

def generate_visualizations(df):
    print("\nGENERATING VISUALIZATIONS...")
    
    # Set style
    sns.set_theme(style="whitegrid")
    plt.rcParams['figure.figsize'] = (10, 6)
    plt.rcParams['font.size'] = 12
    
    # 1. Loan Approval Distribution
    plt.figure()
    status_counts = df['Loan_Status'].value_counts()
    plt.pie(status_counts, labels=['Approved (Y)', 'Rejected (N)'], autopct='%1.1f%%', 
            colors=['#059669', '#dc2626'], startangle=90, explode=(0.05, 0))
    plt.title('Distribution of Loan Status (Approval Rate)')
    plt.tight_layout()
    plt.savefig('static/visualizations/eda_loan_distribution.png', dpi=300)
    plt.close()
    
    # 2. Applicant Income Distribution
    plt.figure()
    sns.histplot(df['ApplicantIncome'], kde=True, color='#1e3a8a', bins=40)
    plt.title('Distribution of Applicant Income')
    plt.xlabel('Applicant Income')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.savefig('static/visualizations/eda_applicant_income.png', dpi=300)
    plt.close()
    
    # 3. Loan Amount Distribution
    plt.figure()
    sns.histplot(df['LoanAmount'].dropna(), kde=True, color='#0ea5e9', bins=30)
    plt.title('Distribution of Loan Amount')
    plt.xlabel('Loan Amount (in Thousands)')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.savefig('static/visualizations/eda_loan_amount.png', dpi=300)
    plt.close()
    
    # 4. Education vs Loan Approval
    plt.figure()
    sns.countplot(x='Education', hue='Loan_Status', data=df, palette=['#059669', '#dc2626'])
    plt.title('Loan Approval Status by Education Level')
    plt.xlabel('Education')
    plt.ylabel('Count')
    plt.legend(title='Loan Status', labels=['Approved (Y)', 'Rejected (N)'])
    plt.tight_layout()
    plt.savefig('static/visualizations/eda_education_vs_loan.png', dpi=300)
    plt.close()
    
    # 5. Credit History vs Loan Approval
    plt.figure()
    sns.countplot(x='Credit_History', hue='Loan_Status', data=df.dropna(subset=['Credit_History']), palette=['#059669', '#dc2626'])
    plt.title('Loan Approval Status by Credit History')
    plt.xlabel('Credit History (1.0 = Good, 0.0 = Bad)')
    plt.ylabel('Count')
    plt.legend(title='Loan Status', labels=['Approved (Y)', 'Rejected (N)'])
    plt.tight_layout()
    plt.savefig('static/visualizations/eda_credit_history_vs_loan.png', dpi=300)
    plt.close()
    
    # 6. Property Area vs Loan Approval
    plt.figure()
    sns.countplot(x='Property_Area', hue='Loan_Status', data=df, palette=['#059669', '#dc2626'])
    plt.title('Loan Approval Status by Property Area')
    plt.xlabel('Property Area')
    plt.ylabel('Count')
    plt.legend(title='Loan Status', labels=['Approved (Y)', 'Rejected (N)'])
    plt.tight_layout()
    plt.savefig('static/visualizations/eda_property_area_vs_loan.png', dpi=300)
    plt.close()
    
    # 7. Correlation Heatmap
    plt.figure(figsize=(8, 6))
    numerical_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    # Add target temporarily to see correlation if numeric
    temp_df = df[numerical_cols].copy()
    temp_df['Loan_Status_Numeric'] = df['Loan_Status'].map({'Y': 1, 'N': 0})
    sns.heatmap(temp_df.corr(), annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    plt.title('Correlation Matrix of Numerical Features')
    plt.tight_layout()
    plt.savefig('static/visualizations/eda_correlation_heatmap.png', dpi=300)
    plt.close()
    
    print("EDA Visualizations generated successfully.")

def train_and_evaluate(df):
    print("=" * 60)
    print("DATA PREPROCESSING & FEATURE ENGINEERING")
    print("=" * 60)
    
    # Create copy of dataframe
    data = df.copy()
    
    # Feature Engineering (Explicitly documented in project documentation)
    # TotalIncome combines applicant and coapplicant incomes as they collectively cover the loan
    data['TotalIncome'] = data['ApplicantIncome'] + data['CoapplicantIncome']
    
    # Income to Loan Ratio evaluates the client's repayment capacity per unit of borrowed capital
    # We add 0.001 to prevent division by zero in case of missing or zero LoanAmount values
    data['Income_to_Loan_Ratio'] = data['TotalIncome'] / (data['LoanAmount'] + 0.001)
    
    print("Engineered Features added:")
    print("- TotalIncome = ApplicantIncome + CoapplicantIncome")
    print("- Income_to_Loan_Ratio = TotalIncome / (LoanAmount + 0.001)")
    
    # Define Target and Features
    X = data.drop(columns=['Loan_ID', 'Loan_Status'])
    y = data['Loan_Status'].map({'Y': 1, 'N': 0}) # Map to 1 (Y) and 0 (N)
    
    # Define columns to preprocess
    numeric_features = ['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 'TotalIncome', 'Income_to_Loan_Ratio']
    categorical_features = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'Credit_History', 'Property_Area']
    
    # Force categorical features to object type for pipeline consistency
    for col in categorical_features:
        X[col] = X[col].astype(object)
        
    print(f"\nFeatures selected: {list(X.columns)}")
    print(f"Numerical Features: {numeric_features}")
    print(f"Categorical Features: {categorical_features}")
    
    # Create preprocessing pipeline
    # Numerical: Median imputation handles missing incomes/amounts, scaling normalizes coefficients
    numeric_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler())
    ])
    
    # Categorical: Impute missing flags with the mode, then One-Hot encode categories (dropping first to avoid multicollinearity)
    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('onehot', OneHotEncoder(handle_unknown='ignore', drop='first', sparse_output=False))
    ])
    
    # Preprocessor column transformer
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features)
        ])
    
    # Split the dataset using stratification to maintain class balance
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, stratify=y, random_state=42
    )
    
    print(f"\nTrain size: {X_train.shape[0]}, Test size: {X_test.shape[0]}")
    
    # Fit the preprocessor on training data only to avoid data leakage
    preprocessor.fit(X_train)
    
    # Save the fitted preprocessor
    joblib.dump(preprocessor, 'model/preprocessor.pkl')
    print("Preprocessor pipeline saved as 'model/preprocessor.pkl'")
    
    # Models dict
    models = {
        'Logistic Regression': LogisticRegression(random_state=42, max_iter=1000),
        'K-Nearest Neighbors': KNeighborsClassifier(n_neighbors=5),
        'Support Vector Machine': SVC(kernel='rbf', probability=True, random_state=42),
        'Decision Tree': DecisionTreeClassifier(max_depth=5, random_state=42)
    }
    
    print("\n" + "=" * 60)
    print("MODEL TRAINING & EVALUATION")
    print("=" * 60)
    
    metrics_summary = {}
    confusion_matrices = {}
    
    # Transform data for training and testing
    X_train_transformed = preprocessor.transform(X_train)
    X_test_transformed = preprocessor.transform(X_test)
    
    # Train and evaluate each model
    for name, model in models.items():
        print(f"\nTraining {name}...")
        model.fit(X_train_transformed, y_train)
        
        # Predict
        y_pred = model.predict(X_test_transformed)
        
        # Compute metrics
        acc = accuracy_score(y_test, y_pred)
        prec = precision_score(y_test, y_pred, zero_division=0)
        rec = recall_score(y_test, y_pred, zero_division=0)
        f1 = f1_score(y_test, y_pred, zero_division=0)
        cm = confusion_matrix(y_test, y_pred)
        
        metrics_summary[name] = {
            'accuracy': float(acc),
            'precision': float(prec),
            'recall': float(rec),
            'f1': float(f1)
        }
        
        confusion_matrices[name] = cm.tolist()
        
        print(f"Results for {name}:")
        print(f" - Accuracy  : {acc:.4f}")
        print(f" - Precision : {prec:.4f}")
        print(f" - Recall    : {rec:.4f}")
        print(f" - F1-Score  : {f1:.4f}")
        print(f" - Confusion Matrix:\n{cm}")
        
    # Model Comparison Plot
    print("\n" + "=" * 60)
    print("MODEL COMPARISON")
    print("=" * 60)
    
    model_names = list(metrics_summary.keys())
    accuracies = [metrics_summary[m]['accuracy'] for m in model_names]
    precisions = [metrics_summary[m]['precision'] for m in model_names]
    recalls = [metrics_summary[m]['recall'] for m in model_names]
    f1_scores = [metrics_summary[m]['f1'] for m in model_names]
    
    comparison_df = pd.DataFrame({
        'Model': model_names,
        'Accuracy': accuracies,
        'Precision': precisions,
        'Recall': recalls,
        'F1-Score': f1_scores
    })
    print(comparison_df.to_string(index=False))
    
    # Generate model comparison bar chart
    plt.figure(figsize=(12, 7))
    x = np.arange(len(model_names))
    width = 0.2
    
    plt.bar(x - 1.5*width, accuracies, width, label='Accuracy', color='#1e3a8a')
    plt.bar(x - 0.5*width, precisions, width, label='Precision', color='#0ea5e9')
    plt.bar(x + 0.5*width, recalls, width, label='Recall', color='#059669')
    plt.bar(x + 1.5*width, f1_scores, width, label='F1-Score', color='#d97706')
    
    plt.xlabel('Machine Learning Models')
    plt.ylabel('Score')
    plt.title('Performance Metrics Comparison of Classification Models')
    plt.xticks(x, model_names)
    plt.ylim(0, 1.1)
    plt.legend(loc='lower right')
    plt.tight_layout()
    plt.savefig('static/visualizations/model_comparison.png', dpi=300)
    plt.close()
    
    # Generate Confusion Matrix subplots
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    axes = axes.flatten()
    
    for idx, name in enumerate(model_names):
        cm = np.array(confusion_matrices[name])
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=axes[idx], cbar=False,
                    xticklabels=['Rejected (0)', 'Approved (1)'],
                    yticklabels=['Rejected (0)', 'Approved (1)'])
        axes[idx].set_title(f'Confusion Matrix - {name}')
        axes[idx].set_xlabel('Predicted Label')
        axes[idx].set_ylabel('True Label')
        
    plt.tight_layout()
    plt.savefig('static/visualizations/confusion_matrices.png', dpi=300)
    plt.close()
    
    # Select Best Model based on F1-score
    print("\n" + "=" * 60)
    print("BEST MODEL SELECTION")
    print("=" * 60)
    best_model_name = max(metrics_summary, key=lambda k: metrics_summary[k]['f1'])
    best_f1 = metrics_summary[best_model_name]['f1']
    best_acc = metrics_summary[best_model_name]['accuracy']
    
    print(f"Selected Best Model: {best_model_name}")
    print(f"Criteria: Highest Validation F1-Score ({best_f1:.4f})")
    
    best_model = models[best_model_name]
    
    # Save best model
    joblib.dump(best_model, 'model/best_model.pkl')
    print("Best model successfully saved as 'model/best_model.pkl'")
    
    # Save meta information for app dashboard
    status_distribution = df['Loan_Status'].value_counts()
    model_info = {
        'total_records': int(df.shape[0]),
        'num_features': int(X.shape[1]),
        'num_models_trained': len(models),
        'best_model_name': best_model_name,
        'best_accuracy': float(best_acc),
        'best_f1_score': float(best_f1),
        'metrics_summary': metrics_summary,
        'confusion_matrices': confusion_matrices,
        'target_distribution': {
            'approved': int(status_distribution.get('Y', 0)),
            'rejected': int(status_distribution.get('N', 0))
        }
    }
    
    with open('model/model_info.pkl', 'wb') as f:
        joblib.dump(model_info, f)
    print("Model meta information saved as 'model/model_info.pkl'")
    print("=" * 60)

def main():
    check_directories()
    
    dataset_path = 'dataset/loan_data.csv'
    if not os.path.exists(dataset_path):
        print(f"ERROR: Dataset not found at {dataset_path}")
        print("Please check your download step or place the file manually.")
        return
        
    df = pd.read_csv(dataset_path)
    inspect_dataset(df)
    generate_visualizations(df)
    train_and_evaluate(df)

if __name__ == '__main__':
    main()
