# Analisis Review Amazon Menggunakan NLP & Machine Learning

Deskripsi Singkat / Overview
Project ini menganalisis ulasan produk Amazon untuk memahami opini pelanggan serta memprediksi rating menggunakan metode NLP dan machine learning. Hasil analisis memberikan insight actionable bagi tim marketing, product management, dan stakeholder bisnis.

## 1. Dataset

Sumber: Kaggle (https://www.kaggle.com/datasets/karkavelrajaj/amazon-sales-dataset)
Jumlah Data: 1351
Kolom Penting:
- category
- discounted_price
- actual_price 
- discount_percentage 
- rating 
- rating_count - Number of people who voted for the Amazon rating
- review_title - Short review
- review_content - Long review

## 2. Tools & Library

Bahasa / Platform: Python, Google Colab / Jupyter Notebook
Library: Pandas, Numpy, Scikit-Learn, Matplotlib, Seaborn, NLTK, spaCy, TextBlob / VADER, WordCloud

## 3. Objective / Tujuan
- Membersihkan dan menyiapkan data review untuk analisis NLP & modelling
- Menemukan tren dan insight dari review pelanggan (EDA)
- Memprediksi sentimen review (Positive / Negative / Neutral)
- Memprediksi rating akhir (1–5) dari review text
- Memberikan rekomendasi actionable untuk seller dan pembeli

## 4. Workflow / Langkah Pengerjaan
### 4.1 Data Cleaning & Preprocessing
- Lowercasing
- Remove noise: HTML tags, URL, angka, tanda baca, emoji
- Tokenization
- Stopword removal
- Lemmatization
- Membuat kolom tambahan: cleaned_title, cleaned_content, content_length
- Menghitung sentiment polarity menggunakan TextBlob/VADER
Insight: Teks menjadi konsisten dan siap untuk NLP & model prediksi.

### 4.2 Exploratory Data Analysis (EDA)
- Distribusi Rating: Mayoritas rating 4–5, menunjukkan review lebih informatif dari angka rating.
- Distribusi Kategori: Electronics & Clothing paling populer.
- Rata-rata Rating per Kategori: Health & Beauty paling konsisten, Electronics banyak ulasan tapi rating fluktuatif.
- Wordcloud Review Content: Dominan kata good, great, quality → review positif tapi generik.
- Correlation Heatmap: Antar fitur numerik (rating, content_length, sentiment_score) sangat lemah → rating tidak dipengaruhi langsung oleh panjang review atau sentiment polarity.

### 4.3 Sentiment Score Analysis (Tanpa Label)
- Menghitung polarity (-1 sampai 1)
- Rata-rata per kategori
Insight:
- Semua kategori mayoritas positif
- Electronics lebih rendah dibanding kategori lain → sejalan dengan rating

### 4.4 NLP Analysis – Top Words & N-Grams

- Top Words: good, great, product, price, quality
- N-Gram Analysis: “great product”, “good quality”, “worth the money”
Insight: Menunjukkan opini utama konsumen tentang kualitas & harga

### 4.5 Balanced Rating Classification
- Membuat kelas rating: Low, Mid, High
- Model: Logistic Regression / SVM / Random Forest
- Hasil: F1-score tinggi → model mendeteksi review berkualitas rendah dengan akurat

### 4.6 Rating Regression Model
- Model: Random Forest Regressor
- Fitur: content_length, sentiment score, kategori (encoded)
Contoh prediksi:
sample_review = "this product is absolutely great and worth the money"
Predicted rating → 4.11
Insight: Model mampu memprediksi rating akhir dari teks, bermanfaat untuk deteksi potensi komplain sejak awal.

### 4.7 Final Insights

- Electronics: laris, ulasan negatif terbanyak, sentiment rendah
- Health & Beauty: stabil, disukai pembeli
- Sentiment score vs rating: korelasi lemah → rating tinggi tidak selalu kualitas tinggi
- Top Words & N-Grams: fokus pada kualitas & harga
- Pipeline end-to-end: Cleaning → EDA → NLP → Modeling → Prediction → Insight

### Visualisasi

- Distribusi rating

  <img width="540" height="391" alt="image" src="https://github.com/user-attachments/assets/f9db9524-014d-4557-90f1-3502be20e213" />

  Mayoritas rating 4–5.

- Distribusi kategori
  <img width="1147" height="449" alt="image" src="https://github.com/user-attachments/assets/dfb79166-e567-4577-a07f-bcde3d5ddd80" />

  Electronics & Clothing paling populer.

- Rata-rata rating per kategori
  <img width="1147" height="526" alt="image" src="https://github.com/user-attachments/assets/0b491c71-30d8-4b6a-9f49-dd7d33a8ce1a" />

  Health & Beauty paling konsisten, Electronics banyak ulasan tapi rating fluktuatif.

- Correlation heatmap
  <img width="900" height="657" alt="image" src="https://github.com/user-attachments/assets/3b0a5584-89b5-4c6c-a3d0-437be191699f" />

  Hubungan di antara kolom penting positif namun lemah sehingga tidak berpengaruh secara langsung.

- Wordcloud & Top Words
  
  <img width="950" height="602" alt="image" src="https://github.com/user-attachments/assets/9c9a7ae2-fc4f-43e0-b6dd-6f9927ef019d" />

  Dominan kata good, great, quality yang menandakan review positif.

- Sentiment Score per kategori
  
  <img width="717" height="437" alt="image" src="https://github.com/user-attachments/assets/bfb1a1e9-579e-4b5d-87e4-c54c53937990" />

  Review Title dan Review Content nya menyatakan review sangat positif di antara musical instruments, toys n games, dan office product, sebaliknya electronics sebagai kategori rating   terbanyak memiliki skor rendah ke 3/9
  
## 8. Tech Stack
- Python (Pandas, Numpy)
- Matplotlib, Seaborn
- Scikit-Learn
- NLTK / spaCy
- TextBlob / VADER
- WordCloud

## 9. Kesimpulan / Takeaways

Proyek ini menunjukkan bagaimana NLP dan predictive modeling dapat digunakan untuk memahami opini pelanggan, mendukung keputusan marketing, serta menyediakan insight actionable untuk penjual dan pembeli.
