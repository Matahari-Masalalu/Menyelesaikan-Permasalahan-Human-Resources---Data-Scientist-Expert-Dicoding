# Proyek Akhir: Menyelesaikan Permasalahan Human Resources di Perusahaan Jaya Jaya Maju

## Business Understanding

**Jaya Jaya Maju** adalah perusahaan multinasional yang telah berdiri sejak tahun 2000 dan memiliki lebih dari 1000 karyawan. Perusahaan ini menghadapi tantangan dalam hal tingginya tingkat *attrition* (pergantian karyawan), yang berdampak negatif terhadap operasional dan biaya.

## Permasalahan Bisnis

- Tingginya tingkat attrition (>10%) menyebabkan gangguan produktivitas dan beban rekrutmen baru.
- Tidak adanya alat prediktif untuk mendeteksi karyawan yang berpotensi resign.
- Perlu solusi berbasis data untuk pengambilan keputusan di departemen HR.

## Cakupan Proyek

- Analisis faktor-faktor penyebab attrition.
- Visualisasi data dan insight melalui **Tableau Public**.
- Pembuatan model machine learning menggunakan **Extra Trees Classifier**.

## Persiapan

### Sumber Data
Dataset diambil dari:  
🔗 [Employee Data - GitHub](https://github.com/dicodingacademy/dicoding_dataset/blob/main/employee/employee_data.csv)

## Dashboard Analitik - Tableau Public
untuk link dashboard bisa diakses melalui

link dashboard 1 : [link dashboard 11](https://public.tableau.com/views/JayaJayaMajuDicoding/Dashboard3?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

link dashboard 2 : [link dashboard 2](https://public.tableau.com/views/JayaJayaMajuDicoding2/Dashboard1?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

![image](https://github.com/user-attachments/assets/24963151-707c-43b6-8540-8d008e210d54)
![image](https://github.com/user-attachments/assets/c3c43c23-1ace-4c3f-8efa-d20b75741ade)



Komponen Dashboard:

- Education & Department Distribution : Mayoritas karyawan berlatar pendidikan Bachelor, dan departemen terbesar adalah R&D.

- Job Satisfaction : Sekitar 60% karyawan memiliki kepuasan kerja tinggi, namun attrition tetap terjadi di berbagai level.

- Environment Satisfaction : Tingkat kepuasan lingkungan kerja sangat memengaruhi keputusan keluar.

- Work Life Balance : Karyawan dengan WLB "Excellent" cenderung bertahan. Nilai "Bad" memiliki attrition lebih tinggi.

- Overall Attrition Distribution : 16.99% dari seluruh karyawan mengalami attrition (berdasarkan pie chart utama).

- Attrition vs Overtime Status : Karyawan yang bekerja lembur memiliki kecenderungan keluar lebih besar. Contoh: 81 dari 179 karyawan yang lembur mengalami attrition.

- Job Satisfaction by Role and Attrition : Menunjukkan distribusi attrition berdasarkan peran dan tingkat kepuasan kerja. Beberapa role seperti Sales Executive dan Laboratory Technician menunjukkan tingkat attrition tinggi.

- Environment Satisfaction by Role and Attrition : Role tertentu dengan kepuasan lingkungan kerja rendah menunjukkan peningkatan risiko attrition.

## Sistem Machine Learning

### Eksperimen Model

Proses pemodelan dilakukan menggunakan framework **PyCaret** yang memungkinkan perbandingan otomatis berbagai algoritma klasifikasi.

#### Langkah-langkah:
1. Preprocessing data: Meliputi penanganan fitur kategorikal, numerik, dan missing value. Selain itu, dilakukan feature selection menggunakan RFE (Recursive Feature Elimination) untuk memilih fitur terbaik, serta penanganan data tidak seimbang menggunakan SMOTE (Synthetic Minority Over-sampling Technique).

2. Inisialisasi setup PyCaret dengan target = Attrition.

3. Evaluasi dan bandingkan berbagai model berdasarkan metrik seperti accuracy, AUC, recall, dan F1-score.

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

###  Model Terpilih:
- **K Neighbors Classifier**  
K-Nearest Neighbors (KNN) Classifier adalah algoritma sederhana dan fleksibel yang tidak memerlukan pelatihan model sebelumnya. KNN bekerja dengan menghitung jarak ke tetangga terdekat untuk melakukan prediksi, sehingga cocok untuk tugas klasifikasi dan regresi. Keunggulannya termasuk kemudahan implementasi, akurasi yang baik pada data sederhana, serta tidak bergantung pada asumsi distribusi data. Namun, KNN bisa lambat pada dataset besar karena harus menghitung jarak ke semua data setiap kali prediksi.

---

## Kesimpulan
- Grafik "Attrition vs Overtime Status" menunjukkan bahwa karyawan yang bekerja lembur memiliki kemungkinan keluar yang jauh lebih tinggi. Dari 179 karyawan yang lembur, 98 orang mengalami attrition (sekitar 55%), jauh lebih tinggi dibandingkan mereka yang tidak lembur. Ini memperkuat bahwa overtime adalah salah satu faktor paling signifikan dalam keputusan karyawan untuk meninggalkan perusahaan.

- Dari grafik distribusi berdasarkan peran, terlihat bahwa posisi Sales Executive mendominasi jumlah attrition di hampir semua level kepuasan lingkungan dan pekerjaan. Meskipun bukan satu-satunya peran dengan tingkat keluar yang tinggi, jumlah karyawan keluar dari posisi ini secara absolut adalah yang tertinggi, menunjukkan bahwa divisi ini perlu perhatian lebih. Jadi, bukan seluruh departemen Sales, tapi spesifik pada Sales Executive.

- Karyawan dengan kepuasan rendah terhadap lingkungan kerja maupun pekerjaan lebih cenderung keluar, terlihat dari tingginya jumlah attrition (warna oranye) pada kategori "Low" di kedua grafik Job Satisfaction dan Environment Satisfaction. Hal ini menekankan pentingnya menciptakan lingkungan kerja yang positif dan memberikan pekerjaan yang memuaskan untuk menekan attrition.

- Dengan pola attrition yang cukup jelas (misalnya keterkaitan dengan overtime dan kepuasan), model seperti Extra Trees Classifier yang bekerja baik pada data tabular dan mampu menangani non-linearitas bisa sangat efektif untuk memprediksi attrition. Model ini cocok untuk digunakan sebagai dasar sistem peringatan dini bagi HR dalam mengantisipasi potensi kehilangan karyawan.

## Rekomendasi Action Items
- Karena lembur terbukti sebagai indikator kuat attrition, perusahaan perlu Meninjau ulang distribusi beban kerja dan Menerapkan pembatasan jam lembur. Memastikan lembur bersifat sukarela dan diberikan kompensasi yang adil. Melacak pola lembur sebagai indikator risiko resign secara proaktif.
- Karena Sales Executive merupakan peran dengan attrition tertinggi, disarankan: Melakukan audit mendalam terhadap job description, target penjualan, dan budaya kerja di posisi ini. Menilai apakah ekspektasi realistis dan mendukung kesejahteraan karyawan. Kembangkan Program Retensi, Pelatihan, dan Engagement
- Fokus pada peningkatan kepuasan kerja dan lingkungan melalui: Program pelatihan pengembangan karier. Coaching dan mentoring rutin. Forum komunikasi dua arah antara manajemen dan karyawan. Lakukan Exit Interview yang Terstruktur dan Analitis
- Gunakan hasil exit interview sebagai umpan balik sistematis untuk: Mengidentifikasi akar masalah berdasarkan role, departemen, dan kepuasan kerja. Mengintegrasikan temuan ini ke dalam strategi HR untuk mencegah attrition di masa depan.

## Referensi
1. fahadrehman07 - Kagle. Diakses pada 20 April 2025 dari (https://www.kaggle.com/code/fahadrehman07/salifort-motors-providing-data-driven-suggestions)
2. Google Colab. Diakses pada 20 April 2025 dari (https://colab.research.google.com/drive/1iVo19vQtD5hk-Kcjuqb2Vg33bMnA1vLu?usp=sharing)
