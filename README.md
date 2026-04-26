```markdown
# CrediCheck

### Smart Credit Assessment & Loan Approval Dashboard

CrediCheck is a Streamlit-based loan approval decision-support dashboard designed for academic demonstration and exploratory analytics. It combines machine learning prediction, dataset inspection, visual analytics, and user feedback collection in a clean finance-style interface.

🔗 **Live Demo:** https://credicheck-yj2eqrickemdqmjctdesnt.streamlit.app/  
🔗 **GitHub Repository:** https://github.com/hanhuang24/CrediCheck

---

## Highlights
- Single applicant prediction
- Batch CSV prediction
- Risk management guidance
- Interactive visual analytics
- Dataset quality inspection
- Prediction history export
- User feedback management
# CrediCheck

> Smart Credit Assessment & Loan Approval Dashboard built with Streamlit for academic demonstration, exploratory analysis, and model-assisted lending decision support.

## Live Demo
🔗 Streamlit App: https://credicheck-yj2eqrickemdqmjctdesnt.streamlit.app/

## GitHub Repository
🔗 GitHub: https://github.com/hanhuang24/CrediCheck

---

## 1. Introduction

**CrediCheck** is an interactive **loan approval decision-support dashboard** developed using **Streamlit**.  
It is designed to help users explore loan applicant data, generate model-based approval predictions, review dataset quality, and interpret visual analytics in a finance-style interface.

This project combines:
- **machine learning prediction**
- **interactive dashboard design**
- **data quality inspection**
- **visual analytics**
- **user feedback collection**

The system is intended for **academic demonstration and exploratory analysis**, rather than fully automated real-world lending decisions.

---

## 2. Project Objectives

The main objectives of this project are:

- Build an interactive web-based dashboard for **loan approval assessment**
- Provide **single** and **batch prediction** functionality
- Visualise applicant and dataset patterns for better understanding
- Support more transparent interpretation of loan-related features
- Demonstrate how machine learning can assist decision-making in financial scenarios
- Offer a professional and user-friendly interface through Streamlit

---

## 3. Key Features

### Core Features
- ✅ **Single Prediction**
  - Users can manually input applicant information and receive a model-based approval result.

- ✅ **Batch Prediction**
  - Users can upload a CSV file and generate predictions for multiple applicants at once.

- ✅ **Prediction History**
  - The application stores prediction records during the current session and allows export as CSV.

- ✅ **Risk Management Guidelines**
  - Provides practical interpretation and review suggestions based on prediction outcomes.

- ✅ **Visual Analytics**
  - Includes charts such as:
    - loan outcome distribution
    - income distribution
    - loan amount distribution
    - CIBIL score comparison
    - correlation heatmap
    - feature importance
    - time trend analysis (if date column exists)

- ✅ **Dataset Insights**
  - Displays dataset summary, schema, missing values, descriptive statistics, target distribution, and filterable previews.

- ✅ **User Feedback Module**
  - Users can submit feedback, download feedback records, delete selected records, or clear all records.

- ✅ **Custom UI Styling**
  - Uses custom CSS to create a modern, polished, finance-style dashboard appearance.

---

## 4. System Overview

CrediCheck is structured as a **multi-tab Streamlit dashboard** with the following modules:

1. **Overview**
   - Introduces the product, features, model metrics, common scenarios, and FAQ.

2. **Smart Prediction**
   - Supports:
     - single applicant prediction
     - batch CSV prediction
     - prediction history tracking

3. **Risk Management Guidelines**
   - Provides operational guidance and manual review checklist.

4. **Visual Analytics**
   - Displays charts and feature importance using the real loaded dataset.

5. **Dataset Insights**
   - Examines structure, quality, statistics, and target balance of the dataset.

6. **User Feedback & Support**
   - Records user feedback and provides support information.

---

## 5. Project Structure

```bash
CrediCheck/
│
├── app.py                      # Main Streamlit application
├── deployment_package.pkl      # Trained model package
├── loan_approval_dataset.csv   # Dataset used in the dashboard
├── logo.png                    # Logo image (optional)
├── user_feedback.csv           # Feedback records generated during usage
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
File Description
app.py: main dashboard application
deployment_package.pkl: stores trained model, scaler, feature columns, model name, and metrics
loan_approval_dataset.csv: dataset loaded for analysis and visualisation
logo.png: optional branding image used in page configuration
user_feedback.csv: generated feedback file for storing submitted comments
requirements.txt: dependency file for reproducibility
￼
6. Technologies Used
Programming Language
Python
Main Libraries
Streamlit – dashboard development
Pandas – data loading and manipulation
NumPy – numerical operations
Matplotlib – plotting
Seaborn – statistical visualisation
Pickle – model package loading
Pillow (PIL) – image/logo loading
os – file path handling
Machine Learning Support
The application loads a pre-trained model from deployment_package.pkl, which may include:
model
scaler
feature columns
performance metrics
￼
7. Installation
Prerequisites
Please make sure you have:
Python 3.9 or above
pip installed
Clone the Repository
bash
Copy
git clone
 https://github.com/hanhuang24/CrediCheck.git
