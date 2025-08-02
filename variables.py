# Detaylı Maaş Hesaplama Sistemi
# Kullanıcıdan çalışan bilgileri alınır, vergi oranı ve maaş türü seçilir.
# Sonuçlar görsel olarak zengin bir tablo ile ekrana yazdırılır.

# # Çalışanları tutacak liste
# calisanlar = []

# # --- Çalışan Ekleme ---
# print("="*40)
# print("👥 ÇALIŞAN EKLEME MODÜLÜ 👥".center(40))
# print("="*40)
# while True:
#     isim = input("Çalışan ismi (çıkmak için ENTER): ")
#     if isim == "":
#         break
#     try:
#         maas = float(input(f"{isim} için brüt maaşı girin: "))
#     except ValueError:
#         print("Hatalı maaş girdisi! Lütfen tekrar deneyin.")
#         continue
#     calisanlar.append({"isim": isim, "brut": maas})
#     print(f"✅ {isim} eklendi!\n")

# if not calisanlar:
#     print("Hiç çalışan eklenmedi. Program sonlandırılıyor.")
#     exit()

# # --- Vergi Oranı Seçimi ---
# print("-"*40)
# print("💸 VERGİ ORANI SEÇİMİ 💸".center(40))
# print("-"*40)
# print("1) %15 (0.15)\n2) %20 (0.20)\n3) %27 (0.27)\n4) Özel oran gir")
# secim = input("Seçiminiz (1-4): ")
# if secim == "1":
#     vergi = 0.15
# elif secim == "2":
#     vergi = 0.20
# elif secim == "3":
#     vergi = 0.27
# elif secim == "4":
#     try:
#         vergi = float(input("Vergi oranını ondalık girin (örn: 0.18): "))
#     except ValueError:
#         print("Hatalı giriş! Varsayılan 0.27 kullanıldı.")
#         vergi = 0.27
# else:
#     print("Geçersiz seçim! Varsayılan 0.27 kullanıldı.")
#     vergi = 0.27

# # --- Maaş Türü Seçimi ---
# print("-"*40)
# print("💼 MAAŞ TÜRÜ SEÇİMİ 💼".center(40))
# print("-"*40)
# print("1) Sadece brüt maaş göster\n2) Sadece net maaş göster\n3) Her ikisini göster")
# maas_turu = input("Seçiminiz (1-3): ")

# # --- Hesaplama ve Görsel Çıktı ---
# def net_maas(brut, vergi):
#     """Brüt maaştan net maaşı hesaplar."""
#     return brut - (brut * vergi)

# print("\n" + "*"*50)
# print("📊 ÇALIŞAN MAAŞ TABLOSU 📊".center(50))
# print("*"*50)
# print(f"{'İSİM':<15} | {'BRÜT (₺)':>12} | {'NET (₺)':>12}")
# print("-"*50)
# for c in calisanlar:
#     brut = c["brut"]
#     net = net_maas(brut, vergi)
#     if maas_turu == "1":
#         print(f"{c['isim']:<15} | {brut:>12.2f} | {'-':>12}")
#     elif maas_turu == "2":
#         print(f"{c['isim']:<15} | {'-':>12} | {net:>12.2f}")
#     else:
#         print(f"{c['isim']:<15} | {brut:>12.2f} | {net:>12.2f}")
# print("*"*50)
# print(f"Vergi oranı: %{vergi*100:.0f}")
# print("*"*50)
# print("✨ Hesaplama tamamlandı! ✨")


