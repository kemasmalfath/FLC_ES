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