cd CrediCheck
Install Dependencies
bash
Copy
pip install -r requirements.txt
￼
8. Running the Project
To launch the Streamlit app locally:
bash
Copy
streamlit run app.py
After running the command, Streamlit will provide a local URL, usually:
bash
Copy
http://localhost:8501
￼
9. Deployment
This project has been deployed on Streamlit Community Cloud.
Online Access
https://credicheck-yj2eqrickemdqmjctdesnt.streamlit.app/
This allows users to access the dashboard without setting up the environment locally.
￼
10. Input Requirements
Single Prediction Input Fields
The prediction form currently includes:
no_of_dependents
income_annum
loan_amount
loan_term
cibil_score
residential_assets_value
commercial_assets_value
luxury_assets_value
bank_asset_value
education
self_employed
Batch Prediction Input
Users can upload a CSV file.
The system:
reads the uploaded file
strips extra spaces from column names
performs one-hot encoding if necessary
aligns columns to the trained model feature list
fills missing features with 0
returns prediction results with probabilities if supported
￼
11. Methodology
11.1 Data Loading
The dashboard loads the dataset from:
bash
Copy
loan_approval_dataset.csv
It automatically:
checks whether the file exists
reads the CSV file
strips whitespace from column names
11.2 Model Loading
The trained package is loaded from:
bash
Copy
deployment_package.pkl
The package is expected to contain:
model
feature_columns
scaler
model_name
metrics
11.3 Prediction Pipeline
The prediction workflow is:
text
Copy
User Input / Uploaded CSV
        ↓
DataFrame Construction
        ↓
One-Hot Encoding (if needed)
        ↓
Feature Alignment to Training Columns
        ↓
Scaling (if scaler exists)
        ↓
Model Prediction
        ↓
