def matriks_transpose(A):
    hasil = []

    for j in range(len(A[0])):
        baris = []
        for i in range(len(A)):
            baris.append(A[i][j])
        hasil.append(baris)
    return hasil

def pengurangan_matriks(A, B):
    hasil = []

    for i in range(len(A)):
        baris = []
        for j in range(len(A[0])):
            baris.append(A[i][j] - B[i][j])
        hasil.append(baris)
    return hasil
