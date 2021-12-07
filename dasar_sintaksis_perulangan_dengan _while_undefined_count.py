"""
program perulangan dengan while sampai paham
"""

jumlah_buku = 10
print("perintah ibu 'baca seluruh buku'")
total_jumlah_baca = 0

jumlah_buku_yang_sudah_di_baca_dan_dipahami = 0
print(f"jumlah_buku_yang_sudah_di_baca dan dipahami {jumlah_buku_yang_sudah_di_baca_dan_dipahami}")

while total_jumlah_baca < jumlah_buku * 2:
    total_jumlah_baca = total_jumlah_baca + 1
    if jumlah_buku_yang_sudah_di_baca_dan_dipahami == 9:
        print(f"buku ke {jumlah_buku_yang_sudah_di_baca_dan_dipahami + 1} belum paham")
    else:
        jumlah_buku_yang_sudah_di_baca_dan_dipahami = jumlah_buku_yang_sudah_di_baca_dan_dipahami + 1
        print(f"buku ke {jumlah_buku_yang_sudah_di_baca_dan_dipahami} sudah di baca dan dipahami")

print(f"jumlah_buku_yang_sudah_di_baca dan dipahami {jumlah_buku_yang_sudah_di_baca_dan_dipahami}")

