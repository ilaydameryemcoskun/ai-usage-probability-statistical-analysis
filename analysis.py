import math
import statistics

print("MAT 203 - Olasilik ve Istatistik Analizi")


veri_2024 = [45.3, 46.3, 42.8, 22.2, 32.2, 31.5, 42.8]
veri_2025 = [46.5, 41.1, 40.0, 13.6, 22.6, 33.7, 41.0]


ortalama_2024 = statistics.mean(veri_2024)
ortalama_2025 = statistics.mean(veri_2025)

std_2024 = statistics.stdev(veri_2024)
std_2025 = statistics.stdev(veri_2025)

print("\n--- Temel Istatistikler ---")
print("2024 Ortalama:", ortalama_2024)
print("2025 Ortalama:", ortalama_2025)
print("2024 Std Sapma:", std_2024)
print("2025 Std Sapma:", std_2025)


z = (40 - ortalama_2025) / std_2025
olasilik = 1 - (0.5 * (1 + math.erf(z / math.sqrt(2))))

print("\n--- Olasilik Analizi ---")
print("2025 icin P(X > 40):", olasilik)


farklar = []
for i in range(len(veri_2024)):
    farklar.append(veri_2025[i] - veri_2024[i])

ortalama_fark = statistics.mean(farklar)
std_fark = statistics.stdev(farklar)
n = len(farklar)

t_degeri = ortalama_fark / (std_fark / math.sqrt(n))

print("\n--- Hipotez Testi ---")
print("t-degeri:", t_degeri)


z_degeri = 1.96
hata_payi = z_degeri * (std_2025 / math.sqrt(len(veri_2025)))

alt_sinir = ortalama_2025 - hata_payi
ust_sinir = ortalama_2025 + hata_payi

print("\n--- %95 Guven Araligi (2025) ---")
print("Alt Sinir:", alt_sinir)
print("Ust Sinir:", ust_sinir)
print("\nOrtalamanın (27.8), Medyandan (21.1) büyük olması, verinin sağa çarpık olduğunu gösterir.")
print("\nAnaliz Basariyla Tamamlandi.")