import streamlit as st
import pandas as pd
import joblib

# Load model, encoders, dan urutan kolom
model = joblib.load("model_attrition.pkl")
encoders = joblib.load("encoders.pkl")
feature_columns = joblib.load("feature_columns.pkl")

st.set_page_config(page_title="Attrition Probability Predictor", layout="wide")
st.title("🔮 Employee Attrition Probability Predictor")
st.markdown("Masukkan data karyawan di bawah ini untuk memprediksi kemungkinan karyawan akan resign atau tetap.")

with st.form("prediction_form"):
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.slider("Age", 18, 60, 30)
        business_travel = st.selectbox("Business Travel", ["Non-Travel", "Travel_Rarely", "Travel_Frequently"])
        daily_rate = st.number_input("Daily Rate", min_value=0)
        department = st.selectbox("Department", ["Sales", "Research & Development", "Human Resources"])
        distance_from_home = st.slider("Distance From Home", 0, 50, 10)
        education = st.selectbox("Education Level", [1, 2, 3, 4, 5])
        education_field = st.selectbox("Education Field", ["Life Sciences", "Medical", "Marketing", "Technical Degree", "Human Resources", "Other"])

    with col2:
        environment_satisfaction = st.selectbox("Environment Satisfaction", [1, 2, 3, 4])
        gender = st.selectbox("Gender", ["Male", "Female"])
        hourly_rate = st.number_input("Hourly Rate", min_value=0)
        job_involvement = st.selectbox("Job Involvement", [1, 2, 3, 4])
        job_level = st.selectbox("Job Level", [1, 2, 3, 4, 5])
        job_role = st.selectbox("Job Role", ["Sales Executive", "Research Scientist", "Laboratory Technician", "Manufacturing Director", "Healthcare Representative", "Manager", "Sales Representative", "Research Director", "Human Resources"])
        job_satisfaction = st.selectbox("Job Satisfaction", [1, 2, 3, 4])

    with col3:
        marital_status = st.selectbox("Marital Status", ["Single", "Married", "Divorced"])
        monthly_income = st.number_input("Monthly Income", min_value=0)
        monthly_rate = st.number_input("Monthly Rate", min_value=0)
        num_companies_worked = st.slider("Num Companies Worked", 0, 10, 1)
        over_time = st.selectbox("Over Time", ["Yes", "No"])
        percent_salary_hike = st.slider("Percent Salary Hike", 0, 100, 15)
        performance_rating = st.selectbox("Performance Rating", [1, 2, 3, 4])

    st.markdown("---")
    col4, col5, col6 = st.columns(3)

    with col4:
        relationship_satisfaction = st.selectbox("Relationship Satisfaction", [1, 2, 3, 4])
        stock_option_level = st.selectbox("Stock Option Level", [0, 1, 2, 3])
        total_working_years = st.slider("Total Working Years", 0, 40, 10)
        training_times_last_year = st.slider("Training Times Last Year", 0, 10, 2)
        work_life_balance = st.selectbox("Work Life Balance", [1, 2, 3, 4])

    with col5:
        years_at_company = st.slider("Years At Company", 0, 40, 5)
        years_in_current_role = st.slider("Years In Current Role", 0, 20, 3)
        years_since_last_promotion = st.slider("Years Since Last Promotion", 0, 15, 1)
        years_with_curr_manager = st.slider("Years With Current Manager", 0, 20, 4)

    submitted = st.form_submit_button("Predict Attrition Probability")

if submitted:
    input_dict = {
        "age": age,
        "business_travel": business_travel,
        "daily_rate": daily_rate,
        "department": department,
        "distance_from_home": distance_from_home,
        "education": education,
        "education_field": education_field,
        "employee_count": 1,
        "environment_satisfaction": environment_satisfaction,
        "gender": gender,
        "hourly_rate": hourly_rate,
        "job_involvement": job_involvement,
        "job_level": job_level,
        "job_role": job_role,
        "job_satisfaction": job_satisfaction,
        "marital_status": marital_status,
        "monthly_income": monthly_income,
        "monthly_rate": monthly_rate,
        "num_companies_worked": num_companies_worked,
        "over18": "Y",
        "over_time": over_time,
        "percent_salary_hike": percent_salary_hike,
        "performance_rating": performance_rating,
        "relationship_satisfaction": relationship_satisfaction,
        "standard_hours": 80,
        "stock_option_level": stock_option_level,
        "total_working_years": total_working_years,
        "training_times_last_year": training_times_last_year,
        "work_life_balance": work_life_balance,
        "years_at_company": years_at_company,
        "years_in_current_role": years_in_current_role,
        "years_since_last_promotion": years_since_last_promotion,
        "years_with_curr_manager": years_with_curr_manager
    }

    input_df = pd.DataFrame([input_dict])

    # Encode kolom kategorikal
    for col in encoders:
        input_df[col] = encoders[col].transform(input_df[col])

    # Susun ulang kolom sesuai pelatihan
    input_df = input_df[feature_columns]

    # Prediksi probabilitas
    prediction = model.predict_proba(input_df)[0]
    attrition_prob = round(prediction[1] * 100, 2)
    stay_prob = round(prediction[0] * 100, 2)

    st.success(f"🎯 Kemungkinan karyawan ini akan *resign*: {attrition_prob}%")
    st.info(f"✅ Kemungkinan akan *tetap bekerja*: {stay_prob}%")
