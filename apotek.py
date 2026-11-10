
print("=== APOTEK SEHAT ===")

daftar_beli = []
total_semua = 0

while True:
    print("\nDAFTAR OBAT")
    print("1. OBH Combi - 13000")
    print("2. Siladex - 25000")
    print("3. Paracetamol 500 mg - 15000")
    print("4. Konidin - 10000")
    print("5. Betadine - 20000")
    print("6. Sanmol Syrup - 23000")
    print("7. Promag - 13000")
    print("8. Tolak Angin - 4000")
    print("9. Diapet - 6000")
    print("10. Insto - 17000")

    pilihan = int(input("\nPilih obat (1-10): "))
    jumlah = int(input("Jumlah obat: "))

    if pilihan == 1:
        nama = "OBH Combi"
        harga = 13000
    elif pilihan == 2:
        nama = "Siladex"
        harga = 25000
    elif pilihan == 3:
        nama = "Paracetamol 500 mg"
        harga = 15000
    elif pilihan == 4:
        nama = "Konidin"
        harga = 10000
    elif pilihan == 5:
        nama = "Betadine"
        harga = 20000
    elif pilihan == 6:
        nama = "Sanmol Syrup"
        harga = 23000
    elif pilihan == 7:
        nama = "Promag"
        harga = 13000
    elif pilihan == 8:
        nama = "Tolak Angin"
        harga = 4000
    elif pilihan == 9:
        nama = "Diapet"
        harga = 6000
    elif pilihan == 10:
        nama = "Insto"
        harga = 17000
    else:
        nama = ""
        harga = 0

    if pilihan >= 1 and pilihan <= 10 and jumlah >= 1:
        subtotal = harga * jumlah

        daftar_beli.append([nama, jumlah, harga, subtotal])
        total_semua = total_semua + subtotal

        print("Obat berhasil ditambahkan!")
    else:
        print("Pilihan atau jumlah tidak valid")

    tambah = input("\nIngin membeli lagi? (ya/tidak): ")

    if tambah.lower() != "ya":
        break

# STRUK AKHIR
print("\n===== STRUK PEMBELIAN =====")

for data in daftar_beli:
    print("Nama obat:", data[0])
    print("Jumlah:", data[1])
    print("Harga:", data[2])
    print("Subtotal: Rp", data[3])
    print("----------------------")

print("Total belanja: Rp", total_semua)

if total_semua >= 50000:
    diskon = total_semua * 5 / 100
    print("Diskon 5%: Rp", int(diskon))
else:
    diskon = 0
    print("Diskon: Rp 0")

bayar = total_semua - diskon

print("Total bayar: Rp", int(bayar))
print("==========================")
print("Terima kasih telah berbelanja!")