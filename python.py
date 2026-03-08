# Cari il
current_year = 2026

# İstifadəçidən məlumatların alınması
name = input("Adınızı daxil edin: ")
age = int(input("Yaşınızı daxil edin: "))
weight = float(input("Çəkinizi daxil edin (kg): "))
height = float(input("Boyunuzu daxil edin (metr): "))
hourly_salary = float(input("Saatlıq maaşı daxil edin: "))
worked_hours = float(input("İşlədiyiniz saat sayını daxil edin: "))

# Doğum ilinin hesablanması
birth_year = current_year - age

# BMI hesablanması
bmi = weight / (height * height)

# Ümumi maaşın hesablanması
total_salary = hourly_salary * worked_hours

# Nəticələrin çapı
print("\n--- Nəticələr ---")
print("Ad:", name)
print("Yaş:", age)
print("Doğum ili:", birth_year)
print("BMI nəticəsi:", round(bmi, 2))
print("Ümumi maaş:", total_salary)