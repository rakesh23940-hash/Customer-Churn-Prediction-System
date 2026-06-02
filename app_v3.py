import streamlit as st
import pandas as pd
import joblib

# ==========================
# PAGE CONFIG
# ==========================

st.set_page_config(
    page_title="AI Customer Churn Intelligence",
    page_icon="🤖",
    layout="wide"
)

# ==========================
# SESSION STATE
# ==========================

if "step" not in st.session_state:
    st.session_state.step = 0

# ==========================
# CUSTOM CSS
# ==========================

st.markdown("""
<style>

.stApp{
    background: linear-gradient(
        135deg,
        #0f172a,
        #111827,
        #1e293b
    );
}

.big-title{
    text-align:center;
    color:#38bdf8;
    font-size:52px;
    font-weight:bold;
}

.sub-title{
    text-align:center;
    color:#cbd5e1;
    font-size:18px;
}

div[data-testid="metric-container"] {
    background-color: #1e293b;
    border: 1px solid #334155;
    padding: 15px;
    border-radius: 12px;
}

</style>
""", unsafe_allow_html=True)

# ==========================
# LOAD MODEL
# ==========================

model = joblib.load("models/churn_model.pkl")
scaler = joblib.load("models/scaler.pkl")

# ==========================
# LANDING PAGE
# ==========================

