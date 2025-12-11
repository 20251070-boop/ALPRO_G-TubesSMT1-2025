# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ====== PROYEK TUGAS BESAR ALPRO ======
# NAMA       : Esti Nur Khazanah
# NIM        : 20251013
# KELAS      : G
# MATKUL     : Algoritme dan Pemrograman
# JUDUL TUBES: Pengelolaan Data Penjualan Obat Rumput
# ======================================

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# === PENGELOLAAN DATA PENJUALAN OBAT RUMPUT ===

def create(data):
    #Menerima input dari user dan menyimpan / menambahkan ke list data
    print("\n=== Tambah Data Penjualan Obat Rumput ===")
    try:
        ID_OR = int(input(" ID Obat Rumput: "))
        tanggal_pembelian = input(" Tanggal Pembelian (DD-MM-YYYY): ")
        nama_OR = input(" Masukkan Nama Obat Rumput: ")
        harga_OR_RP = int(input(" Masukkan Harga Obat: "))
        jumlah_PB = int(input(" Masukkan Jumlah Pembelian: "))
        total = harga_OR_RP * jumlah_PB
        data.append([ID_OR, nama_OR, tanggal_pembelian, harga_OR_RP, jumlah_PB, total])
        print(f"Data '{nama_OR}' berhasil ditambahkan!")
    except ValueError:
        print("Input tidak valid! Pastikan harga dan jumlah berupa angka.")
    return data

def read(data):
    #Menampilkan data yang tersimpan secara rapi dan terstruktur
    #Dapat memberikan pilihan user apakah ingin ditampilkan semua (sorted)
    #atau mencari dengan pilihan dari user
    print("\n=== Data Penjualan Obat Rumput ===")

    if len(data) == 0:
        print("Belum ada data penjualan.")
        return

    print("\n1. Tampilkan Semua Data")
    print("2. Tampilkan Berdasarkan Tanggal Pembelian")
    print("3. Tampilkan Berdasarkan Urutan Harga")
    print("4. Cari Data Berdasarkan Nama")
    print("5. Cari Data Berdasarkan ID")
    print("6. Kembali ke Menu Utama")

    pilih = input("Pilih: ")

    # MENAMPILKAN SEMUA DATA OBAT RUMPUT
    if pilih == "1":
        print("\n===>  Data Penjualan Obat Rumput  <===")
        print(f"{'ID':<4} {'TP':<10} {'Nama Obat':<15} {'Harga':<10} {'JP':^8} {'Total':<10}")
        print("-" * 55)

        for d in data:
            print(f"{d[0]:<4} {d[1]:<10} {d[2]:<15} {d[3]:<10} {d[4]:^8} {d[5]:<10}")


    # SORTING
    # > Menampilkan Obat Rumput Berdasarkan Tanggal Pembelian <
    elif pilih == "2":
        print("\n1. Tanggal Terbaru")
        print("2. Tanggal Terlama")
        pilih_TP = input("Pilih: ").upper()

        try:
            if pilih_TP == "1":
                urutan_data = sorted(data, key=lambda x: x[2].split("-")[2] + x[2].split("-")[1] + x[2].split("-")[0], reverse=True)
                print("\n=== Tanggal Terbaru ===") 

            elif pilih_TP == "2":
                urutan_data = sorted(data, key=lambda x: x[2].split("-")[2] + x[2].split("-")[1] + x[2].split("-")[0])
                print("\n=== Tanggal Terlama ===")

            else:
                print("Pilihan tidak valid.")
                return

            print(f"\n{'ID':<4} {'Nama Obat':<15} {'TP':<15} {'Harga':<10} {'JP':<8} {'Total':<10}")
            print("-" * 70)

            for d in urutan_data:
                print(f"{d[0]:<4} {d[1]:<15} {d[2]:<15} {d[3]:<10} {d[4]:<8} {d[5]:<10}")
        except:
            print("Format tanggal tidak valid!")


    # > Menampilkan Obat Rumput Berdasarkan Harga <
    elif pilih == "3":
        print("\n1. Harga Tertinggi ")
        print("2. Harga Terendah ")
        pilih_harga = input("Pilih : ").upper()

        if pilih_harga == "1":
            urutan_data = sorted(data, key=lambda x: x[3], reverse=True)
            print("\n=== Harga Tertinggi ke Terendah ===")

        elif pilih_harga == "2":
            urutan_data = sorted(data, key=lambda x: x[3])
            print("\n=== Harga Terendah ke Tertinggi ===")
        else:
            print("Pilihan tidak valid.")
            return

        for d in urutan_data:
            print(f" ID:{d[0]} | Obat:{d[1]} | Harga:{d[2]} | TP:{d[3]} | JP:{d[4]} | Total:{d[5]}")


    # SEARCHING
    # > Mencari Obat Rumput Berdasarkan Nama <
    elif pilih == "4":
        cari = input("Masukkan Nama Obat: ").lower()
        ditemukan = False

        for d in data:
            if d[1].lower() == cari:
                print(f"\nDitemukan! ID:{d[0]} | TP:{d[2]} | Harga:{d[3]} | JP:{d[4]} | Total:{d[5]}")
                ditemukan = True

        if not ditemukan:
            print("Data tidak ditemukan.")


    # > Mencari Obat Rumput Berdasarkan ID <
    elif pilih == "5":
        try:
            cari = int(input("Masukkan ID Obat: "))
            ditemukan = False

            for d in data:
                if d[0] == cari:
                    print(f"\nDitemukan! Obat:{d[1]} | TP:{d[2]} | Harga:{d[3]} | JP:{d[4]} | Total:{d[5]}")
                    ditemukan = True

            if not ditemukan:
                print("Data tidak ditemukan.")
        except:
            print("ID harus berupa angka!")


    elif pilih == "6":
        return

    else:
        print("Pilihan tidak valid.")

