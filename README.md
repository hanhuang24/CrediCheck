# CrediCheck
A Streamlit loan approval support tool combining data insights, prediction, and responsible use guidance.
## Coursework Information

- **Module:** [Your Module Name]
- **Assignment Title:** Final Project / Dashboard Development
- **Student Name:** [Your Name]
- **Student ID:** [Your Student ID]
- **Institution:** Xi’an Jiaotong-Liverpool University
- **Submission Type:** Individual Coursework
- # CrediCheck: Smart Credit Assessment and Loan Approval Dashboard

## Module Project README

---

## 1. Project Title

**CrediCheck: Smart Credit Assessment and Loan Approval Dashboard**

---

## 2. Project Overview

CrediCheck is an interactive dashboard developed using **Python** and **Streamlit** for academic demonstration purposes. The system is designed to support loan approval analysis through a combination of predictive modelling, visual analytics, dataset exploration, and user feedback collection.

The project aims to simulate a simplified decision-support environment in which users can input applicant information, generate loan approval predictions, inspect relevant data patterns, and review supporting risk management guidance. In addition, the dashboard includes dataset quality inspection and a feedback mechanism to support continuous system improvement.

This project was developed as part of an academic coursework submission and is intended for demonstration, analysis, and presentation purposes only.

---

## 3. Project Objectives

The main objectives of this project are:

- to design and implement an interactive credit assessment dashboard;
- to integrate a machine learning model for loan approval prediction;
- to provide clear and accessible data visualisation for users;
- to support exploratory analysis of a loan approval dataset;
- to demonstrate the use of dashboard-based decision-support tools in a finance-related scenario;
- to collect user feedback for future development and refinement.

---

## 4. Key Features

The dashboard is organised into six main functional modules:

### 4.1 Overview
This section introduces the dashboard and presents:
- system purpose;
- capability summary;
- model performance metrics;
- example user scenarios;
- responsible use guidance.

### 4.2 Smart Prediction
This module allows users to generate predictions in two ways:

#### Single Prediction
Users can manually enter applicant information such as:
- number of dependents;
- annual income;
- loan amount;
- loan term;
- CIBIL score;
- residential, commercial, luxury, and bank asset values;
- education status;
- self-employment status.

The system returns a prediction result indicating whether the loan is estimated to be approved or rejected. If the model supports probability outputs, the interface also displays approval and rejection probabilities.

#### Batch Prediction
Users can upload a CSV file containing multiple applicant records. The dashboard performs predictions for all uploaded entries and allows the results to be downloaded as a CSV file.

#### Prediction History
Predictions made during the current session are stored temporarily and displayed in a history table. Users may also export this history or clear it when required.

### 4.3 Risk Management Guidelines
This page provides practical guidance related to:
- recommended actions based on prediction outcome;
- operational risk checklist completion;
- risk category descriptions;
- compliance awareness notes.

This section is included to demonstrate how model output may be supported by simple business-oriented interpretation and review steps.

### 4.4 Visual Analytics
The visual analytics page presents charts and plots generated from the loaded dataset, including:
- loan outcome distribution;
- annual income distribution;
- loan amount distribution;
- CIBIL score comparison by target outcome;
- correlation heatmap of numeric variables;
- feature importance chart based on the deployed model;
- time trend analysis if a suitable date column is available.

### 4.5 Dataset Insights
This page allows users to explore the loaded dataset through:
- dataset summary;
- target column identification;
- data quality scoring;
- schema inspection;
- missing value analysis;
- descriptive statistics;
- numeric feature summary;
- target distribution analysis;
- filtered dataset preview and export.

### 4.6 User Feedback and Support
This module allows users to:
- submit structured feedback;
- indicate their role and feedback type;
- provide a satisfaction rating;
- leave free-text comments;
- view recent feedback records;
- download feedback records;
- delete selected feedback records;
- clear all feedback records.

---

## 5. Technologies Used

The following technologies and libraries were used in this project:

- **Python**
- **Streamlit**
- **Pandas**
- **NumPy**
- **Matplotlib**
- **Seaborn**
- **Pickle**
- **Pillow**

These tools were selected to support data processing, interactive dashboard creation, model deployment, and visualisation.

---

## 6. Project Files

The main project files are as follows:

```bash
app.py
loan_approval_dataset.csv
deployment_package.pkl
user_feedback.csv
logo.png
README.md
