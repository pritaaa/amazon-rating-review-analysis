# Analisis Review Amazon Menggunakan NLP & Machine Learning
# Health Insurance Pricing & Risk Analysis

## Business Context

Perusahaan asuransi kesehatan perlu menyeimbangkan **profitabilitas** dan **manajemen risiko**. Tantangan utama:

* Menentukan premi yang adil namun tetap menguntungkan
* Mengidentifikasi pelanggan berisiko tinggi sejak awal
* Mengurangi lonjakan biaya klaim melalui strategi preventif

Project ini mensimulasikan peran **Data / Business Analyst** dalam membantu tim **Underwriting, Pricing, dan Marketing** mengambil keputusan berbasis data.

---

## Objective (Business-Oriented)

* Membantu tim underwriting mengelompokkan pelanggan berdasarkan tingkat risiko
* Mendukung tim pricing dalam menentukan **tier premi**
* Memberikan simulasi kebijakan (what-if analysis) untuk menurunkan biaya klaim

---

## Stakeholders

* **Underwriting Team** – klasifikasi risiko pelanggan
* **Pricing Team** – penentuan premi berbasis risiko
* **Marketing / Health Program Team** – program preventif (diet, stop smoking)

---

## Dataset

* Source: Medical Insurance Cost Dataset (Kaggle)
* Records: 1,338 pelanggan
* Key Features:

  * Age, BMI, Smoker Status, Children, Region
  * Target: Insurance Charges

---

## Tools & Workflow

**Python (Pandas, NumPy)** – data cleaning & analysis
**EDA & Visualization** – identifikasi pola risiko
**Scikit-Learn** – regression & risk modeling
**Scenario Analysis** – simulasi kebijakan bisnis

Workflow:

1. Data Cleaning & Validation
2. Exploratory Data Analysis (EDA)
3. Risk Scoring Development (0–100)
4. Cost Prediction (Regression Model)
5. Scenario Analysis (Policy Simulation)
6. Business Insight & Recommendation

---

## Key Analysis & Insights

### Risk Drivers

* **Smoker status** meningkatkan biaya hingga ±200–300%
* **BMI tinggi** berhubungan langsung dengan lonjakan biaya
* **Usia** menunjukkan peningkatan risiko yang stabil

### High-Risk Segment

Pelanggan dengan kombinasi:

* Smoker
* BMI tinggi
* Usia menengah–lanjut

Merupakan kontributor biaya tertinggi.

---

## Scenario Analysis (What-If)

* Menurunkan BMI sebesar 5 poin → penurunan prediksi biaya signifikan
* Perubahan status **smoker → non-smoker** memberikan dampak terbesar

Simulasi ini membantu tim memahami **dampak kebijakan preventif sebelum diterapkan**.

---

## Business Recommendations

* Terapkan **tiered premium pricing** berbasis risk score
* Berikan **diskon premi** bagi pelanggan yang mengikuti program kesehatan
* Prioritaskan program stop-smoking untuk segmen risiko tinggi

---

## Business Impact (Estimated)

* Potensi pengurangan biaya klaim jangka menengah
* Profil risiko pelanggan lebih terkendali
* Strategi pricing lebih transparan dan adil

---

## Takeaway

Project ini menunjukkan bagaimana analisis data dapat:

* Menghubungkan data → keputusan bisnis
* Mendukung strategi pricing & risk management
* Digunakan langsung oleh tim non-teknis dalam pengambilan keputusan
