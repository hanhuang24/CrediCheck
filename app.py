import os
import pickle
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# =========================================================
# Page Config
# =========================================================
logo = Image.open("logo.png") if os.path.exists("logo.png") else None

st.set_page_config(
    page_title="CrediCheck",
    page_icon=logo if logo else "📊",
    layout="wide"
)

# =========================================================
# Custom CSS
# =========================================================
st.markdown("""
<style>
:root {
    --bg-main: linear-gradient(135deg, #eef6ff 0%, #e9f2ff 45%, #f7fbff 100%);
    --bg-orb-1: rgba(59,130,246,0.20);
    --bg-orb-2: rgba(99,102,241,0.16);
    --bg-orb-3: rgba(16,185,129,0.10);

    --text-main: #0f172a;
    --text-soft: #334155;
    --text-muted: #64748b;

    --glass-bg: rgba(255, 255, 255, 0.55);
    --glass-bg-strong: rgba(255, 255, 255, 0.72);
    --glass-border: rgba(255, 255, 255, 0.45);
    --glass-shadow: 0 8px 32px rgba(31, 38, 135, 0.12);

    --input-bg: rgba(255,255,255,0.48);
    --input-border: rgba(148,163,184,0.28);

    --tab-bg: rgba(255,255,255,0.42);
    --tab-text: #1e3a8a;
    --tab-border: rgba(255,255,255,0.40);
    --tab-active-bg: linear-gradient(135deg, rgba(37,99,235,0.92), rgba(59,130,246,0.92));
    --tab-active-text: #ffffff;
    --tab-active-border: rgba(255,255,255,0.20);

    --btn-bg: linear-gradient(135deg, rgba(37,99,235,0.95), rgba(59,130,246,0.95));
    --btn-hover-bg: linear-gradient(135deg, rgba(29,78,216,0.98), rgba(37,99,235,0.98));
    --btn-text: #ffffff;

    --badge-bg: rgba(34,197,94,0.14);
    --badge-text: #15803d;
    --badge-border: rgba(34,197,94,0.22);

    --table-border: rgba(148,163,184,0.24);
}

@media (prefers-color-scheme: dark) {
    :root {
        --bg-main: linear-gradient(135deg, #07111f 0%, #0b1220 45%, #111827 100%);
        --bg-orb-1: rgba(59,130,246,0.18);
        --bg-orb-2: rgba(139,92,246,0.14);
        --bg-orb-3: rgba(16,185,129,0.08);

        --text-main: #f8fafc;
        --text-soft: #dbeafe;
        --text-muted: #94a3b8;

        --glass-bg: rgba(15, 23, 42, 0.45);
        --glass-bg-strong: rgba(15, 23, 42, 0.62);
        --glass-border: rgba(255, 255, 255, 0.10);
        --glass-shadow: 0 8px 32px rgba(0, 0, 0, 0.35);

        --input-bg: rgba(15,23,42,0.42);
        --input-border: rgba(148,163,184,0.18);

        --tab-bg: rgba(15,23,42,0.42);
        --tab-text: #e2e8f0;
        --tab-border: rgba(255,255,255,0.08);
        --tab-active-bg: linear-gradient(135deg, rgba(37,99,235,0.92), rgba(96,165,250,0.92));
        --tab-active-text: #ffffff;
        --tab-active-border: rgba(255,255,255,0.10);

        --btn-bg: linear-gradient(135deg, rgba(37,99,235,0.95), rgba(96,165,250,0.95));
        --btn-hover-bg: linear-gradient(135deg, rgba(29,78,216,0.98), rgba(59,130,246,0.98));
        --btn-text: #ffffff;

        --badge-bg: rgba(34,197,94,0.14);
        --badge-text: #86efac;
        --badge-border: rgba(34,197,94,0.24);

        --table-border: rgba(148,163,184,0.16);
    }
}

html, body, [class*="css"], .stApp {
    font-family: "Inter", "Segoe UI", sans-serif;
    color: var(--text-main) !important;
}

.stApp {
    background:
        radial-gradient(circle at 0% 0%, var(--bg-orb-1), transparent 30%),
        radial-gradient(circle at 100% 0%, var(--bg-orb-2), transparent 28%),
        radial-gradient(circle at 50% 100%, var(--bg-orb-3), transparent 24%),
        var(--bg-main);
    background-attachment: fixed;
}

.block-container {
    max-width: 1280px;
    padding-top: 1.2rem;
    padding-bottom: 2rem;
}

p, span, label, div, h1, h2, h3, h4, h5, h6 {
    color: var(--text-main);
}

h1, h2, h3 {
    letter-spacing: -0.02em;
}

[data-testid="stMarkdownContainer"] * {
    color: var(--text-main) !important;
}

.glass-card,
.metric-card,
.feature-card,
.hero-box {
    background: var(--glass-bg);
    border: 1px solid var(--glass-border);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    box-shadow: var(--glass-shadow);
    color: var(--text-main) !important;
}

.hero-box {
    border-radius: 24px;
    padding: 28px 30px;
    background: var(--glass-bg-strong);
    position: relative;
    overflow: hidden;
}

.hero-box::before {
    content: "";
    position: absolute;
    inset: 0;
    background: linear-gradient(
        120deg,
        rgba(255,255,255,0.18) 0%,
        rgba(255,255,255,0.04) 35%,
        rgba(255,255,255,0.00) 100%
    );
    pointer-events: none;
}

.metric-card {
    border-radius: 20px;
    padding: 20px 22px;
}

.feature-card {
    border-radius: 20px;
    padding: 22px;
    min-height: 180px;
    transition: all 0.25s ease;
}

.feature-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 16px 40px rgba(31, 38, 135, 0.16);
}

.stTabs [data-baseweb="tab-list"] {
    gap: 10px;
    margin-bottom: 1rem;
    flex-wrap: wrap;
    background: transparent;
}

.stTabs [data-baseweb="tab"] {
    height: 50px;
    background: var(--tab-bg);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    border-radius: 16px;
    border: 1px solid var(--tab-border);
    color: var(--tab-text) !important;
    font-weight: 700;
    padding: 0 18px;
    box-shadow: var(--glass-shadow);
    transition: all 0.2s ease;
}

.stTabs [data-baseweb="tab"]:hover {
    transform: translateY(-1px);
}

.stTabs [aria-selected="true"] {
    background: var(--tab-active-bg) !important;
    color: var(--tab-active-text) !important;
    border: 1px solid var(--tab-active-border) !important;
}

div[data-baseweb="input"] > div,
div[data-baseweb="select"] > div,
div[data-baseweb="textarea"] > div {
    border-radius: 16px !important;
    border: 1px solid var(--input-border) !important;
    background: var(--input-bg) !important;
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    color: var(--text-main) !important;
    box-shadow: inset 0 1px 0 rgba(255,255,255,0.08);
}

input, textarea, select {
    color: var(--text-main) !important;
    background: transparent !important;
}

input::placeholder,
textarea::placeholder {
    color: var(--text-muted) !important;
}

.stButton > button {
    background: var(--btn-bg);
    color: var(--btn-text) !important;
    border: 1px solid rgba(255,255,255,0.14);
    border-radius: 16px;
    padding: 0.82rem 1.1rem;
    font-size: 1rem;
    font-weight: 800;
    letter-spacing: 0.01em;
    box-shadow: 0 10px 24px rgba(37,99,235,0.28);
    transition: all 0.22s ease;
}

.stButton > button:hover {
    background: var(--btn-hover-bg);
    color: var(--btn-text) !important;
    transform: translateY(-1px);
    box-shadow: 0 14px 28px rgba(37,99,235,0.34);
}

[data-testid="stDataFrame"] {
    border: 1px solid var(--table-border);
    border-radius: 20px;
    overflow: hidden;
    background: var(--glass-bg);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
}


.status-badge {
    display: inline-block;
    padding: 8px 14px;
    border-radius: 999px;
    background: var(--badge-bg);
    color: var(--badge-text) !important;
    font-weight: 700;
    font-size: 14px;
    border: 1px solid var(--badge-border);
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
}

.small-muted {
    color: var(--text-muted) !important;
    font-size: 15px;
}


section[data-testid="stSidebar"] > div {
    background: var(--glass-bg-strong);
    backdrop-filter: blur(18px);
    -webkit-backdrop-filter: blur(18px);
}

div[data-testid="stForm"] {
    background: transparent;
}


details {
    background: var(--glass-bg);
    border: 1px solid var(--glass-border);
    border-radius: 18px;
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    padding: 4px 8px;
}

hr {
    border: none;
    height: 1px;
    background: linear-gradient(
        90deg,
        transparent,
        rgba(148,163,184,0.35),
        transparent
    );
    margin: 1.2rem 0;
}

::-webkit-scrollbar {
    width: 10px;
    height: 10px;
}
::-webkit-scrollbar-thumb {
    background: rgba(148,163,184,0.35);
    border-radius: 999px;
}
::-webkit-scrollbar-track {
    background: transparent;
}

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)
# =========================================================
# Helpers
# =========================================================
@st.cache_data
def load_data():
    file_path = os.path.join(BASE_DIR, 
"loan_approval_dataset.csv"
)
    if not os.path.exists(file_path):
        return None

    try:
        df = pd.read_csv(file_path)
        df.columns = df.columns.str.strip()
        return df
    except Exception:
        return None

@st.cache_resource
def load_package():
    package_path = os.path.join(BASE_DIR, "deployment_package.pkl")

    if not os.path.exists(package_path):
        st.error("deployment_package.pkl does not exist at expected path")
        return None, None, None, None, None

    try:
        with open(package_path, "rb") as f:
            package = pickle.load(f)

        return (
            package.get("model"),
            package.get("feature_columns"),
            package.get("scaler"),
            package.get("model_name"),
            package.get("metrics")
        )
    except Exception as e:
        st.error(f"Failed to load deployment_package.pkl: {e}")
        return None, None, None, None, None

def find_target_column(df):
    for col in ["loan_status", "Loan_Status", "status", "loan_approved"]:
        if col in df.columns:
            return col
    return None


def find_date_column(df):
    possible = ["date", "application_date", "created_at", "timestamp"]
    for col in possible:
        if col in df.columns:
            return col
    return None


def format_input_dataframe(input_dict, feature_columns):
    input_df = pd.DataFrame([input_dict])
    for col in feature_columns:
        if col not in input_df.columns:
            input_df[col] = 0
    return input_df[feature_columns]


def metric_box(label, value):
    st.markdown(f"""
    <div class="metric-card">
        <div class="small-muted">{label}</div>
        <div style="font-size:32px; font-weight:800; color:#18456f;">{value}</div>
    </div>
    """, unsafe_allow_html=True)


def info_card(title, text):
    st.markdown(f"""
    <div class="feature-card">
        <div style="font-size:22px; font-weight:800; color:#18456f;">{title}</div>
        <div class="small-muted" style="margin-top:10px;">{text}</div>
    </div>
    """, unsafe_allow_html=True)

def data_quality_score(df):
    default_details = {
        "completeness": 0,
        "uniqueness": 0,
        "validity": 0,
        "consistency": 0
    }

    if df is None or df.empty:
        return 0, default_details

    total_cells = df.shape[0] * df.shape[1]
    missing_cells = df.isna().sum().sum()

    completeness = 100 - (missing_cells / total_cells * 100) if total_cells > 0 else 0

    duplicate_rows = df.duplicated().sum()
    uniqueness = 100 - (duplicate_rows / len(df) * 100) if len(df) > 0 else 0

    validity = 100
    consistency = 100

    completeness = max(0, round(completeness, 2))
    uniqueness = max(0, round(uniqueness, 2))
    validity = max(0, round(validity, 2))
    consistency = max(0, round(consistency, 2))

    score = round((completeness + uniqueness + validity + consistency) / 4, 2)

    quality_details = {
        "completeness": completeness,
        "uniqueness": uniqueness,
        "validity": validity,
        "consistency": consistency
    }

    return score, quality_details
def normalize_prediction_label(prediction):
    if isinstance(prediction, str):
        pred = prediction.strip().lower()
        if pred in ["approved", "approve", "yes", "1", "true"]:
            return "Approved"
        elif pred in ["rejected", "reject", "no", "0", "false"]:
            return "Rejected"
        return str(prediction)

    try:
        if int(prediction) == 1:
            return "Approved"
        elif int(prediction) == 0:
            return "Rejected"
    except:
        pass

    return str(prediction)


def to_csv_download(df):
    return df.to_csv(index=False).encode("utf-8")


def prepare_prediction_input(input_df, feature_columns):
    """
    Make input dataframe compatible with training feature columns.
    Handles:
    - raw columns
    - one-hot encoding
    - training columns with unexpected spaces
    """
    df_input = input_df.copy()

    if feature_columns is None:
        return None

    if all(col in df_input.columns for col in feature_columns):
        return df_input[feature_columns]

    for col in df_input.select_dtypes(include="object").columns:
        df_input[col] = df_input[col].astype(str)

    df_encoded = pd.get_dummies(df_input)

    renamed_columns = {}
    for col in df_encoded.columns:
        for feat in feature_columns:
            # 忽略空格比较
            if col.replace(" ", "") == feat.replace(" ", ""):
                renamed_columns[col] = feat
                break

    df_encoded = df_encoded.rename(columns=renamed_columns)

    for col in feature_columns:
        if col not in df_encoded.columns:
            df_encoded[col] = 0

    df_encoded = df_encoded[feature_columns]

    return df_encoded
    
# =========================================================
# Load Data / Model
# =========================================================
df = load_data()
model, feature_columns, scaler, model_name, metrics = load_package()

# =========================================================
# Header
# =========================================================
st.markdown("<br>", unsafe_allow_html=True)

left, right = st.columns([6, 1.5])

with left:
    brand1, brand2 = st.columns([1.2, 6])

    with brand1:
        if logo:
            st.image(logo, width=120)

    with brand2:
        st.markdown(
            """
            <h1 style="margin-bottom: 0; color: #1f1f1f; font-size: 40px; font-weight: 700;">
                CrediCheck
            </h1>
            """,
            unsafe_allow_html=True
        )
        st.markdown(
            """
            <p style="margin-top: 6px; margin-bottom: 0; color: #6c757d; font-size: 16px;">
                Smart Credit Assessment & Loan Approval Dashboard
            </p>
            """,
            unsafe_allow_html=True
        )
        st.markdown(
            """
            <p style="margin-top: 8px; font-size: 14px; color: #8a8f98;">
                <span style="font-weight: 600;">Target Users:</span>
                Banks · Lenders · Risk Analysts
            </p>
            """,
            unsafe_allow_html=True
        )

with right:
    st.markdown(
        """
        <div style="text-align: right; padding-top: 10px;">
            <span style="
                display: inline-block;
                padding: 6px 14px;
                border-radius: 20px;
                font-size: 13px;
                font-weight: 600;
            ">
                ● System Ready
            </span>
        </div>
        """,
        unsafe_allow_html=True
    )
# =========================================================
# Quick Access
# =========================================================
st.markdown(
    "<h3 style='color:#123B6D; margin-bottom:16px;'>Quick Access</h3>",
    unsafe_allow_html=True
)

f1, f2, f3 = st.columns(3)

with f1:
    info_card(
        "Applicant Input",
        "Enter applicant profile, income, liabilities, and employment details for assessment."
    )

with f2:
    info_card(
        "Risk Evaluation",
        "Review risk indicators, credit score ranges, and model-based approval suggestions."
    )

with f3:
    info_card(
        "Decision Support",
        "Compare outcomes, inspect key factors, and support transparent lending decisions."
    )

st.markdown("<br>", unsafe_allow_html=True)

# =========================================================
# Navigation
# =========================================================
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "Overview",
    "Smart Prediction",
    "Risk Management Guidelines",
    "Visual Analytics",
    "Dataset Insights",
    "User Feedback & Support"
])

# =========================================================
# Tab 1 - Overview
# =========================================================
with tab1:
    st.markdown("## Product Overview")
    st.caption("A loan approval decision-support dashboard for academic demonstration and exploratory analysis.")

    # -------- Real project introduction --------
    info_card(
        "Platform Introduction",
        "CrediCheck is a premium loan approval support dashboard with advanced predictive modelling and finance-style analytics, designed to help users assess applicant risk, improve decision efficiency, and support more informed loan approval processes."
    )


    # -------- Real feature overview --------
    st.markdown("### Current Capabilities")

    col1, col2, col3 = st.columns(3)
    with col1:
        metric_box("Core Function", "Prediction")
        st.write("Generate a model-assisted estimate based on user-entered applicant information.")

    with col2:
        metric_box("Core Function", "Visual Analysis")
        st.write("Explore numeric distributions, target-related comparisons, and feature correlations.")

    with col3:
        metric_box("Core Function", "Risk Guidelines")
        st.write("Provide practical decision-support guidance based on model outcomes and risk awareness principles.")

    # -------- Real model performance --------
    st.markdown("### Model Performance")

    if metrics:
        m1, m2, m3, m4, m5 = st.columns(5)
        with m1:
            metric_box("Accuracy", metrics.get("accuracy", "N/A"))
        with m2:
            metric_box("Precision", metrics.get("precision", "N/A"))
        with m3:
            metric_box("Recall", metrics.get("recall", "N/A"))
        with m4:
            metric_box("F1-score", metrics.get("f1_score", "N/A"))
        with m5:
            metric_box("AUC", metrics.get("auc", "N/A"))
    else:
        st.warning("Model performance metrics are unavailable. Please check deployment_package.pkl.")


    # -------- Real use scenarios without fake claims --------
    st.markdown("### Typical User Scenarios")

    u1, u2 = st.columns(2)
    with u1:
        info_card(
            "Applicant Evaluation Scenario",
            "A user can enter applicant financial and profile information in the Smart Prediction page "
            "to obtain a model-generated approval estimate based on the currently deployed model."
        )

    with u2:
        info_card(
            "Dataset Review Scenario",
            "A user can inspect the loaded loan dataset, review descriptive statistics, "
            "and examine visual patterns related to income, loan amount, credit score, and target outcomes."
        )

    # -------- Real FAQ only based on current system --------
    with st.expander("FAQ - Frequently Asked Questions"):
        st.write("**Q1. What is CrediCheck?**")
        st.write("CrediCheck is a loan approval support dashboard that combines prediction, data inspection, and visual analytics in one interface.")

        st.write("**Q2. Does it make final loan decisions automatically?**")
        st.write("No. It supports decision-making, but final approval should always involve human judgment.")

        st.write("**Q3. What does the prediction result mean?**")
        st.write("It shows the model’s estimated outcome or risk level based on the applicant information provided.")

        st.write("**Q4. What data is used in the dashboard?**")
        st.write("The dashboard content is generated from the currently loaded dataset and deployment package.")

    # -------- Responsible use --------
    info_card(
        "Responsible Use",
        "This dashboard is intended for academic presentation, demonstration, and exploratory decision-support. "
        "It should not be treated as a substitute for formal credit policy, manual verification, compliance review, or professional judgement."
    )


# =========================================================
# Tab 2
# =========================================================
with tab2:
    st.markdown("## Smart Prediction")

    subtab1, subtab2, subtab3 = st.tabs([
        "Single Prediction",
        "Batch Prediction",
        "Prediction History"
    ])

    if "prediction_history" not in st.session_state:
        st.session_state.prediction_history = []

    prediction_ready = (model is not None and feature_columns is not None)

    # =====================================================
    # Subtab 1 - Single Prediction
    # =====================================================
    with subtab1:
        st.markdown("### Single Prediction")

        if not prediction_ready:
            st.warning("Prediction module is not available yet.")
            st.info("`deployment_package.pkl` has not been found or could not be loaded.")
            st.caption("You can still use the rest of the dashboard normally.")
        else:
            st.write("Enter applicant information to generate a prediction.")

            no_of_dependents = st.number_input("Number of Dependents", min_value=0, step=1)
            income_annum = st.number_input("Annual Income", min_value=0.0, step=1000.0)
            loan_amount = st.number_input("Loan Amount", min_value=0.0, step=1000.0)
            loan_term = st.number_input("Loan Term", min_value=1, step=1)
            cibil_score = st.number_input("CIBIL Score", min_value=0, max_value=900, step=1)
            residential_assets_value = st.number_input("Residential Assets Value", min_value=0.0, step=1000.0)
            commercial_assets_value = st.number_input("Commercial Assets Value", min_value=0.0, step=1000.0)
            luxury_assets_value = st.number_input("Luxury Assets Value", min_value=0.0, step=1000.0)
            bank_asset_value = st.number_input("Bank Asset Value", min_value=0.0, step=1000.0)
            education = st.selectbox("Education", ["Graduate", "Not Graduate"])
            self_employed = st.selectbox("Self Employed", ["Yes", "No"])

            if st.button("Predict", use_container_width=True):
                try:
                    input_df = pd.DataFrame([{
                        "no_of_dependents": no_of_dependents,
                        "income_annum": income_annum,
                        "loan_amount": loan_amount,
                        "loan_term": loan_term,
                        "cibil_score": cibil_score,
                        "residential_assets_value": residential_assets_value,
                        "commercial_assets_value": commercial_assets_value,
                        "luxury_assets_value": luxury_assets_value,
                        "bank_asset_value": bank_asset_value,
                        "education": education,
                        "self_employed": self_employed
                    }])

                    pred_input = prepare_prediction_input(input_df, feature_columns)

                    if pred_input is None:
                        st.error("Prediction input could not be prepared.")
                    else:
                        if scaler is not None:
                            pred_input_transformed = scaler.transform(pred_input)
                        else:
                            pred_input_transformed = pred_input

                        prediction = model.predict(pred_input_transformed)[0]
                        prediction_label = normalize_prediction_label(prediction)

                        st.success(f"Prediction Result: {prediction_label}")

                        approved_prob = None
                        rejected_prob = None

                        if hasattr(model, "predict_proba"):
                            proba = model.predict_proba(pred_input_transformed)[0]
                            if len(proba) >= 2:
                                rejected_prob = round(float(proba[0]) * 100, 2)
                                approved_prob = round(float(proba[1]) * 100, 2)
                                st.write(f"Rejected Probability: **{rejected_prob}%**")
                                st.write(f"Approved Probability: **{approved_prob}%**")

                        st.session_state.prediction_history.append({
                            "no_of_dependents": no_of_dependents,
                            "income_annum": income_annum,
                            "loan_amount": loan_amount,
                            "loan_term": loan_term,
                            "cibil_score": cibil_score,
                            "residential_assets_value": residential_assets_value,
                            "commercial_assets_value": commercial_assets_value,
                            "luxury_assets_value": luxury_assets_value,
                            "bank_asset_value": bank_asset_value,
                            "education": education,
                            "self_employed": self_employed,
                            "prediction": prediction_label,
                            "rejected_probability": rejected_prob,
                            "approved_probability": approved_prob
                        })

                except Exception as e:
                    st.error(f"Prediction failed: {e}")
            else:
                st.caption("No prediction has been generated yet.")

    # =====================================================
    # Subtab 2 - Batch Prediction
    # =====================================================
    with subtab2:
        st.markdown("### Batch Prediction via CSV")

        if not prediction_ready:
            st.warning("Batch prediction is currently unavailable.")
            st.info("Please create `deployment_package.pkl` first if you want to use prediction features.")
        else:
            st.write("Upload a CSV file containing applicant information for batch scoring.")

            st.write("#### Required Training Feature Columns")
            st.dataframe(pd.DataFrame({"feature_columns": feature_columns}), use_container_width=True)

            uploaded_file = st.file_uploader(
                "Upload CSV File",
                type=["csv"],
                key="batch_upload"
            )

            if uploaded_file is None:
                st.info("No CSV file has been uploaded.")
            else:
                try:
                    batch_df = pd.read_csv(uploaded_file)
                    batch_df.columns = batch_df.columns.str.strip()

                    st.write("#### Uploaded Data Preview")
                    st.dataframe(batch_df.head(), use_container_width=True)

                    pred_input = prepare_prediction_input(batch_df, feature_columns)

                    if pred_input is None:
                        st.error("Batch prediction input could not be prepared.")
                    else:
                        if scaler is not None:
                            pred_input_transformed = scaler.transform(pred_input)
                        else:
                            pred_input_transformed = pred_input

                        batch_pred = model.predict(pred_input_transformed)

                        batch_result = batch_df.copy()
                        batch_result["prediction"] = [normalize_prediction_label(p) for p in batch_pred]

                        if hasattr(model, "predict_proba"):
                            batch_proba = model.predict_proba(pred_input_transformed)
                            if batch_proba.shape[1] >= 2:
                                batch_result["rejected_probability"] = np.round(batch_proba[:, 0] * 100, 2)
                                batch_result["approved_probability"] = np.round(batch_proba[:, 1] * 100, 2)

                        st.write("#### Batch Prediction Results")
                        st.dataframe(batch_result, use_container_width=True)

                        st.download_button(
                            "Download Prediction Results CSV",
                            data=to_csv_download(batch_result),
                            file_name="batch_prediction_results.csv",
                            mime="text/csv"
                        )

                except Exception as e:
                    st.error(f"Batch prediction failed: {e}")

    # =====================================================
    # Subtab 3 - Prediction History
    # =====================================================
    with subtab3:
        st.markdown("### Prediction History")

        if len(st.session_state.prediction_history) == 0:
            st.info("No prediction history is currently available.")
        else:
            history_df = pd.DataFrame(st.session_state.prediction_history)
            st.dataframe(history_df, use_container_width=True)

            st.download_button(
                "Export Prediction History",
                data=to_csv_download(history_df),
                file_name="prediction_history.csv",
                mime="text/csv"
            )

            if st.button("Clear Prediction History", use_container_width=True):
                st.session_state.prediction_history = []
                st.success("Prediction history cleared.")
                st.rerun()
# =========================================================
# Tab 3 - Risk Management Guidelines
# =========================================================
with tab3:
    st.markdown("## Risk Management Guidelines")
    st.caption("Provide practical decision-support guidance based on model outcomes and risk awareness principles.")

    st.info("These guidelines are for academic demonstration and operational reference only. Final lending decisions should always include human review, policy checks, and compliance procedures.")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Recommended Actions by Prediction Outcome")

        st.success("""
        **If Estimated Outcome = Approved**
        - Continue with document verification
        - Validate declared income and asset values
        - Confirm identity and credit profile consistency
        - Review affordability relative to loan amount and term
        - Apply standard compliance and underwriting checks
        """)

        st.error("""
        **If Estimated Outcome = Rejected**
        - Reassess applicant credit profile
        - Check for low credit score or insufficient asset support
        - Review debt burden and income adequacy
        - Request corrected or additional documentation if needed
        - Escalate marginal cases for manual review
        """)

    with col2:
        st.markdown("### Risk Review Checklist")

        risk_check_1 = st.checkbox("Identity and KYC documents verified")
        risk_check_2 = st.checkbox("Income source verified")
        risk_check_3 = st.checkbox("Asset declarations verified")
        risk_check_4 = st.checkbox("Credit score reviewed")
        risk_check_5 = st.checkbox("Loan affordability reviewed")
        risk_check_6 = st.checkbox("Manual review completed (if needed)")

        checked_count = sum([
            risk_check_1, risk_check_2, risk_check_3,
            risk_check_4, risk_check_5, risk_check_6
        ])

        st.progress(checked_count / 6)
        st.write(f"Checklist completion: **{checked_count}/6**")

    st.markdown("### Risk Categories and Handling Guidance")

    risk_df = pd.DataFrame({
        "Risk Level": ["Low", "Medium", "High"],
        "Typical Signals": [
            "Strong credit score, stable income, adequate assets",
            "Mixed indicators, some affordability or asset concerns",
            "Low credit score, weak income support, insufficient assets"
        ],
        "Suggested Handling": [
            "Proceed with standard verification",
            "Manual review and request supporting documents",
            "Escalate, reassess, or decline based on policy"
        ]
    })
    st.dataframe(risk_df, use_container_width=True)

    st.markdown("### Compliance Awareness")
    st.warning(
        "Real-world lending workflows should consider fairness, responsible lending principles, internal credit policy, "
        "anti-fraud checks, and applicable financial compliance requirements."
    )

    with st.expander("View operational guidance notes"):
        st.write("""
        - Predictions should support, not replace, professional judgement.
        - High-confidence approvals still require verification.
        - Borderline cases should be routed to a manual review stage.
        - Model output should be interpreted alongside business policy.
        """)

# =========================================================
# Tab 4 - Analytics & Visualization
# =========================================================
with tab4:
    st.markdown("## Analytics & Visualization")
    st.caption("Visual analysis is generated only from the currently loaded real dataset.")

    # -----------------------------------------------------
    # Dataset availability check
    # -----------------------------------------------------
    if df is None or df.empty:
        st.error("Dataset is unavailable or empty. Visualization cannot be generated.")
    else:
        df = df.copy()
        df.columns = df.columns.str.strip()

        target_col = find_target_column(df)
        numeric_df = df.select_dtypes(include=np.number)

        # -------------------------------------------------
        # Feature importance preparation
        # -------------------------------------------------
        feature_importance_df = None

        if model is not None and feature_columns is not None:
            try:
                if hasattr(model, "feature_importances_"):
                    feature_importance_df = pd.DataFrame({
                        "Feature": feature_columns,
                        "Importance": model.feature_importances_
                    })

                elif hasattr(model, "coef_"):
                    coef_values = model.coef_[0] if len(model.coef_.shape) > 1 else model.coef_
                    feature_importance_df = pd.DataFrame({
                        "Feature": feature_columns,
                        "Importance": np.abs(coef_values)
                    })

                if feature_importance_df is not None:
                    feature_importance_df = feature_importance_df.sort_values(
                        by="Importance",
                        ascending=False
                    )

            except Exception as e:
                st.warning(f"Feature importance could not be generated: {e}")
                feature_importance_df = None

        # -------------------------------------------------
        # Two-column visualization area
        # -------------------------------------------------
        c1, c2 = st.columns(2)

        with c1:
            if target_col and target_col in df.columns:
                st.markdown("### Loan Outcome Distribution")
                fig, ax = plt.subplots(figsize=(7, 4))
                sns.countplot(data=df, x=target_col, palette=["#a8d0ff", "#2d77dd"], ax=ax)
                ax.set_title("Distribution of Loan Outcomes", fontweight="bold")
                plt.tight_layout()
                st.pyplot(fig)
            else:
                st.info("Target column is not available, so loan outcome distribution cannot be displayed.")

            if "loan_amount" in df.columns:
                st.markdown("### Loan Amount Distribution")
                fig, ax = plt.subplots(figsize=(7, 4))
                sns.histplot(df["loan_amount"].dropna(), kde=True, color="#1c63c7", ax=ax)
                ax.set_title("Distribution of Loan Amount", fontweight="bold")
                plt.tight_layout()
                st.pyplot(fig)
            else:
                st.info("Column 'loan_amount' is not available in the dataset.")

        with c2:
            if "income_annum" in df.columns:
                st.markdown("### Annual Income Distribution")
                fig, ax = plt.subplots(figsize=(7, 4))
                sns.histplot(df["income_annum"].dropna(), kde=True, color="#2d77dd", ax=ax)
                ax.set_title("Distribution of Annual Income", fontweight="bold")
                plt.tight_layout()
                st.pyplot(fig)
            else:
                st.info("Column 'income_annum' is not available in the dataset.")

            if target_col and target_col in df.columns and "cibil_score" in df.columns:
                st.markdown("### CIBIL Score by Loan Outcome")
                fig, ax = plt.subplots(figsize=(7, 4))
                sns.boxplot(data=df, x=target_col, y="cibil_score", palette=["#a8d0ff", "#2d77dd"], ax=ax)
                ax.set_title("CIBIL Score by Loan Outcome", fontweight="bold")
                plt.tight_layout()
                st.pyplot(fig)
            else:
                st.info("Target column or 'cibil_score' is not available for comparative analysis.")

        # -------------------------------------------------
        # Correlation heatmap
        # -------------------------------------------------
        if numeric_df.shape[1] > 1:
            st.markdown("### Correlation Heatmap")
            fig, ax = plt.subplots(figsize=(11, 6))
            corr = numeric_df.corr()
            sns.heatmap(corr, cmap="Blues", annot=True, fmt=".2f", linewidths=0.5, ax=ax)
            ax.set_title("Correlation Between Numeric Features", fontweight="bold")
            plt.tight_layout()
            st.pyplot(fig)
        else:
            st.info("At least two numeric columns are required to generate a correlation heatmap.")

        # -------------------------------------------------
        # Feature importance
        # -------------------------------------------------
        st.markdown("### Feature Importance")
        if feature_importance_df is not None and not feature_importance_df.empty:
            top_features = feature_importance_df.head(10)

            fig, ax = plt.subplots(figsize=(8, 5))
            sns.barplot(
                data=top_features,
                y="Feature",
                x="Importance",
                palette="Blues_r",
                ax=ax
            )
            ax.set_title("Top Feature Importance", fontweight="bold")
            plt.tight_layout()
            st.pyplot(fig)

            st.dataframe(feature_importance_df, use_container_width=True)
        else:
            st.info("Feature importance is not available for the current model.")

        # -------------------------------------------------
        # Time trend analysis
        # -------------------------------------------------
        st.markdown("### Time Trend Analysis")
        date_col = find_date_column(df)

        if date_col:
            try:
                trend_df = df.copy()
                trend_df[date_col] = pd.to_datetime(trend_df[date_col], errors="coerce")
                trend_df = trend_df.dropna(subset=[date_col])

                if not trend_df.empty:
                    trend_df["year_month"] = trend_df[date_col].dt.to_period("M").astype(str)
                    monthly_counts = trend_df.groupby("year_month").size().reset_index(name="applications")

                    fig, ax = plt.subplots(figsize=(10, 4))
                    sns.lineplot(
                        data=monthly_counts,
                        x="year_month",
                        y="applications",
                        marker="o",
                        color="#2d77dd",
                        ax=ax
                    )
                    ax.set_title("Monthly Application Trend", fontweight="bold")
                    ax.set_xlabel("Year-Month")
                    ax.set_ylabel("Applications")
                    plt.xticks(rotation=45)
                    plt.tight_layout()
                    st.pyplot(fig)

                    st.dataframe(monthly_counts, use_container_width=True)
                else:
                    st.info("No valid datetime values are available for trend analysis.")

            except Exception as e:
                st.warning(f"Time trend analysis could not be generated: {e}")
        else:
            st.info("No date column was detected for time trend analysis.")

# =========================================================
# Tab 5 - Dataset Insights
# =========================================================
with tab5:
    st.markdown("## Dataset Insights")
    st.caption("Explore the real structure, quality, and distribution of the currently loaded dataset.")

    # -----------------------------
    # Dataset availability check
    # -----------------------------
    if df is None or df.empty:
        st.error("Dataset is unavailable or empty. Please check whether the CSV file was loaded correctly.")
    else:
        rows = df.shape[0]
        cols = df.shape[1]
        target_col = find_target_column(df)
        target_text = target_col if target_col else "Not Found"

        # -----------------------------
        # Basic dataset summary
        # -----------------------------
        st.markdown("### Dataset Summary")

        a1, a2, a3 = st.columns(3)
        with a1:
            metric_box("Rows", rows)
        with a2:
            metric_box("Columns", cols)
        with a3:
            metric_box("Target Column", target_text)

        # -----------------------------
        # Data quality score
        # -----------------------------
        st.markdown("### Data Quality Score")

        score, quality_details = data_quality_score(df)

        q1, q2, q3, q4 = st.columns(4)
        with q1:
            metric_box("Quality Score", f"{score}/100")
        with q2:
            metric_box("Missing %", f"{quality_details.get('missing_ratio', 0)}%")
        with q3:
            metric_box("Duplicate %", f"{quality_details.get('duplicate_ratio', 0)}%")
        with q4:
            metric_box("Outlier %", f"{quality_details.get('outlier_ratio', 0)}%")

        with st.expander("How is the quality score calculated?"):
            st.write("""
            The score is calculated from the currently loaded dataset only.
            It is based on:
            - Missing value ratio
            - Duplicate row ratio
            - Numeric outlier ratio estimated with the IQR rule
            """)
            st.write("This is a simple dashboard-level quality indicator, not a formal data governance metric.")

        # -----------------------------
        # Dataset filter
        # -----------------------------
        st.markdown("### Dataset Filter")

        filtered_df = df.copy()
        categorical_cols = filtered_df.select_dtypes(exclude=np.number).columns.tolist()

        if categorical_cols:
            filter_col = st.selectbox(
                "Choose a categorical column to filter",
                ["None"] + categorical_cols
            )

            if filter_col != "None":
                options = filtered_df[filter_col].dropna().unique().tolist()
                options = sorted(options)

                selected_values = st.multiselect(
                    "Select values",
                    options,
                    default=options[:3] if len(options) >= 3 else options
                )

                if selected_values:
                    filtered_df = filtered_df[filtered_df[filter_col].isin(selected_values)]
        else:
            st.info("No categorical columns are available for filtering in the current dataset.")

        # -----------------------------
        # Filtered dataset preview
        # -----------------------------
        st.markdown("### Dataset Preview")
        st.write(f"Filtered dataset rows: **{filtered_df.shape[0]}**, columns: **{filtered_df.shape[1]}**")
        st.dataframe(filtered_df.head(), use_container_width=True)

        # -----------------------------
        # Schema and missing values
        # -----------------------------
        st.markdown("### Schema & Missing Values")

        info_df = pd.DataFrame({
            "Column": filtered_df.columns,
            "Data Type": [str(dtype) for dtype in filtered_df.dtypes],
            "Missing Values": [filtered_df[col].isnull().sum() for col in filtered_df.columns],
            "Missing %": [
                round((filtered_df[col].isnull().sum() / len(filtered_df)) * 100, 2) if len(filtered_df) > 0 else 0
                for col in filtered_df.columns
            ],
            "Unique Values": [filtered_df[col].nunique(dropna=True) for col in filtered_df.columns]
        })

        st.dataframe(info_df, use_container_width=True)

        # -----------------------------
        # Descriptive statistics
        # -----------------------------
        st.markdown("### Descriptive Statistics")

        try:
            desc_df = filtered_df.describe(include="all").transpose()
            st.dataframe(desc_df, use_container_width=True)
        except Exception as e:
            st.warning(f"Descriptive statistics could not be generated: {e}")

        # -----------------------------
        # Numeric columns summary
        # -----------------------------
        numeric_cols = filtered_df.select_dtypes(include=np.number).columns.tolist()

        st.markdown("### Numeric Feature Summary")
        if numeric_cols:
            numeric_summary = pd.DataFrame({
                "Feature": numeric_cols,
                "Min": [filtered_df[col].min() for col in numeric_cols],
                "Max": [filtered_df[col].max() for col in numeric_cols],
                "Mean": [round(filtered_df[col].mean(), 2) for col in numeric_cols],
                "Median": [round(filtered_df[col].median(), 2) for col in numeric_cols],
                "Std": [round(filtered_df[col].std(), 2) if pd.notnull(filtered_df[col].std()) else 0 for col in numeric_cols]
            })
            st.dataframe(numeric_summary, use_container_width=True)
        else:
            st.info("No numeric columns are available in the filtered dataset.")

        # -----------------------------
        # Target variable distribution
        # -----------------------------
        if target_col and target_col in filtered_df.columns:
            st.markdown("### Target Variable Distribution")

            target_counts = filtered_df[target_col].value_counts(dropna=False)
            target_counts_df = target_counts.reset_index()
            target_counts_df.columns = [target_col, "Count"]
            target_counts_df["Percentage %"] = round((target_counts_df["Count"] / target_counts_df["Count"].sum()) * 100, 2)

            st.dataframe(target_counts_df, use_container_width=True)

            if len(target_counts) >= 2:
                imbalance_ratio = round(target_counts.max() / max(target_counts.min(), 1), 2)

                if imbalance_ratio > 1.5:
                    st.warning(f"Potential class imbalance detected. Imbalance ratio: {imbalance_ratio}")
                else:
                    st.success(f"Class balance looks acceptable. Imbalance ratio: {imbalance_ratio}")
            else:
                st.info("The target variable contains fewer than two observable classes in the filtered dataset.")
        else:
            st.info("Target column is not available in the filtered dataset.")

        # -----------------------------
        # Optional raw data download
        # -----------------------------
        st.markdown("### Export Filtered Data")
        st.download_button(
            label="Download Filtered Dataset CSV",
            data=filtered_df.to_csv(index=False).encode("utf-8"),
            file_name="filtered_dataset.csv",
            mime="text/csv"
        )

# =========================================================
# Tab 6 - User Feedback & Support
# =========================================================
with tab6:
    st.markdown("## User Feedback & Support")
    st.caption("Collect user feedback and provide basic support access points for continuous improvement.")

    left_col, right_col = st.columns([1.1, 0.9])

    # -----------------------------------------------------
    # Left column - Submit feedback
    # -----------------------------------------------------
    with left_col:
        st.markdown("### Submit Feedback")

        feedback_name = st.text_input("Your Name")
        feedback_role = st.selectbox(
            "Role",
            ["Student", "Instructor", "Analyst", "Reviewer", "Other"]
        )
        feedback_type = st.selectbox(
            "Feedback Type",
            ["Bug Report", "Feature Suggestion", "Usability Feedback", "Model Feedback", "General Comment"]
        )
        feedback_score = st.slider("Satisfaction Score", 1, 5, 4)
        feedback_text = st.text_area("Your Feedback", height=160)

        if st.button("Submit Feedback", use_container_width=True):
            if feedback_text.strip() == "":
                st.warning("Please enter your feedback before submitting.")
            else:
                feedback_record = pd.DataFrame([{
                    "name": feedback_name,
                    "role": feedback_role,
                    "feedback_type": feedback_type,
                    "satisfaction_score": feedback_score,
                    "feedback_text": feedback_text
                }])

                feedback_file = "user_feedback.csv"

                if os.path.exists(feedback_file):
                    feedback_record.to_csv(feedback_file, mode="a", header=False, index=False)
                else:
                    feedback_record.to_csv(feedback_file, index=False)

                st.success("Thank you. Your feedback has been recorded.")
                st.rerun()

    # -----------------------------------------------------
    # Right column - Support info
    # -----------------------------------------------------
    with right_col:
        st.markdown("### Support Information")
        st.info("""
**Support Scope**
- Dashboard usage questions
- Dataset understanding
- Prediction workflow clarification
- Visual analytics interpretation
""")

        st.markdown("### Help Resources")
        st.write("- User guide: coming soon")
        st.write("- FAQ page: recommended for next version")
        st.write("- Model documentation: available in project report")

        st.markdown("### Contact")
        st.write("**Support Email:** 3509937197@qq.com")
        st.write("**Response Mode:** Academic demonstration only")
        st.write("**Availability:** Manual review / offline support")

    # -----------------------------------------------------
    # Recent feedback records
    # -----------------------------------------------------
    st.markdown("### Recent Feedback Records")
    feedback_file = "user_feedback.csv"

    if os.path.exists(feedback_file):
        try:
            feedback_df = pd.read_csv(feedback_file)

            if feedback_df.empty:
                st.caption("No feedback records found yet.")
            else:
                # 重置索引，方便删除
                feedback_df = feedback_df.reset_index(drop=True)
                feedback_df.insert(0, "record_id", feedback_df.index)

                st.dataframe(feedback_df.tail(10), use_container_width=True)

                # 下载按钮
                csv_bytes = feedback_df.drop(columns=["record_id"]).to_csv(index=False).encode("utf-8")
                st.download_button(
                    label="Download Feedback Records",
                    data=csv_bytes,
                    file_name="user_feedback_export.csv",
                    mime="text/csv"
                )

                # -------------------------------------------------
                # Delete single record
                # -------------------------------------------------
                st.markdown("### Delete a Feedback Record")

                selected_record_id = st.selectbox(
                    "Select record ID to delete",
                    feedback_df["record_id"].tolist()
                )

                confirm_delete = st.checkbox("I confirm I want to delete the selected feedback record")

                if confirm_delete and st.button("Delete Selected Record", use_container_width=True):
                    updated_df = feedback_df[feedback_df["record_id"] != selected_record_id].drop(columns=["record_id"])
                    updated_df.to_csv(feedback_file, index=False)
                    st.success(f"Feedback record {selected_record_id} deleted successfully.")
                    st.rerun()

                # -------------------------------------------------
                # Clear all records
                # -------------------------------------------------
                st.markdown("### Danger Zone")

                confirm_clear = st.checkbox("I confirm I want to delete ALL feedback records")

                if confirm_clear and st.button("Clear All Feedback Records", use_container_width=True):
                    empty_df = pd.DataFrame(columns=feedback_df.drop(columns=["record_id"]).columns)
                    empty_df.to_csv(feedback_file, index=False)
                    st.success("All feedback records have been deleted.")
                    st.rerun()

        except Exception as e:
            st.warning(f"Unable to read feedback records: {e}")
    else:
        st.caption("No feedback records found yet.")
