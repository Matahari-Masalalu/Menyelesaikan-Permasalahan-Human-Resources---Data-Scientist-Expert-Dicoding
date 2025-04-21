import streamlit as st
import pandas as pd
from pycaret.classification import load_model, predict_model
from sklearn.preprocessing import LabelEncoder

# Load model
model = load_model('model_attrition')

# Fungsi untuk melakukan encoding pada fitur objek
def encode_features(df, label_encoders):
    for col in df.select_dtypes(include='object').columns:
        le = label_encoders[col]
        df[col] = le.transform(df[col])
    return df

# Template input untuk pengguna
st.title("Prediksi Attrition Karyawan")
st.write("Masukkan data karyawan untuk memprediksi apakah mereka akan mengalami attrition atau tidak.")

# Input fitur untuk prediksi
age = st.number_input("Age", min_value=18, max_value=100, value=30)
business_travel = st.selectbox("Business Travel", options=["Travel_Rarely", "Travel_Frequently", "Non-Travel"])
daily_rate = st.number_input("Daily Rate", min_value=0, value=1500)
department = st.selectbox("Department", options=["Sales", "Research & Development", "Human Resources"])
distance_from_home = st.number_input("Distance from Home", min_value=0, value=5)
education = st.selectbox("Education", options=[1, 2, 3, 4])  # Assuming these are encoded values for Education
education_field = st.selectbox("Education Field", options=["Life Sciences", "Other", "Medical", "Marketing", "Technical Degree"])
employee_count = st.number_input("Employee Count", min_value=0, value=1)
environment_satisfaction = st.selectbox("Environment Satisfaction", options=[1, 2, 3, 4])
gender = st.selectbox("Gender", options=["Male", "Female"])
hourly_rate = st.number_input("Hourly Rate", min_value=10, value=50)
job_involvement = st.selectbox("Job Involvement", options=[1, 2, 3, 4])
job_level = st.selectbox("Job Level", options=[1, 2, 3, 4])
job_role = st.selectbox("Job Role", options=["Sales Executive", "Research Scientist", "Laboratory Technician", "Manufacturing Director", "Healthcare Representative"])
job_satisfaction = st.selectbox("Job Satisfaction", options=[1, 2, 3, 4])
marital_status = st.selectbox("Marital Status", options=["Single", "Married", "Divorced"])
monthly_income = st.number_input("Monthly Income", min_value=0, value=3000)
monthly_rate = st.number_input("Monthly Rate", min_value=0, value=5000)
num_companies_worked = st.number_input("Num Companies Worked", min_value=0, value=1)
over18 = st.selectbox("Over 18", options=["Y"])
over_time = st.selectbox("Over Time", options=["Yes", "No"])
percent_salary_hike = st.number_input("Percent Salary Hike", min_value=0, value=10)
performance_rating = st.number_input("Performance Rating", min_value=1, max_value=5, value=3)
relationship_satisfaction = st.selectbox("Relationship Satisfaction", options=[1, 2, 3, 4])
standard_hours = st.number_input("Standard Hours", min_value=0, value=80)
stock_option_level = st.selectbox("Stock Option Level", options=[0, 1, 2, 3])
total_working_years = st.number_input("Total Working Years", min_value=0, value=5)
training_times_last_year = st.number_input("Training Times Last Year", min_value=0, value=1)
work_life_balance = st.selectbox("Work Life Balance", options=[1, 2, 3, 4])
years_at_company = st.number_input("Years At Company", min_value=0, value=3)
years_in_current_role = st.number_input("Years In Current Role", min_value=0, value=2)
years_since_last_promotion = st.number_input("Years Since Last Promotion", min_value=0, value=1)
years_with_curr_manager = st.number_input("Years With Current Manager", min_value=0, value=1)

# Create a dataframe with the input values
user_input = pd.DataFrame({
    "Age": [age],
    "BusinessTravel": [business_travel],
    "DailyRate": [daily_rate],
    "Department": [department],
    "DistanceFromHome": [distance_from_home],
    "Education": [education],
    "EducationField": [education_field],
    "EmployeeCount": [employee_count],
    "EnvironmentSatisfaction": [environment_satisfaction],
    "Gender": [gender],
    "HourlyRate": [hourly_rate],
    "JobInvolvement": [job_involvement],
    "JobLevel": [job_level],
    "JobRole": [job_role],
    "JobSatisfaction": [job_satisfaction],
    "MaritalStatus": [marital_status],
    "MonthlyIncome": [monthly_income],
    "MonthlyRate": [monthly_rate],
    "NumCompaniesWorked": [num_companies_worked],
    "Over18": [over18],
    "OverTime": [over_time],
    "PercentSalaryHike": [percent_salary_hike],
    "PerformanceRating": [performance_rating],
    "RelationshipSatisfaction": [relationship_satisfaction],
    "StandardHours": [standard_hours],
    "StockOptionLevel": [stock_option_level],
    "TotalWorkingYears": [total_working_years],
    "TrainingTimesLastYear": [training_times_last_year],
    "WorkLifeBalance": [work_life_balance],
    "YearsAtCompany": [years_at_company],
    "YearsInCurrentRole": [years_in_current_role],
    "YearsSinceLastPromotion": [years_since_last_promotion],
    "YearsWithCurrManager": [years_with_curr_manager]
})

# Lakukan encoding pada input
df_model_encoded = encode_features(user_input, label_encoders)

# Prediksi dengan model yang telah diload
prediction = predict_model(model, data=df_model_encoded)

# Tampilkan hasil prediksi
st.subheader("Hasil Prediksi:")
if prediction['Label'][0] == 1:
    st.write("Karyawan ini diprediksi akan mengalami attrition.")
else:
    st.write("Karyawan ini diprediksi tidak akan mengalami attrition.")
