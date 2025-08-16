!pip install scikit-fuzzy
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
# Variabel input 1: Tingkat Kesulitan Materi
kesulitan_materi = ctrl.Antecedent(np.arange(0, 101, 1), 'kesulitan_materi')
kesulitan_materi['rendah'] = fuzz.trimf(kesulitan_materi.universe, [0, 0, 50])
kesulitan_materi['sedang'] = fuzz.trimf(kesulitan_materi.universe, [30, 50, 70])
kesulitan_materi['tinggi'] = fuzz.trimf(kesulitan_materi.universe, [50, 100, 100])

# Variabel input 2: Frekuensi Konsultasi
frekuensi_konsultasi = ctrl.Antecedent(np.arange(0, 11, 1), 'frekuensi_konsultasi')
frekuensi_konsultasi['jarang'] = fuzz.trimf(frekuensi_konsultasi.universe, [0, 0, 5])
frekuensi_konsultasi['normal'] = fuzz.trimf(frekuensi_konsultasi.universe, [3, 5, 7])
frekuensi_konsultasi['sering'] = fuzz.trimf(frekuensi_konsultasi.universe, [5, 10, 10])

# Variabel input 3: Kualitas Istirahat
kualitas_istirahat = ctrl.Antecedent(np.arange(0, 101, 1), 'kualitas_istirahat')
kualitas_istirahat['buruk'] = fuzz.trimf(kualitas_istirahat.universe, [0, 0, 50])
kualitas_istirahat['cukup'] = fuzz.trimf(kualitas_istirahat.universe, [30, 50, 70])
kualitas_istirahat['baik'] = fuzz.trimf(kualitas_istirahat.universe, [50, 100, 100])

# Variabel output: Tingkat Stres
tingkat_stres = ctrl.Consequent(np.arange(0, 101, 1), 'tingkat_stres')
tingkat_stres['ringan'] = fuzz.trimf(tingkat_stres.universe, [0, 0, 50])
tingkat_stres['sedang'] = fuzz.trimf(tingkat_stres.universe, [30, 50, 70])
tingkat_stres['berat'] = fuzz.trimf(tingkat_stres.universe, [50, 100, 100])

# Visualisasi fungsi keanggotaan
kesulitan_materi.view()
plt.title('Tingkat Kesulitan Materi')
plt.show()

frekuensi_konsultasi.view()
plt.title('Frekuensi Konsultasi dengan Pembimbing')
plt.show()

kualitas_istirahat.view()
plt.title('Kualitas Istirahat Mahasiswa')
plt.show()

tingkat_stres.view()
plt.title('Tingkat Stres Mahasiswa')
plt.show()

# Membuat aturan fuzzy berdasarkan pengetahuan psikologis
rule1 = ctrl.Rule(kesulitan_materi['rendah'] & frekuensi_konsultasi['jarang'] & kualitas_istirahat['baik'], tingkat_stres['ringan'])
rule2 = ctrl.Rule(kesulitan_materi['sedang'] & frekuensi_konsultasi['normal'] & kualitas_istirahat['cukup'], tingkat_stres['sedang'])
rule3 = ctrl.Rule(kesulitan_materi['tinggi'] & frekuensi_konsultasi['sering'] & kualitas_istirahat['buruk'], tingkat_stres['berat'])
rule4 = ctrl.Rule(kesulitan_materi['tinggi'] | kualitas_istirahat['buruk'], tingkat_stres['sedang'])
rule5 = ctrl.Rule(frekuensi_konsultasi['sering'] & kualitas_istirahat['baik'], tingkat_stres['sedang'])
rule6 = ctrl.Rule(kesulitan_materi['rendah'] & frekuensi_konsultasi['jarang'] & kualitas_istirahat['buruk'], tingkat_stres['sedang'])
rule7 = ctrl.Rule(kesulitan_materi['tinggi'] & frekuensi_konsultasi['jarang'], tingkat_stres['berat'])
rule8 = ctrl.Rule(kesulitan_materi['sedang'] & kualitas_istirahat['baik'], tingkat_stres['ringan'])

# Membuat sistem kontrol
stres_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8])
diagnosa_stres = ctrl.ControlSystemSimulation(stres_ctrl)
# Fungsi untuk mendapatkan input user
def get_user_input():
    print("=== Sistem Diagnosa Tingkat Stres Mahasiswa ===")
    print("Silakan masukkan data berikut (0-100 atau 0-10):")

    try:
        km = float(input("Tingkat kesulitan materi (0-100): "))
        fk = float(input("Frekuensi konsultasi dengan pembimbing per minggu (0-10): "))
        ki = float(input("Kualitas istirahat (0-100): "))

        if not (0 <= km <= 100) or not (0 <= fk <= 10) or not (0 <= ki <= 100):
            raise ValueError("Input di luar range yang ditentukan")

        return km, fk, ki
    except ValueError as e:
        print(f"Input tidak valid: {e}")
        return None

# Mendapatkan input dan melakukan perhitungan
user_input = get_user_input()
if user_input:
    km, fk, ki = user_input

    # Set input ke sistem fuzzy
    diagnosa_stres.input['kesulitan_materi'] = km
    diagnosa_stres.input['frekuensi_konsultasi'] = fk
    diagnosa_stres.input['kualitas_istirahat'] = ki

    # Proses perhitungan
    diagnosa_stres.compute()

    # Menampilkan hasil
    print("\n=== Hasil Diagnosa ===")
    print(f"Tingkat stres: {diagnosa_stres.output['tingkat_stres']:.2f}")

    # Visualisasi hasil
    tingkat_stres.view(sim=diagnosa_stres)
    plt.title('Hasil Diagnosa Tingkat Stres')
    plt.show()

    # Interpretasi hasil
    stres_value = diagnosa_stres.output['tingkat_stres']
    if stres_value <= 40:
        print("Interpretasi: Stres Ringan")
        print("Rekomendasi: Pertahankan pola kerja dan istirahat yang baik")
    elif stres_value <= 70:
        print("Interpretasi: Stres Sedang")
        print("Rekomendasi: Perlu manajemen waktu yang lebih baik dan konsultasi rutin")
    else:
        print("Interpretasi: Stres Berat")
        print("Rekomendasi: Segera konsultasikan dengan pembimbing dan layanan konseling kampus")
else:
    print("Diagnosa tidak dapat dilanjutkan karena input tidak valid")
