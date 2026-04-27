# CrediCheck: Loan Applicant Risk Analysis Tool

**Module:** ACC102  
**Track:** Track 4 – Interactive Data Analysis Tool  
**Repository Link:** https://github.com/hanhuang24/CrediCheck  
**App Link:**  https://credicheck-yj2eqrickemdqmjctdesnt.streamlit.app/  
**Demo Video:**  https://video.xjtlu.edu.cn/Mediasite/MyMediasite/embedded/presentations/6aee3d4b6bc14ebea182e82fc83ab1b01d
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
- **Source:**   https://www.kaggle.com/datasets/architsharma01/loan-approval-prediction-dataset
- **Date accessed:** 2026.4.27  

### Main variables include:
- Number of Dependents of the Applicant  
- Education of the Applicant  
- Employment Status of the Applicant 
- Annual Income of the Applicant  
- Loan Amount  
- Loan Term in Years  
- Credit Score  
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
├── deployment_package.pkl
├── logo.png
└── user_feedback.txt                          
```
---

## 9. How to Run the Project Locally
This Track 4 project is designed to run locally after cloning the repository.  
(If the download fails and the app cannot be run, you can directly click on the app link to view it.)
### Step 1: Clone the repository
git clone https://github.com/hanhuang24/CrediCheck.git  
cd CrediCheck
### Step 2: Install required packages
pip install -r requirements.txt
### Step 3: Run the Streamlit app
streamlit run app.py
### Step 4: Open the app
After the command runs, Streamlit will provide a local URL in the terminal, usually:  
http://localhost:8501

---

## 10. Required Packages
Typical packages used in this project include:  
- pandas  
- numpy  
- matplotlib  
- seaborn  
- scikit-learn  
- streamlit

All required packages should be listed in requirements.txt.

---

## 11.Key Outputs
This project produces two main types of outputs:  

Analytical Outputs
- summary statistics and data exploration results
- comparisons between approved and rejected applicants
- visualisations of important variables

Interactive Outputs
- user-entered applicant profile
- model-based prediction result
- a simple interface for interpreting loan-related risk patterns

The tool demonstrates how Python analysis can be transformed into a practical user-facing product.

---

## 12. Interpretation and Value
The project suggests that applicant-level characteristics such as income, credit history, and asset-related variables may be associated with loan approval outcomes.  
The value of the tool is not that it makes real lending decisions, but that it helps users:  
- understand how structured applicant data can be analysed
- see how a predictive workflow can be implemented in Python
- interact with a simple data product rather than only reading notebook outputs

---

## 13. Limitations
This project has several important limitations:  

- the dataset is relatively simple and may not fully represent real-world lending environments
- the model is intended for educational demonstration only
- predictions should not be used as real financial decisions
- some important real-world factors may not be included in the dataset
- model outputs depend on the quality and scope of the available data

Because of these limitations, the project should be understood as a learning-oriented prototype rather than a production-ready credit scoring system.

---

## 14. Future Improvements
If more time were available, this project could be improved by:  
- testing additional machine learning models
- improving model explainability
- adding fairness and bias analysis
- improving the visual design of the interface
- expanding the dataset with more realistic financial variables
- saving the full preprocessing and modelling pipeline more formally
- enhancing the app with clearer probability interpretation and user guidance

---

## 15. Disclaimer
This project is intended for educational purposes only.  
It is not a real credit scoring system and should not be used for actual lending or financial approval decisions.

---

## 16. Author
- Student Name: han huang
- Module: ACC102
- Track: Track 4 – Interactive Data Analysis Tool
