from data.database import cari_siswa_by_id, BayarJajan, BayarParkir

def tampilkan_menu_utama():
    print("\n=======================================")
    print("      DSQPAY - DIGITAL SCHOOL PAY      ")
    print("   Tap & Go: Jajan & Parkir Tanpa Antre ")
    print("=======================================")
    print("1. Login Siswa (Scan QR / Input ID)")
    print("2. Keluar Aplikasi")
    print("=======================================")

def tampilkan_menu_transaksi(siswa):
    print(f"\nSelamat Datang, {siswa.nama}! [{siswa.id_card}]")
    print("=== MENU TRANSAKSI DSQPAY ===")
    print("1. Cek Saldo & Profil Siswa (Fitur 1)")
    print("2. Bayar Jajan fmart/Koperasi (Fitur 2)")
    print("3. Bayar Parkir Otomatis - Rp2.000 (Fitur 3)")
    print("4. Logout / Ganti Akun")
    print("=============================")

def main():
    # Instansiasi objek pembayaran (polymorphism)
    layanan_jajan = BayarJajan()
    layanan_parkir = BayarParkir()

    while True:
        tampilkan_menu_utama()
        pilihan = input("Pilih Menu (1-2): ")
        if pilihan == "1":
            id_input = input("Scan QR / Masukkan ID Kartu Pelajar (Contoh: DSQ001): ")
            siswa_aktif = cari_siswa_by_id(id_input)
            if siswa_aktif:
                while True:
                    tampilkan_menu_transaksi(siswa_aktif)
                    opsi = input("Pilih Fitur (1-4): ")
                    if opsi == "1":
                        print("\n=== 👤 PROFIL & SALDO SISWA ===")
                        print(f"Nama Pelajar : {siswa_aktif.nama}")
                        print(f"ID Digital   : {siswa_aktif.id_card}")
                        print(f"Sisa Saldo   : Rp {siswa_aktif.get_saldo():,}")
                        print("=================================")
                    elif opsi == "2":
                        print("\n--- 🛍️ KASIR FMART / KOPERASI ---")
                        try:
                            nominal = int(input("Masukkan Total Nominal Belanja (Rp): "))
                            # polymorphism pembayaran jajan
                            layanan_jajan.proses_bayar(siswa_aktif, nominal)
                        except ValueError:
                            print("❌ Input salah! Nominal harus berupa angka bulat.")
                    elif opsi == "3":
                        print("\n--- 🚗 GERBANG PARKIR OTOMATIS ---")
                        print("Memindai QR Reader Parkir...")
                        # polymorphism pembayaran parkir (Tarif otomatis flat)
                        layanan_parkir.proses_bayar(siswa_aktif)
                    elif opsi == "4":
                        print(f"👋 Berhasil keluar dari akun {siswa_aktif.nama}.")
                        break
                    else:
                        print("❌ Pilihan fitur tidak tersedia!")
            else:
                print("❌ Data kartu pelajar tidak ditemukan! Coba lagi.")

        elif pilihan == "2":
            print("\nTerima kasih telah menggunakan DSQpay! Tap dan Go! 👋")
            break
        else:
            print("❌ Pilihan menu tidak valid!")

if __name__ == "__main__":
    main()