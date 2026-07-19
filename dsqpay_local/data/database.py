# data/database.py
# array of Objects Python (Local Storage)
from abc import ABC, abstractmethod

class MetodePembayaran(ABC):
    @abstractmethod
    def proses_bayar(self, siswa, nominal):
        pass

class BayarJajan(MetodePembayaran):
    def proses_bayar(self, siswa, nominal):
        if nominal <= 0:
            print("❌ Nominal jajan tidak valid!")
            return False
        
        # akses saldo lewat method di kelas Siswa karena enkapsulasi
        if siswa.get_saldo() >= nominal:
            siswa.kurangi_saldo(nominal)
            print(f"✅ [fmart/Koperasi] Transaksi Berhasil! Dipotong: Rp {nominal:,}")
            return True
        else:
            print(f"❌ Transaksi Gagal! Saldo tidak mencukupi. (Kurang: Rp {nominal - siswa.get_saldo():,})")
            return False

class BayarParkir(MetodePembayaran):
    def proses_bayar(self, siswa, nominal=2000):
        # Parkir menggunakan tarif flat Rp 2.000 (Polymorphism)
        if siswa.get_saldo() >= nominal:
            siswa.kurangi_saldo(nominal)
            print(f"✅ [Parkir Sekolah] Transaksi Berhasil! Dipotong: Rp {nominal:,} (Tarif Flat)")
            return True
        else:
            print(f"❌ Transaksi Gagal! Saldo tidak cukup untuk parkir. (Kurang: Rp {nominal - siswa.get_saldo():,})")
            return False

class Siswa:
    def __init__(self, nama, id_card, saldo_awal):
        self.nama = nama
        self.id_card = id_card
        # Encapsulation: Saldo bersifat private (__saldo) agar aman tidak bisa diubah langsung dari luar
        self.__saldo = saldo_awal 

    # Getter untuk mendapatkan saldo secara aman
    def get_saldo(self):
        return self.__saldo

    # Method internal untuk mengubah saldo (enkapsulasi kontrol)
    def kurangi_saldo(self, jumlah):
        if jumlah > 0 and self.__saldo >= jumlah:
            self.__saldo -= jumlah

# Array of Objects untuk mensimulasikan data akun siswa di sekolah
db_siswa = [
    Siswa("Meylani", "DSQ001", 50000),
    Siswa("Husnah", "DSQ002", 75000),
    Siswa("Celine", "DSQ003", 15000),
    Siswa("Sipa", "DSQ004", 1500), # Saldo kurang dari tarif parkir untuk testing
]

def cari_siswa_by_id(id_card):
    for siswa in db_siswa:
        if siswa.id_card.upper() == id_card.upper():
            return siswa
    return None
