# ============================================
# 1-MASHQ: Son musbat yoki manfiy ekanini aniqlash
# ============================================
print("=== 1-MASHQ: Musbat yoki manfiy ===")
son1 = float(input("Sonni kiriting: "))

if son1 > 0:
    print(f"{son1} — musbat son\n")
elif son1 < 0:
    print(f"{son1} — manfiy son\n")
else:
    print(f"{son1} — bu nol (na musbat, na manfiy)\n")


# ============================================
# 2-MASHQ: Son juft yoki toq ekanini aniqlash
# ============================================
print("=== 2-MASHQ: Juft yoki toq ===")
son2 = int(input("Butun son kiriting: "))

if son2 % 2 == 0:
    print(f"{son2} — juft son\n")
else:
    print(f"{son2} — toq son\n")


# ============================================
# 3-MASHQ: Ikki sondan kattasini chiqarish
# ============================================
print("=== 3-MASHQ: Kattasini topish ===")
a = float(input("Birinchi sonni kiriting: "))
b = float(input("Ikkinchi sonni kiriting: "))

if a > b:
    print(f"Katta son: {a}\n")
elif b > a:
    print(f"Katta son: {b}\n")
else:
    print(f"Ikkala son ham teng: {a}\n")


# ============================================
# 4-MASHQ: Yosh bo'yicha ruxsat tekshirish
# ============================================
print("=== 4-MASHQ: Yosh tekshirish ===")
yosh = int(input("Yoshingizni kiriting: "))

if yosh >= 18:
    print("Ruxsat berildi\n")
else:
    print("Ruxsat berilmadi\n")


# ============================================
# 5-MASHQ: Son 100 dan katta yoki kichik ekanini aniqlash
# ============================================
print("=== 5-MASHQ: 100 bilan solishtirish ===")
son3 = float(input("Sonni kiriting: "))

if son3 > 100:
    print(f"{son3} — 100 dan katta")
elif son3 < 100:
    print(f"{son3} — 100 dan kichik")
else:
    print(f"{son3} — aynan 100 ga teng")