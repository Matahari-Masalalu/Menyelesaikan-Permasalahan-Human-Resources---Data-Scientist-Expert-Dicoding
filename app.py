import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from pycaret.classification import load_model, predict_model

st.set_page_config(page_title="HR Tools PT Jaya Jaya Maju", layout="wide")

# Fungsi untuk homepage
def home_page():
    st.title('Dashboard')
    st.write('Selamat datang di homepage!')

# Fungsi untuk halaman prediksi
def predict_page():
    # Load model
    model = load_model("model_attrition")

    st.markdown("<h1 style='text-align: center;'>🔮 Prediksi Resign Karyawan (Attrition)</h1>", unsafe_allow_html=True)

    with st.form("form"):
        col1, col2, col3 = st.columns(3)

        with col1:
            MonthlyIncome = st.number_input("Monthly Income 💰", 1000, 20000, 5000)
            MonthlyRate = st.number_input("Monthly Rate 📈", 1000, 25000, 10000)
            DailyRate = st.number_input("Daily Rate 💸", 100, 1500, 500)
            Department = st.selectbox("Departemen 🏢", ["Sales", "Research & Development", "Human Resources"])
            DistanceFromHome = st.number_input("Jarak dari Rumah 🏠", 1, 30, 10)
            Education = st.selectbox("Pendidikan 🎓", [1, 2, 3, 4, 5])
            EducationField = st.selectbox("Bidang Pendidikan 📘", ["Life Sciences", "Other", "Medical", "Marketing", "Technical Degree", "Human Resources"])
            EnvironmentSatisfaction = st.selectbox("Environment Satisfaction 🌿", [1, 2, 3, 4])
            BusinessTravel = st.selectbox("Perjalanan Bisnis ✈️", ["Travel_Rarely", "Travel_Frequently", "Non-Travel"])
            Gender = st.selectbox("Jenis Kelamin 🚻", ["Male", "Female"])
            

        with col2:
            Age = st.slider("Umur", 18, 60, 30)
            HourlyRate = st.slider("Hourly Rate 💵", 30, 100, 60)
            PercentSalaryHike = st.slider("Kenaikan Gaji (%) 💸", 10, 25, 15)
            YearsAtCompany = st.slider("Tahun di Perusahaan 🏢", 0, 40, 5)
            YearsInCurrentRole = st.slider("Tahun di Posisi Saat Ini 💼", 0, 18, 3)
            YearsSinceLastPromotion = st.slider("Tahun Sejak Promosi Terakhir ⏳", 0, 15, 2)
            YearsWithCurrManager = st.slider("Tahun dengan Manajer Saat Ini 👨‍💼", 0, 17, 3)
            TotalWorkingYears = st.slider("Total Tahun Pengalaman 🧠", 0, 40, 10)
            TrainingTimesLastYear = st.slider("Jumlah Pelatihan Tahun Ini 📚", 0, 10, 3)
            NumCompaniesWorked = st.slider("Jumlah Perusahaan Pernah Bekerja 🏭", 0, 10, 2)
            
            
            

        with col3:
            OverTime = st.selectbox("Lembur 🕒", ["Yes", "No"])
            JobInvolvement = st.selectbox("Job Involvement 👨‍💼", [1, 2, 3, 4])
            JobLevel = st.selectbox("Job Level 📊", [1, 2, 3, 4, 5])
            JobRole = st.selectbox("Job Role 💼", ["Sales Executive", "Research Scientist", "Laboratory Technician", 
                                                "Manufacturing Director", "Healthcare Representative", "Manager", 
                                                "Sales Representative", "Research Director", "Human Resources"])
            JobSatisfaction = st.selectbox("Job Satisfaction 😊", [1, 2, 3, 4])
            PerformanceRating = st.selectbox("Performance Rating ⭐", [1, 2, 3, 4])
            RelationshipSatisfaction = st.selectbox("Relationship Satisfaction ❤️", [1, 2, 3, 4])
            StockOptionLevel = st.selectbox("Stock Option Level 📈", [0, 1, 2, 3])
            WorkLifeBalance = st.selectbox("Work Life Balance ⚖️", [1, 2, 3, 4])
            MaritalStatus = st.selectbox("Status Pernikahan 💍", ["Single", "Married", "Divorced"])

        col_left, col_mid, col_right = st.columns([3,1,3])

        with col_mid:
            submitted = st.form_submit_button("🔍 Prediksi")

    if submitted:
        input_dict = {
            'Age': Age,
            'BusinessTravel': BusinessTravel,
            'DailyRate': DailyRate,
            'Department': Department,
            'DistanceFromHome': DistanceFromHome,
            'Education': Education,
            'EducationField': EducationField,
            'EnvironmentSatisfaction': EnvironmentSatisfaction,
            'Gender': Gender,
            'HourlyRate': HourlyRate,
            'JobInvolvement': JobInvolvement,
            'JobLevel': JobLevel,
            'JobRole': JobRole,
            'JobSatisfaction': JobSatisfaction,
            'MaritalStatus': MaritalStatus,
            'MonthlyIncome': MonthlyIncome,
            'MonthlyRate': MonthlyRate,
            'NumCompaniesWorked': NumCompaniesWorked,
            'OverTime': OverTime,
            'PercentSalaryHike': PercentSalaryHike,
            'PerformanceRating': PerformanceRating,
            'RelationshipSatisfaction': RelationshipSatisfaction,
            'StockOptionLevel': StockOptionLevel,
            'TotalWorkingYears': TotalWorkingYears,
            'TrainingTimesLastYear': TrainingTimesLastYear,
            'WorkLifeBalance': WorkLifeBalance,
            'YearsAtCompany': YearsAtCompany,
            'YearsInCurrentRole': YearsInCurrentRole,
            'YearsSinceLastPromotion': YearsSinceLastPromotion,
            'YearsWithCurrManager': YearsWithCurrManager,
        }

        input_df = pd.DataFrame([input_dict])

        for col in input_df.select_dtypes(include='object').columns:
            le = LabelEncoder()
            input_df[col] = le.fit_transform(input_df[col])
        hasil = predict_model(model, data=input_df)
        pred = hasil['prediction_label'][0]
        prob = hasil['prediction_score'][0]

        st.markdown("---")
        st.markdown("<h3>🎯 Hasil Prediksi:</h3>", unsafe_allow_html=True)
        st.write(hasil)
        if pred == 1:
            st.warning("Karyawan ini berpotensi resign!😢")
        else:
            st.success("Karyawan ini tidak berpotensi resign!😄")
        st.info(f"🎯 Probabilitas: **{round(prob*100, 2)}%**")

# Toggle burger menggunakan sidebar
def toggle_burger():
    pages = {
        'Home': home_page,
        'Predict Featur': predict_page,
    }
    st.sidebar.title("PT Maju Jaya Jaya")
    st.sidebar.image("logo2.png", width=200)
    page = st.sidebar.selectbox('Pilih Halaman', list(pages.keys()))

    # Panggil halaman yang dipilih
    pages[page]()

if __name__ == '__main__':
    toggle_burger()
