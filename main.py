# ============================================
son = int(input("Sonni kiriting: "))

if son % 2 == 0:
    print(f"{son} - juft son")
else:
    print(f"{son} - toq son")

print("-" * 40)
# ============================================
son2 = float(input("Sonni kiriting: "))

if son2 > 0:
    print(f"{son2} - musbat son")
elif son2 < 0:
    print(f"{son2} - manfiy son")
else:
    print("Bu son nolga teng")

print("-" * 40)
# ============================================
a = float(input("1-sonni kiriting: "))
b = float(input("2-sonni kiriting: "))
c = float(input("3-sonni kiriting: "))

if a >= b and a >= c:
    eng_katta = a
elif b >= a and b >= c:
    eng_katta = b
else:
    eng_katta = c

print(f"Eng katta son: {eng_katta}")

print("-" * 40)
# ============================================
son3 = int(input("Sonni kiriting: "))

if son3 % 5 == 0:
    print(f"{son3} soni 5 ga qoldiqsiz bo'linadi")
else:
    print(f"{son3} soni 5 ga bo'linmaydi")

print("-" * 40)
# ==========================================
ball = float(input("Ballni kiriting (0-100): "))

if ball >= 90:
    baho = "A"
elif ball >= 80:
    baho = "B"
elif ball >= 70:
    baho = "C"
elif ball >= 60:
    baho = "D"
else:
    baho = "F"

print(f"Sizning bahoyingiz: {baho}")

print("-" * 40)
# ============================================
yil = int(input("Yilni kiriting: "))

if (yil % 4 == 0 and yil % 100 != 0) or (yil % 400 == 0):
    print(f"{yil} - kabisa yil")
else:
    print(f"{yil} - oddiy yil")

print("-" * 40)
# ============================================
harorat = float(input("Haroratni kiriting (Celsiy darajada): "))

if harorat <= 0:
    holat = "Muzlash"
elif harorat <= 15:
    holat = "Sovuq"
elif harorat <= 25:
    holat = "Iliq"
else:
    holat = "Issiq"

print(f"Harorat holati: {holat}")