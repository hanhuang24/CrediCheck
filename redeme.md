# CrediCheck: Loan Applicant Risk Analysis Tool

**Module:** ACC102  
**Track:** Track 4 – Interactive Data Analysis Tool  
**Repository Link:** https://github.com/hanhuang24/CrediCheck  
**App Link:** [Insert your app link here, if available]  
**Demo Video:** [Insert your 1–3 minute Mediasite video link here]  

---

## 1. Project Overview

CrediCheck is an interactive data analysis tool designed to explore loan applicant data and support basic loan risk assessment.  
The project combines Python-based data cleaning, exploratory data analysis, machine learning, and a Streamlit interface to help users understand how applicant characteristics may relate to loan approval outcomes.

This project was developed for the **ACC102 Mini Assignment (Track 4)**.

---

## 2. Problem Statement

Loan providers often need to make quick and consistent decisions when reviewing applications.  
This project explores the following question:

**Can applicant information such as income, education, employment status, asset values, and credit history help predict loan approval outcomes?**

The goal is not to replace real financial decision-making, but to build an educational data product that demonstrates how Python analysis can be turned into a simple and usable interactive tool.

---

## 3. Target Users

This tool is intended for users such as:

- loan screening staff in banks or financial institutions  
- risk control analysts  
- small lending platforms  
- business staff conducting initial applicant reviews  
- students who want to learn how machine learning can be deployed in an interactive data product  

These users may benefit from a simple interface that combines data exploration with prediction outputs.

---

## 4. Dataset

- **Dataset name:** `loan_approval_dataset.csv`  
- **Source:** [Insert original dataset source link here]  
- **Date accessed:** [Insert access date here]  

### Main variables include:
- applicant income  
- co-applicant income  
- loan amount  
- loan term  
- credit history  
- education  
- self-employment status  
- residential asset value  
- commercial asset value  
- luxury asset value  
- bank asset value  
- loan approval status  

### Why this dataset was chosen
This dataset was chosen because it contains structured applicant-level variables that are relevant to loan approval analysis.  
It is suitable for educational use because it allows data cleaning, visual analysis, and predictive modelling within a manageable project scope.

---

## 5. Project Objectives

The main objectives of this project are:

1. to explore patterns in loan applicant data  
2. to identify variables associated with loan approval outcomes  
3. to build a basic predictive model using Python  
4. to create an interactive Streamlit tool that allows users to input applicant information and view prediction results  

---

## 6. Methods and Workflow

The project followed these main steps:

### 6.1 Data Preparation
- imported the dataset into Python  
- checked data types and general structure  
- cleaned the dataset and prepared variables for analysis  
- selected relevant features for modelling  

### 6.2 Exploratory Data Analysis
- examined the distribution of key variables  
- compared approved and rejected applicants  
- created visualisations to identify useful patterns  

### 6.3 Model Development
- prepared input features and target labels  
- trained a classification model to predict loan approval outcomes  
- evaluated model behaviour using standard testing procedures  

### 6.4 Interactive Tool Development
- built a Streamlit interface  
- created pages for data analysis and prediction  
- added feature-column matching checks  
- added exception handling to improve reliability  
- included a limitations section to support responsible interpretation  

---

## 7. Main Features of the Tool

The tool includes the following functions:

### Data Analysis Page
Users can explore the dataset through summary information and visual outputs.

### Prediction Page
Users can enter applicant information and receive a prediction based on the trained model.

### Feature Matching Checks
The app checks whether the app input structure matches the trained model feature structure, reducing prediction errors caused by column mismatch.

### Error Handling
The tool includes exception handling so that invalid input or unexpected issues are managed more safely.

### Limitations Page
The app explains the boundaries of the analysis and reminds users that the project is for educational purposes only.

---

## 8. Repository Structure

A suggested repository structure for this project is shown below:

```text
CrediCheck/
│
├── README.md
├── app.py
├── notebook.ipynb
├── loan_approval_dataset.csv
├── requirements.txt
├── figures/                # optional: charts or screenshots
└── models/                 # optional: saved model files
