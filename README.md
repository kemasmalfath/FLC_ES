# 🎓 Sistem Diagnosa Tingkat Stres Mahasiswa Menggunakan Logika Fuzzy

## 📌 Deskripsi Proyek

Mahasiswa tingkat akhir sering mengalami stres saat menyusun tugas akhir (skripsi atau tesis). Tingkat stres ini bersifat subjektif dan tidak pasti, dipengaruhi oleh berbagai faktor seperti:


- Tingkat kesulitan materi yang dihadapi,
- Frekuensi konsultasi dengan dosen pembimbing,
- Kualitas istirahat atau tidur mahasiswa.
Sistem ini dibangun menggunakan **logika  fuzzy** untuk mengakomodasi data linguistik dan ketidakpastian dalam mendiagnosis tingkat stres. Diharapkan, sistem ini dapat membantu **dosen wali atau konselor kampus** dalam mengidentifikasi kondisi psikologis mahasiswa dan memberikan rekomendasi yang sesuai.
## 🧠 Tujuan Sistem
- Mendiagnosa **tingkat stres mahasiswa tingkat akhir** berdasarkan gejala subjektif.
- Menggunakan pendekatan fuzzy untuk menangani ketidakpastian dan data linguistik.
- Memberikan **rekomendasi** yang sesuai berdasarkan hasil diagnosa

## 🧩 Variabel dalam Sistem

### 📥 Variabel Input:

1. **Tingkat Kesulitan Materi (0 - 100)**
   - Rendah
   - Sedang
   - Tinggi

2. **Frekuensi Konsultasi per Minggu (0 - 10)**
   - Jarang
   - Normal
   - Sering

3. **Kualitas Istirahat (0 - 100)**
   - Buruk
   - Cukup
   - Baik
### 📤 Variabel Output:

- **Tingkat Stres Mahasiswa (0 - 100)**
  - Ringan
  - Sedang
  - Berat

---

## 🧾 Aturan Fuzzy (Knowledge Base)

Beberapa aturan logika fuzzy yang digunakan dalam sistem ini:

- Jika kesulitan materi **rendah**, konsultasi **jarang**, dan istirahat **baik**, maka stres **ringan**.
- Jika kesulitan materi **sedang**, konsultasi **normal**, dan istirahat **cukup**, maka stres **sedang**.
- Jika kesulitan materi **tinggi**, konsultasi **sering**, dan istirahat **buruk**, maka stres **berat**.
- Jika kesulitan materi **tinggi** atau istirahat **buruk**, maka stres **sedang**.
- Dan aturan lainnya sesuai dengan basis pengetahuan psikologis.

---

## 📊 Visualisasi Fungsi Keanggotaan

Sistem ini menampilkan grafik fungsi keanggotaan untuk setiap variabel:

- Tingkat Kesulitan Materi
- Frekuensi Konsultasi
- Kualitas Istirahat
- Tingkat Stres Mahasiswa

Visualisasi ini penting untuk memahami bagaimana nilai input linguistik dikonversi menjadi numerik melalui fungsi fuzzy.

---

## ⚙️ Teknologi dan Library yang Digunakan

- Python 3.x
- [Scikit-Fuzzy](https://github.com/scikit-fuzzy/scikit-fuzzy) (`skfuzzy`)
- Matplotlib (`matplotlib.pyplot`)
- Google Colaboratory (Colab)

---

## 📥 Cara Menjalankan

1. Buka [Google Colab](https://colab.research.google.com)
2. Install library:
   ```python
   !pip install scikit-fuzzy
   ```
3. Jalankan seluruh sel kode dari atas ke bawah.
4. Masukkan input sesuai prompt:
   - Tingkat kesulitan materi (0 - 100)
   - Frekuensi konsultasi per minggu (0 - 10)
   - Kualitas istirahat (0 - 100)
5. Sistem akan menghitung dan menampilkan hasil berupa tingkat stres serta rekomendasi.

---

## 📽️ Video Penjelasan

Video penjelasan dan demo dapat dilihat di YouTube:  
📺 [Link Video YouTube Anda di sini](https://youtube.com)

---

## 📅 Informasi Tugas

- **Tema**: Diagnosa Tingkat Stres Mahasiswa Saat Menghadapi Tugas Akhir
- **Deadline Pengumpulan**: Rabu, 18 Juni 2024, pukul 23:59 WIB
- **Link Form Pengumpulan**: [https://forms.gle/99Tx2c8QEmD9Fove9](https://forms.gle/99Tx2c8QEmD9Fove9)

---

## 🙋‍♂️ Interpretasi Output

Output akhir berupa nilai numerik dari tingkat stres mahasiswa, disertai dengan interpretasi:

| Nilai Output | Interpretasi       | Rekomendasi                                                         |
|--------------|--------------------|----------------------------------------------------------------------|
| 0 - 40       | **Stres Ringan**   | Pertahankan pola kerja dan istirahat yang baik.                     |
| 41 - 70      | **Stres Sedang**   | Perlu manajemen waktu dan konsultasi rutin dengan pembimbing.      |
| 71 - 100     | **Stres Berat**    | Segera konsultasikan ke dosen wali atau layanan konseling kampus.  |

---

## 📚 Referensi

- Teori Logika Fuzzy oleh Lotfi Zadeh
- Modul Psikologi Pendidikan dan Konseling Mahasiswa
- Dokumentasi Scikit-Fuzzy

---

## 👨‍💻 Author

Proyek ini dibuat oleh:  
**Nama:** [Nama Anda]  
**NIM:** [Nomor Induk Mahasiswa]  
**Kelas:** [Nama Kelas atau Prodi]



## ✅ Lisensi

Proyek ini bersifat edukatif dan bebas digunakan untuk pembelajaran.