if st.session_state.step == 0:

    st.markdown("""
    <div class="big-title">
    🤖 AI Customer Churn Intelligence
    </div>

    <div class="sub-title">
    Predict • Analyze • Retain Customers
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    st.info("""
    This AI system predicts customer churn
    using Machine Learning.
    """)

    st.write("")

    if st.button("🚀 Start Analysis"):

        st.session_state.step = 1
        st.rerun()

# ==========================
# STEP 1
# ==========================

elif st.session_state.step == 1:

    st.header("👤 Step 1 : Customer Profile")

    gender = st.selectbox(
        "Gender",
        [
            "Female",
            "Male"
        ]
    )

    senior = st.selectbox(
        "Senior Citizen",
        [
            "No",
            "Yes"
        ]
    )

    partner = st.selectbox(
        "Partner",
        [
            "No",
            "Yes"
        ]
    )

    dependents = st.selectbox(
        "Dependents",
        [
            "No",
            "Yes"
        ]
    )

    st.write("")

    if st.button("➡ Next"):

        st.session_state.gender = gender
        st.session_state.senior = senior
        st.session_state.partner = partner
        st.session_state.dependents = dependents

        st.session_state.step = 2
        st.rerun()
# ==========================
# STEP 2
# ==========================

elif st.session_state.step == 2:

    st.header("📡 Step 2 : Service Details")

    phone_service = st.selectbox(
        "Phone Service",
        [
            "No",
            "Yes"
        ]
    )

    multiple_lines = st.selectbox(
        "Multiple Lines",
        [
            "No",
            "Yes",
            "No phone service"
        ]
    )

    internet_service = st.selectbox(
        "Internet Service",
        [
            "DSL",
            "Fiber optic",
            "No"
        ]
    )

    online_security = st.selectbox(
        "Online Security",
        [
            "No",
            "Yes",
            "No internet service"
        ]
    )

    online_backup = st.selectbox(
        "Online Backup",
        [
            "No",
            "Yes",
            "No internet service"
        ]
    )

    device_protection = st.selectbox(
        "Device Protection",
        [
            "No",
            "Yes",
            "No internet service"
        ]
    )

    tech_support = st.selectbox(
        "Tech Support",
        [
            "No",
            "Yes",
            "No internet service"
        ]
    )

    streaming_tv = st.selectbox(
        "Streaming TV",
        [
            "No",
            "Yes",
            "No internet service"
        ]
    )

    streaming_movies = st.selectbox(
        "Streaming Movies",
        [
            "No",
            "Yes",
            "No internet service"
        ]
    )

    col1, col2 = st.columns(2)

    with col1:

        if st.button("⬅ Back"):

            st.session_state.step = 1
            st.rerun()

    with col2:

        if st.button("➡ Next"):

            st.session_state.phone_service = phone_service

            st.session_state.multiple_lines = multiple_lines

            st.session_state.internet_service = internet_service

            st.session_state.online_security = online_security

            st.session_state.online_backup = online_backup

            st.session_state.device_protection = device_protection

            st.session_state.tech_support = tech_support

            st.session_state.streaming_tv = streaming_tv

            st.session_state.streaming_movies = streaming_movies

            st.session_state.step = 3

            st.rerun()
# ==========================
# STEP 3
# ==========================

elif st.session_state.step == 3:

    st.header("💳 Step 3 : Billing Details")

    tenure = st.number_input(
        "Tenure (Months)",
        min_value=0,
        max_value=100,
        value=12
    )

    monthly_charges = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        max_value=200.0,
        value=70.0
    )

    total_charges = st.number_input(
        "Total Charges",
        min_value=0.0,
        max_value=10000.0,
        value=1000.0
    )

    contract = st.selectbox(
        "Contract",
        [
            "Month-to-month",
            "One year",
            "Two year"
        ]
    )

    paperless_billing = st.selectbox(
        "Paperless Billing",
        [
            "No",
            "Yes"
        ]
    )

    payment_method = st.selectbox(
        "Payment Method",
        [
            "Bank transfer (automatic)",
            "Credit card (automatic)",
            "Electronic check",
            "Mailed check"
        ]
    )

    col1, col2 = st.columns(2)

    with col1:

        if st.button("⬅ Back"):

            st.session_state.step = 2
            st.rerun()

    with col2:

        if st.button("🚀 Analyze Customer"):

            st.session_state.tenure = tenure
            st.session_state.monthly_charges = monthly_charges
            st.session_state.total_charges = total_charges

            st.session_state.contract = contract
            st.session_state.paperless_billing = paperless_billing
            st.session_state.payment_method = payment_method

            st.session_state.step = 4
            st.rerun()
# ==========================
# STEP 4
# ==========================

elif st.session_state.step == 4:

    st.markdown(
    """
    <h1 style='text-align:center'>
    🤖 AI Analysis Dashboard
    </h1>
    """,
    unsafe_allow_html=True
)

    columns = [
        'SeniorCitizen',
        'tenure',
        'MonthlyCharges',
        'TotalCharges',
        'gender_Male',
        'Partner_Yes',
        'Dependents_Yes',
        'PhoneService_Yes',
        'MultipleLines_No phone service',
        'MultipleLines_Yes',
        'InternetService_Fiber optic',
        'InternetService_No',
        'OnlineSecurity_No internet service',
        'OnlineSecurity_Yes',
        'OnlineBackup_No internet service',
        'OnlineBackup_Yes',
        'DeviceProtection_No internet service',
        'DeviceProtection_Yes',
        'TechSupport_No internet service',
        'TechSupport_Yes',
        'StreamingTV_No internet service',
        'StreamingTV_Yes',
        'StreamingMovies_No internet service',
        'StreamingMovies_Yes',
        'Contract_One year',
        'Contract_Two year',
        'PaperlessBilling_Yes',
        'PaymentMethod_Credit card (automatic)',
        'PaymentMethod_Electronic check',
        'PaymentMethod_Mailed check'
    ]

    input_data = {col: 0 for col in columns}

    # =====================
    # BASIC
    # =====================

    input_data["SeniorCitizen"] = (
        1 if st.session_state.senior == "Yes" else 0
    )

    input_data["tenure"] = st.session_state.tenure
    input_data["MonthlyCharges"] = st.session_state.monthly_charges
    input_data["TotalCharges"] = st.session_state.total_charges

    # =====================
    # CUSTOMER
    # =====================

    if st.session_state.gender == "Male":
        input_data["gender_Male"] = 1

    if st.session_state.partner == "Yes":
        input_data["Partner_Yes"] = 1

    if st.session_state.dependents == "Yes":
        input_data["Dependents_Yes"] = 1

    # =====================
    # PHONE
    # =====================

    if st.session_state.phone_service == "Yes":
        input_data["PhoneService_Yes"] = 1

    if st.session_state.multiple_lines == "Yes":
        input_data["MultipleLines_Yes"] = 1

    if st.session_state.multiple_lines == "No phone service":
        input_data["MultipleLines_No phone service"] = 1

    # =====================
    # INTERNET
    # =====================

    if st.session_state.internet_service == "Fiber optic":
        input_data["InternetService_Fiber optic"] = 1

    elif st.session_state.internet_service == "No":
        input_data["InternetService_No"] = 1

    # =====================
    # ONLINE SECURITY
    # =====================

    if st.session_state.online_security == "Yes":
        input_data["OnlineSecurity_Yes"] = 1

    elif st.session_state.online_security == "No internet service":
        input_data["OnlineSecurity_No internet service"] = 1

    # =====================
    # ONLINE BACKUP
    # =====================

    if st.session_state.online_backup == "Yes":
        input_data["OnlineBackup_Yes"] = 1

    elif st.session_state.online_backup == "No internet service":
        input_data["OnlineBackup_No internet service"] = 1

    # =====================
    # DEVICE PROTECTION
    # =====================

    if st.session_state.device_protection == "Yes":
        input_data["DeviceProtection_Yes"] = 1

    elif st.session_state.device_protection == "No internet service":
        input_data["DeviceProtection_No internet service"] = 1

    # =====================
    # TECH SUPPORT
    # =====================

    if st.session_state.tech_support == "Yes":
        input_data["TechSupport_Yes"] = 1

    elif st.session_state.tech_support == "No internet service":
        input_data["TechSupport_No internet service"] = 1

    # =====================
    # STREAMING TV
    # =====================

    if st.session_state.streaming_tv == "Yes":
        input_data["StreamingTV_Yes"] = 1

    elif st.session_state.streaming_tv == "No internet service":
        input_data["StreamingTV_No internet service"] = 1

    # =====================
    # STREAMING MOVIES
    # =====================

    if st.session_state.streaming_movies == "Yes":
        input_data["StreamingMovies_Yes"] = 1

    elif st.session_state.streaming_movies == "No internet service":
        input_data["StreamingMovies_No internet service"] = 1

    # =====================
    # CONTRACT
    # =====================

    if st.session_state.contract == "One year":
        input_data["Contract_One year"] = 1

    elif st.session_state.contract == "Two year":
        input_data["Contract_Two year"] = 1

    # =====================
    # PAPERLESS
    # =====================

    if st.session_state.paperless_billing == "Yes":
        input_data["PaperlessBilling_Yes"] = 1

    # =====================
    # PAYMENT
    # =====================

    if st.session_state.payment_method == "Credit card (automatic)":
        input_data["PaymentMethod_Credit card (automatic)"] = 1

    elif st.session_state.payment_method == "Electronic check":
        input_data["PaymentMethod_Electronic check"] = 1

    elif st.session_state.payment_method == "Mailed check":
        input_data["PaymentMethod_Mailed check"] = 1

    # =====================
    # MODEL
    # =====================

    input_df = pd.DataFrame([input_data])

    input_scaled = scaler.transform(input_df)

    probability = model.predict_proba(
        input_scaled
    )[0][1]

    # =====================
    # DASHBOARD
    # =====================

    st.markdown(
        f"""
        <h1 style='text-align:center;
        color:#38bdf8;
        font-size:70px;'>
        {probability*100:.2f}%
        </h1>
        """,
        unsafe_allow_html=True
    )

    st.subheader("📊 Dashboard")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Churn Probability",
            f"{probability*100:.2f}%"
        )

    with col2:
        st.metric(
            "Tenure",
            st.session_state.tenure
        )

    with col3:
        st.metric(
            "Monthly Charges",
            f"${st.session_state.monthly_charges}"
        )

    st.progress(
        int(probability * 100)
    )

    if probability > 0.80:

        st.error("🔴 High Risk Customer")

    elif probability > 0.60:

        st.warning("🟡 Medium Risk Customer")

    else:

        st.success("🟢 Low Risk Customer")

    # =====================
    # CUSTOMER SUMMARY
    # =====================

    st.subheader("👤 Customer Summary")

    col1_sum, col2_sum = st.columns(2)

    with col1_sum:
        st.write(
            f"**Gender:** {st.session_state.gender}"
        )
        st.write(
            f"**Partner:** {st.session_state.partner}"
        )
        st.write(
            f"**Dependents:** {st.session_state.dependents}"
        )

    with col2_sum:
        st.write(
            f"**Contract:** {st.session_state.contract}"
        )
        st.write(
            f"**Internet:** {st.session_state.internet_service}"
        )
        st.write(
            f"**Payment:** {st.session_state.payment_method}"
        )

    # =====================
    # RECOMMENDATIONS
    # =====================

    st.subheader("💡 Recommendations")

    if probability > 0.80:

        st.write("✅ Offer Discount")
        st.write("✅ Assign Retention Executive")

    elif probability > 0.60:

        st.write("✅ Offer Annual Plan")

    else:

        st.success(
    "✅ Continue Regular Engagement"
)

    # =====================
    # BUSINESS INSIGHT
    # =====================

    st.subheader("📊 Business Insight")

    if probability > 0.80:

        st.error("""
    Customer is highly likely to churn.

    Immediate retention strategy required.
    """)

    elif probability > 0.60:

        st.warning("""
    Customer shows moderate churn risk.

    Monitor engagement closely.
    """)

    else:

        st.success("""
    Customer appears stable and loyal.

    Continue regular engagement.
    """)

    # =====================
    # REPORT
    # =====================

    report = f"""
Customer Churn Report

Probability: {probability*100:.2f}%

Gender: {st.session_state.gender}
Contract: {st.session_state.contract}

Risk Analysis Completed
"""

    st.download_button(
        "📄 Download Report",
        report,
        "customer_report.txt"
    )

    # =====================
    # RESET
    # =====================

    if st.button("🔄 Start New Analysis"):

        st.session_state.step = 0
        st.rerun()