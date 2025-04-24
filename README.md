# Proyek Akhir: Prediksi Tingkat Attrition di Perusahaan Jaya Jaya Maju

## Business Understanding

**Jaya Jaya Maju** adalah perusahaan multinasional yang telah berdiri sejak tahun 2000 dan memiliki lebih dari 1000 karyawan. Perusahaan ini menghadapi tantangan dalam hal tingginya tingkat *attrition* (pergantian karyawan), yang berdampak negatif terhadap operasional dan biaya.

## Permasalahan Bisnis

- Tingginya tingkat attrition (>10%) menyebabkan gangguan produktivitas dan beban rekrutmen baru.
- Tidak adanya alat prediktif untuk mendeteksi karyawan yang berpotensi resign.
- Perlu solusi berbasis data untuk pengambilan keputusan di departemen HR.

## Cakupan Proyek

- Analisis faktor-faktor penyebab attrition.
- Pembuatan model machine learning menggunakan **Extra Trees Classifier**.
- Visualisasi data dan insight melalui **Tableau Public**.

## Persiapan dan Setup

### Sumber Data
Dataset diambil dari:  
🔗 [Employee Data - GitHub](https://github.com/dicodingacademy/dicoding_dataset/blob/main/employee/employee_data.csv)

## Dashboard Analitik - Looker Studio
untuk link dashboard
link dashboard 1 : https://public.tableau.com/views/JayaJayaMajuDicoding/Dashboard3?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link

link dashboard 2 : https://public.tableau.com/views/JayaJayaMajuDicoding2/Dashboard1?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link

![image](https://github.com/user-attachments/assets/24963151-707c-43b6-8540-8d008e210d54)
![image](https://github.com/user-attachments/assets/c3c43c23-1ace-4c3f-8efa-d20b75741ade)



Komponen Dashboard:

- Education & Department Distribution : Mayoritas karyawan berlatar pendidikan Bachelor, dan departemen terbesar adalah R&D.

### Job Satisfaction
Sekitar 60% karyawan memiliki kepuasan kerja tinggi, namun attrition tetap terjadi di berbagai level.

### Environment Satisfaction
Tingkat kepuasan lingkungan kerja sangat memengaruhi keputusan keluar.

### Work Life Balance
Karyawan dengan WLB "Excellent" cenderung bertahan. Nilai "Bad" memiliki attrition lebih tinggi.

### Overall Attrition Distribution
16.99% dari seluruh karyawan mengalami attrition (berdasarkan donut chart utama).

### Attrition vs Overtime Status
Karyawan yang bekerja lembur memiliki kecenderungan keluar lebih besar. Contoh: 81 dari 670 karyawan yang lembur mengalami attrition.

### Job Satisfaction by Role and Attrition
Menunjukkan distribusi attrition berdasarkan peran dan tingkat kepuasan kerja. Beberapa role seperti Sales Executive dan Laboratory Technician menunjukkan tingkat attrition tinggi.

### Environment Satisfaction by Role and Attrition
Role tertentu dengan kepuasan lingkungan kerja rendah menunjukkan peningkatan risiko attrition.

## 🤖 Sistem Machine Learning

### 📌 Eksperimen Model

Proses pemodelan dilakukan menggunakan framework **PyCaret** yang memungkinkan perbandingan otomatis berbagai algoritma klasifikasi.

#### ⚙️ Langkah-langkah:
1. Preprocessing data (handling kategorikal, numerik, dan missing value).
2. Inisialisasi setup PyCaret dengan target = `Attrition`.
3. Evaluasi dan bandingkan berbagai model berdasarkan metrik berikut:

| Metrik Evaluasi | Deskripsi |
|-----------------|-----------|
| **Accuracy**    | Ketepatan model secara keseluruhan |
| **AUC (ROC)**   | Kemampuan model membedakan kelas |
| **Recall**      | Kemampuan mendeteksi karyawan yang benar-benar keluar |
| **Precision**   | Akurasi dari prediksi keluar |
| **F1-score**    | Harmoni antara Recall dan Precision |
| **Kappa**       | Agreement antara prediksi dan aktual |
| **MCC**         | Korelasi antara label aktual dan prediksi |

Dari hasil eksperimen, model **K Neighbors Classifier** dipilih sebagai model terbaik berdasarkan keseimbangan skor di seluruh metrik tersebut.

### 📌 Model Terpilih:
- **K Neighbors Classifier**  
K-Nearest Neighbors (KNN) Classifier adalah algoritma sederhana dan fleksibel yang tidak memerlukan pelatihan model sebelumnya. KNN bekerja dengan menghitung jarak ke tetangga terdekat untuk melakukan prediksi, sehingga cocok untuk tugas klasifikasi dan regresi. Keunggulannya termasuk kemudahan implementasi, akurasi yang baik pada data sederhana, serta tidak bergantung pada asumsi distribusi data. Namun, KNN bisa lambat pada dataset besar karena harus menghitung jarak ke semua data setiap kali prediksi.

---

### 🌐 Akses Aplikasi:
🔗 [Buka Aplikasi Streamlit](https://zainalfatt-idcamp-data-scientist-terapan-dicoding-proyek-perta.streamlit.app/)

### 📋 Fitur Aplikasi:
- ✅ Form input untuk memprediksi status attrition berdasarkan karakteristik karyawan.
- 🔍 Validasi input otomatis.
- 📊 Prediksi real-time dengan tampilan **confidence score**.


✅ Kesimpulan
Overtime adalah indikator kuat terhadap keputusan karyawan untuk keluar.

Karyawan dengan Work-Life Balance rendah (nilai 1-2) memiliki proporsi keluar yang lebih tinggi.

Sales menjadi departemen dengan attrition rate tertinggi (20.69%).

Model Extra Trees bekerja baik dalam memprediksi potensi keluar karyawan.

📌 Rekomendasi Action Items
Evaluasi kebijakan lembur dan beban kerja.

Perkuat program keseimbangan kerja dan kehidupan pribadi (WLB).

Audit internal untuk departemen dengan tingkat keluar tinggi.

Kembangkan program retensi, pelatihan, dan engagement.

Lakukan exit interview untuk menemukan akar masalah attrition.

Proyek ini diharapkan menjadi solusi prediktif dan strategis bagi tim HR dalam menurunkan angka attrition serta meningkatkan kepuasan dan retensi karyawan.
