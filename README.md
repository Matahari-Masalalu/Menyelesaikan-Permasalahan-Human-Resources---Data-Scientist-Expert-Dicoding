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
- Deploy model ke aplikasi berbasis **Streamlit**.
- Visualisasi data dan insight melalui **Looker Studio Dashboard**.

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

### Education & Department Distribution

Mayoritas karyawan berlatar pendidikan Bachelor, dan departemen terbesar adalah R&D.

### Job Satisfaction
Sekitar 60% karyawan memiliki kepuasan kerja tinggi, namun attrition tetap terjadi di berbagai level.

### Environment Satisfaction
Tingkat kepuasan lingkungan kerja sangat memengaruhi keputusan keluar.

### Work Life Balance
Karyawan dengan WLB "Excellent" cenderung bertahan. Nilai "Bad" memiliki attrition lebih tinggi.

### Overall Attrition Distribution
16.99% dari seluruh karyawan mengalami attrition (berdasarkan donut chart utama).

### Job Satisfaction by Role and Attrition
Menunjukkan distribusi attrition berdasarkan peran dan tingkat kepuasan kerja. Beberapa role seperti Sales Executive dan Laboratory Technician menunjukkan tingkat attrition tinggi.

### Attrition vs Overtime Status
Karyawan yang bekerja lembur memiliki kecenderungan keluar lebih besar. Contoh: 81 dari 670 karyawan yang lembur mengalami attrition.

### Environment Satisfaction by Role and Attrition
Role tertentu dengan kepuasan lingkungan kerja rendah menunjukkan peningkatan risiko attrition.
🤖 Sistem Machine Learning
📌 Algoritma:
Extra Trees Classifier — handal untuk data kategori & numerik.

🌐 Akses Aplikasi:
🔗 Buka Aplikasi Streamlit

📋 Fitur:
Form input untuk prediksi status attrition.

Validasi input dan prediksi otomatis berdasarkan data.

Tampilan hasil dan confidence score.

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
