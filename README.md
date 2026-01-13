# Analisis Review Amazon Menggunakan NLP & Machine Learning
Amazon Rating Analysis (Customer Insight & Quality Monitoring)
## Business Context
Sebagai marketplace besar, Amazon perlu memahami kualitas produk dan potensi risiko keluhan pelanggan dari review teks yang masuk setiap hari. Project ini berperan sebagai simulasi pekerjaan Data Analyst / Business Analyst yang membantu tim Product, Marketing, dan Seller Management membaca sinyal awal dari customer feedback.

## Business Questions
* Kategori produk mana yang paling berisiko menghasilkan review negatif?
* Apakah sentiment review bisa digunakan sebagai early signal sebelum rating turun?
* Bagaimana insight review dapat membantu prioritas perbaikan produk dan campaign?

## Data Overview
Sumber: Amazon Product Reviews (Kaggle)
Total data: 1.351 review
Informasi utama: kategori produk, harga & diskon, rating, isi review teks

## Key Metrics & Dimensions
* Metrics
*  Rating (1–5)
*  Sentiment score
*  Rating class (Low / Mid / High)
  
## Dimensions
*  Product category
*  Review text
*  Price & discount
*  Analysis Summary (Insight-Oriented)
  
### 1. Customer Sentiment vs Rating
*  Mayoritas review bersentimen positif, namun sentiment tinggi tidak selalu berarti rating tinggi.
*  Korelasi sentiment–rating lemah → risiko produk bermasalah bisa tersembunyi di balik review positif generik.

### 2. Category Risk Profiling
*  Electronics: volume review tinggi, sentiment relatif rendah, rating paling fluktuatif → kategori paling berisiko.
*  Health & Beauty: rating stabil dan konsisten → kualitas produk lebih terjaga.

### 3. NLP Insight (What Customers Care About)
* Kata dominan: quality, price, worth the money.
*  Fokus pelanggan bukan fitur kompleks, tapi value for money & kualitas dasar.

### 4. Predictive Use Case
*  Model klasifikasi mampu mendeteksi review berisiko rendah rating.
*  Model regresi dapat memperkirakan rating hanya dari teks → berguna untuk early complaint detection.

## Business Recommendations
*  Prioritaskan quality monitoring untuk kategori Electronics.
*  Gunakan sentiment & keyword review sebagai alert system sebelum rating turun.
*  Seller dengan review negatif berulang dapat diarahkan ke program quality improvement.
*  Marketing dapat menyesuaikan campaign berdasarkan pain point utama pelanggan (harga & kualitas).

## Tools & Workflow (Industry-Style)
* Python (data cleaning & analysis)
* NLP for text understanding
* Machine Learning for prediction
*  GitHub for documentation & collaboration

