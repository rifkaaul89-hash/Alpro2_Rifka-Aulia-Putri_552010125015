#Latihan mandiri (challenge)
#Konverensi Suhu

# Program Konversi Suhu

# Input
celcius = float(input("Masukkan suhu dalam Celcius: "))

# Proses konversi
fahrenheit = (9/5 * celcius) + 32
kelvin = celcius + 273.15

# Output (dibulatkan 2 angka di belakang koma)
print("Suhu dalam Fahrenheit:", round(fahrenheit, 2))
print("Suhu dalam Kelvin:", round(kelvin, 2))