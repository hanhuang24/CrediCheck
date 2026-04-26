# CrediCheck

## Smart Credit Assessment & Loan Approval Dashboard

CrediCheck is a Streamlit-based interactive loan approval decision-support dashboard developed for academic demonstration and exploratory analytics. It combines machine learning prediction, dataset inspection, visual analytics, and user feedback collection in a finance-style interface.

## Live Links

- **Streamlit App:** https://credicheck-yj2eqrickemdqmjctdesnt.streamlit.app/
- **GitHub Repository:** https://github.com/hanhuang24/CrediCheck
- **Demo Video:** [Replace with your Mediasite / video link]

---

## Problem and Intended Users

Loan approval decisions often require reviewing multiple applicant features, such as income, credit score, loan amount, and asset values. This project explores how a machine learning-assisted dashboard can support loan-related analysis and early-stage decision support in a more interactive and transparent way.

**Intended users may include:**
- credit assessment staff
- risk analysts
- small lending platform reviewers
- business screening staff
- students learning applied machine learning deployment

This tool is designed for **academic demonstration, exploratory analysis, and model-assisted decision support**, rather than fully automated real-world lending decisions.

---

## Project Objectives

The main objectives of CrediCheck are to:

- build an interactive web-based dashboard for loan approval assessment
- support both **single applicant prediction** and **batch CSV prediction**
- help users inspect and understand the underlying dataset
- visualise key patterns related to loan outcomes
- demonstrate how machine learning can assist financial decision support
- provide a clear and user-friendly Streamlit interface

---

## Key Features

### 1. Single Prediction
Users can manually enter applicant information and receive a model-based approval prediction.

### 2. Batch CSV Prediction
Users can upload a CSV file and generate predictions for multiple applicants at once.

### 3. Prediction History Export
The app stores prediction records during the current session and allows export as CSV.

### 4. Risk Management Guidance
The dashboard provides practical review suggestions and basic manual checking guidance based on prediction outcomes.

### 5. Interactive Visual Analytics
The app includes charts such as:
- loan outcome distribution
- income distribution
- loan amount distribution
- CIBIL score comparison
- correlation heatmap
- feature importance
- time trend analysis (if a suitable date column exists)

### 6. Dataset Insights
Users can inspect:
- dataset summary
- schema
- missing values
- descriptive statistics
- target distribution
- filterable data preview

### 7. User Feedback Module
Users can submit feedback, download feedback records, delete selected entries, or clear all records.

### 8. Custom Streamlit UI Styling
The dashboard uses custom CSS to create a more polished finance-style interface.

---

## System Overview

CrediCheck is structured as a multi-section Streamlit dashboard with the following modules:

1. **Overview**
   - project purpose
   - features
   - usage scenarios
   - FAQ
   - responsible use statement

2. **Smart Prediction**
   - single applicant prediction
   - batch CSV prediction
   - prediction history

3. **Risk Management Guidelines**
   - operational suggestions
   - manual review checklist
   - compliance awareness reminders

4. **Visual Analytics**
   - interactive charts based on the loaded dataset
   - feature importance and distribution analysis

5. **Dataset Insights**
   - data structure
   - quality summary
   - descriptive statistics
   - missing value inspection
   - target balance
   - filterable preview

6. **User Feedback & Support**
   - feedback submission
   - feedback download
   - record management

---

## Repository Structure

```text
CrediCheck/
├── app.py                    # Main Streamlit application
├── deployment_package.pkl    # Trained model package
├── loan_approval_dataset.csv # Dataset used in the dashboard
├── logo.png                  # Optional logo image
├── user_feedback.csv         # Feedback records generated during usage
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
