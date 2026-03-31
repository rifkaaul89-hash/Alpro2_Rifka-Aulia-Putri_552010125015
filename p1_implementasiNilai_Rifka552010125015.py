#Latihan 2
#Implementasi Nilai Akhir Mahasiswa

tugas = float(input("Nilai Tugas: "))
uts = float(input("Nilai UTS: "))
uas = float(input("Nilai UAS: "))

if 0 <= tugas <= 100 and 0 <= uas <= 100:
    nilai_akhir = (0.3 * tugas) + (0.3 * uts) + (0.4 * uas)
    print("Nilai akhir:", nilai_akhir)
else:
    print("iput tidak valid!")