Result + Probability Output
11.4 Visual Analytics
The dashboard generates analytics only from the currently loaded real dataset.
Visualisations are conditional, meaning plots are shown only if the required columns are available.
11.5 Data Quality Inspection
The application computes a simple dataset quality score based on:
completeness
uniqueness
validity
consistency
It also provides schema information, missing values, descriptive statistics, and filtered dataset previews.
￼
12. Dashboard Pages
12.1 Overview
This page introduces:
project purpose
current capabilities
model performance
user scenarios
FAQ
responsible use statement
12.2 Smart Prediction
This page supports:
Single Prediction
Batch Prediction
Prediction History
12.3 Risk Management Guidelines
This page includes:
recommended actions for approved/rejected predictions
a manual review checklist
risk category guidance
compliance awareness reminders
12.4 Visual Analytics
This page may display:
loan outcome distribution
loan amount distribution
annual income distribution
CIBIL score by outcome
correlation heatmap
feature importance
monthly application trend
12.5 Dataset Insights
This page includes:
dataset summary
quality score
dataset filter
schema and missing values
descriptive statistics
numeric feature summary
target distribution
CSV export of filtered data
12.6 User Feedback & Support
This page includes:
feedback submission form
support information
recent feedback records
download feedback data
record deletion tools
￼
13. Results and Functionality Demonstration
Prediction Output
For each applicant, the system can return:
predicted label:
Approved
Rejected
probability scores (if predict_proba is available)
Analytics Output
The dashboard supports chart-based interpretation of:
applicant financial patterns
target variable distribution
relationships between features
model feature importance
Session Output
Users can:
view previous predictions in the current session
export prediction history as CSV
Feedback Output
Users can:
submit comments
save them to user_feedback.csv
export feedback records
delete specific entries
clear all entries
￼
14. Example Use Cases
Use Case 1: Manual Applicant Review
A user enters applicant income, assets, liabilities, education, and employment information to obtain a model-generated approval estimate.
Use Case 2: Batch Scoring
A user uploads a CSV file of multiple applicants and downloads a result file containing predictions and probabilities.
Use Case 3: Dataset Exploration
A user investigates the structure and quality of the dataset through descriptive statistics, filtering, and visualisations.
Use Case 4: Academic Demonstration
The system can be used in coursework, project presentations, or demonstrations of applied machine learning and dashboard design.
￼
15. Strengths of the Project
This project demonstrates several strengths:
clear multi-module dashboard structure
practical integration of machine learning with Streamlit
strong focus on visual presentation and user experience
useful mix of prediction, analytics, and support features
exportable outputs for prediction and feedback workflows
appropriate responsible-use messaging for academic context
￼
16. Limitations
Current limitations include:
The dashboard depends on the availability of deployment_package.pkl
Prediction quality depends on the trained model and training data quality
The data quality score is a simplified indicator rather than a formal industry metric
Feedback is stored in a local CSV file, which is not suitable for large-scale production systems
The application is intended for academic demonstration rather than real banking deployment
Some advanced explainability methods (such as SHAP or LIME) are not yet included
￼
17. Future Improvements
Potential future work includes:
add model explainability tools such as SHAP
improve data quality scoring with more robust rules
integrate secure database storage for feedback
add user authentication and role-based access
support more file formats such as Excel
expand risk scoring logic beyond binary approval prediction
add downloadable PDF reports
improve production readiness with logging, monitoring, and exception management
add model retraining workflow and version control
provide richer documentation and user guide pages
￼
18. Reproducibility
To reproduce the project locally, ensure the following files are present in the project root:
app.py
loan_approval_dataset.csv
deployment_package.pkl
requirements.txt
Then run:
bash
Copy
pip install -r requirements.txt
streamlit run app.py
￼
19. Contribution
This project was completed by:
Han Huang
If this project is part of an academic submission, it represents the implementation of an interactive loan approval dashboard with predictive analytics and decision-support functionality.
￼
20. References
Possible references relevant to this project include:
Streamlit official documentation
Pandas documentation
NumPy documentation
Matplotlib documentation
Seaborn documentation
machine learning model documentation depending on the model used in deployment_package.pkl
Example:
Streamlit Documentation: https://docs.streamlit.io/
Pandas Documentation: https://pandas.pydata.org/
NumPy Documentation: https://numpy.org/
Matplotlib Documentation: https://matplotlib.org/
Seaborn Documentation: https://seaborn.pydata.org/
￼
21. Responsible Use Statement
CrediCheck is developed for:
academic demonstration
exploratory data analysis
model-assisted decision support
It should not be used as the sole basis for real-world lending decisions.
Any actual financial decision process should include:
human judgement
policy review
compliance checks
identity verification
fairness and responsible lending assessment
￼
22. Acknowledgements
Thanks to:
open-source Python and Streamlit communities
academic supervisors and instructors
contributors of the dataset and machine learning ecosystem

