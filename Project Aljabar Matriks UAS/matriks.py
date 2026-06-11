import Davina026 as dv

A = [[3, 6, 8], [7, 8, 4], [6, 9, 3]]
B = [[2, 3, 4], [4, 5, 6], [7, 3, 1]]

hasil = dv.matriks_transpose(A)
hasil_pengurangan = dv.pengurangan_matriks(A, B)

print("Matriks Awal:")
for baris in A:
    print(baris)

print("Hasil Transpose:")
for baris in hasil:
    print(baris)

print("Hasil Pengurangan Matriks:")
for baris in hasil_pengurangan:
    print(baris)