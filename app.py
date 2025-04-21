import streamlit as st
import pandas as pd
import joblib

# Load model dan encoder
model = joblib.load("model_attrition.pkl")
label_encoders = joblib.load("label_encoders.pkl")

st.title("🚀 Attrition Prediction App")

# Input form
with st.form("input_form"):
    employee_data = {}

    employee_data["age"] = st.slider("Age", 18, 60, 30)
    employee_data["business_travel"] = st.selectbox("Business Travel", ["Travel_Frequently", "Travel_Rarely", "Non-Travel"])
    employee_data["daily_rate"] = st.number_input("Daily Rate", 100, 1500, 800)
    employee_data["department"] = st.selectbox("Department", ["Human Resources", "Research & Development", "Sales"])
    employee_data["distance_from_home"] = st.slider("Distance From Home", 1, 30, 10)
    employee_data["education"] = st.slider("Education", 1, 5, 3)
    employee_data["education_field"] = st.selectbox("Education Field", ["Life Sciences", "Other", "Medical", "Marketing", "Technical Degree", "Human Resources"])
    employee_data["employee_count"] = 1  # default
    employee_data["environment_satisfaction"] = st.slider("Environment Satisfaction", 1, 4, 3)
    employee_data["gender"] = st.selectbox("Gender", ["Male", "Female"])
    employee_data["hourly_rate"] = st.slider("Hourly Rate", 30, 100, 60)
    employee_data["job_involvement"] = st.slider("Job Involvement", 1, 4, 3)
    employee_data["job_level"] = st.slider("Job Level", 1, 5, 2)
    employee_data["job_role"] = st.selectbox("Job Role", ["Sales Executive", "Research Scientist", "Laboratory Technician", "Manufacturing Director", "Healthcare Representative", "Manager", "Sales Representative", "Research Director", "Human Resources"])
    employee_data["job_satisfaction"] = st.slider("Job Satisfaction", 1, 4, 3)
    employee_data["marital_status"] = st.selectbox("Marital Status", ["Single", "Married", "Divorced"])
    employee_data["monthly_income"] = st.number_input("Monthly Income", 1000, 20000, 5000)
    employee_data["monthly_rate"] = st.number_input("Monthly Rate", 1000, 30000, 10000)
    employee_data["num_companies_worked"] = st.slider("Num Companies Worked", 0, 10, 2)
    employee_data["over18"] = 1  # default (Y)
    employee_data["over_time"] = st.selectbox("Over Time", ["Yes", "No"])
    employee_data["percent_salary_hike"] = st.slider("Percent Salary Hike", 10, 25, 15)
    employee_data["performance_rating"] = st.slider("Performance Rating", 1, 4, 3)
    employee_data["relationship_satisfaction"] = st.slider("Relationship Satisfaction", 1, 4, 2)
    employee_data["standard_hours"] = 80  # default
    employee_data["stock_option_level"] = st.slider("Stock Option Level", 0, 3, 1)
    employee_data["total_working_years"] = st.slider("Total Working Years", 0, 40, 10)
    employee_data["training_times_last_year"] = st.slider("Training Times Last Year", 0, 6, 3)
    employee_data["work_life_balance"] = st.slider("Work Life Balance", 1, 4, 3)
    employee_data["years_at_company"] = st.slider("Years at Company", 0, 40, 5)
    employee_data["years_in_current_role"] = st.slider("Years in Current Role", 0, 20, 3)
    employee_data["years_since_last_promotion"] = st.slider("Years Since Last Promotion", 0, 15, 2)
    employee_data["years_with_curr_manager"] = st.slider("Years with Current Manager", 0, 20, 4)

    submitted = st.form_submit_button("Predict Attrition")

# Predict
if submitted:
    input_df = pd.DataFrame([employee_data])
    
    # Apply label encoding
    for col, le in label_encoders.items():
        if col in input_df:
            input_df[col] = le.transform(input_df[col])

    prediction = model.predict(input_df)[0]
    prob = model.predict_proba(input_df)[0][1]

    if prediction == 1:
        st.error(f"❌ Karyawan berisiko resign (probabilitas: {prob:.2f})")
    else:
        st.success(f"✅ Karyawan diprediksi akan bertahan (probabilitas keluar: {prob:.2f})")
