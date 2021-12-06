"""
program perulangan dengan while
"""

jumlah_buku = 10
print("perintah ibu 'baca seluruh buku'")

jumlah_buku_yang_sudah_di_baca = 0
print(f"jumlah_buku_yang_sudah_di_baca {jumlah_buku_yang_sudah_di_baca}")

while jumlah_buku_yang_sudah_di_baca < jumlah_buku:
    jumlah_buku_yang_sudah_di_baca = jumlah_buku_yang_sudah_di_baca + 1
    print(f"buku ke {jumlah_buku_yang_sudah_di_baca} sudah di baca")

print(f"jumlah_buku_yang_sudah_di_baca {jumlah_buku_yang_sudah_di_baca}")