def update(data):
    #Mengupdate data di list data sesuai data baru dari input user
    print("\n=== Update Data Penjualan Obat Rumput ===")

    if len(data) == 0:
        print("Belum ada data yang diupdate.")
        return data

    print("\nDaftar Data:")
    for i, d in enumerate(data):
        print(f" ID:{d[0]} | Nama:{d[1]} | TP:{d[2]} | Harga:{d[3]} | JP:{d[4]} | Total:{d[5]}")

    try:
        New = int(input("\nMasukkan ID data yang ingin diubah: ")) - 1

        if 0 <= New < len(data):
            print(f"\nMengubah data '{data[New][1]}'")

            nama_baru = input("Nama Obat Rumput Baru: ")
            TP_baru = input("Tanggal Pembelian Obat Rumput Baru: ")
            harga_baru = int(input("Harga Obat Rumput Baru: "))
            JP_baru = int(input("Jumlah Pembelian Obat Rumput Baru: "))
            total_baru = harga_baru * JP_baru

            data[New][1] = nama_baru
            data[New][2] = TP_baru
            data[New][3] = harga_baru
            data[New][4] = JP_baru
            data[New][5] = total_baru

            print("Data berhasil diperbarui!")
        else:
            print("Nomor data tidak valid.")

    except ValueError:
        print("Input harus berupa angka!")
    return data

def delete(data):
    #Menghapus data pilihan user dari list data
    print("\n=== Hapus Data Penjualan Obat Rumput ===")

    if len(data) == 0:
        print("Belum ada data yang dapat dihapus.")
        return data

    print("\nDaftar Data:")
    for i, d in enumerate(data):
        print(f" {i} ID:{d[0]} | Nama:{d[1]} | TP:{d[2]} | Harga:{d[3]} | JP:{d[4]} | Total:{d[5]}")

    try:
        hapus_data = int(input("\nMasukkan ID data yang ingin dihapus: "))
        index = next((i for i, d in enumerate(data) if d[0] == hapus_data), None)

        if index is not None:
            konfirmasi = input(f"Yakin ingin menghapus data dengan ID {data[index][0]}? : ").lower()
            if konfirmasi == "ya":
                data.pop(index)
                print("Data berhasil dihapus!")
            else:
                print("Penghapusan dibatalkan.")
        else:
            print("Nomor ID tidak valid / tidak ditemukan.")

    except ValueError:
        print("Input harus berupa angka!")

def menuUtama(): #contoh fungsi menuUtama
    print("=============================================")
    print("=== Pengelolaan Data Penjulan Obat Rumput ===")
    print("===          by Esti Nur Khazanah         ===")
    print("=============================================")
    print("1. Tambah Pesanan")
    print("2. Lihat Pesanan")
    print("3. Edit Pesanan")
    print("4. Hapus Pesanan")
    print("5. Keluar")
    try:
        pilihan = int(input("Masukkan pilihan [1 - 5]: "))
        if pilihan < 1 or pilihan > 5:
            print("Pilihan hanya antara 1 sampai 5. Silakan coba lagi.")
            input()
        else:
            return pilihan
    except ValueError:
        print("Input harus berupa angka. Silakan coba lagi.")


##### PROGRAM UTAMA #####

pilihan = 0
data = [[101, "Gempur", "03-01-2025", 70000, 2, 140000],
        [102, "Jifos", "05-01-2025", 50000, 1, 50000],
        [103, "Tamaris", "10-01-2025", 50000, 6, 300000],
        [104, "Bablas", "25-01-2025", 60000, 4, 240000],
        [105, "Rambo Gol", "08-02-2025", 70000, 3, 210000],
        [201, "Paraken", "07-01-2025", 50000, 8, 400000],
        [202, "Helitop", "18-01-2025", 45000, 2, 90000],
        [203, "Gramaxone", "14-02-2025", 75000, 4, 300000],
        [204, "Krestara", "27-02-2025", 40000, 10, 400000],
        [205, "Noxone", "05-03-2025", 55000, 7, 385000]]

while (pilihan != 5):
    pilihan = menuUtama()
    if (pilihan == 1):
        data = create(data)
    elif (pilihan == 2):
        read(data)
        input("Kembali tekan ENTER..")
    elif (pilihan == 3):
        data = update(data)
    elif (pilihan == 4):
        data = delete(data)
print("Terima kasih..!")
