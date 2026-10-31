import sqlite3

NAMA_DB = "riwayat.db"


def buat_tabel():
    koneksi = sqlite3.connect(NAMA_DB)
    kursor = koneksi.cursor()
    kursor.execute(
        """
        CREATE TABLE IF NOT EXISTS riwayat (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            input TEXT,
            network TEXT,
            broadcast TEXT,
            jumlah_host INTEGER,
            waktu TEXT DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    koneksi.commit()
    koneksi.close()


def simpan(teks_input, hasil):
    koneksi = sqlite3.connect(NAMA_DB)
    kursor = koneksi.cursor()
    kursor.execute(
        "INSERT INTO riwayat (input, network, broadcast, jumlah_host) VALUES (?, ?, ?, ?)",
        (teks_input, str(hasil["network"]), str(hasil["broadcast"]), hasil["jumlah_host"]),
    )
    koneksi.commit()
    koneksi.close()


def ambil_riwayat():
    koneksi = sqlite3.connect(NAMA_DB)
    kursor = koneksi.cursor()
    kursor.execute(
        "SELECT waktu, input, network, broadcast, jumlah_host FROM riwayat ORDER BY id DESC LIMIT 10"
    )
    data = kursor.fetchall()
    koneksi.close()
    return data


def hapus_semua():
    koneksi = sqlite3.connect(NAMA_DB)
    kursor = koneksi.cursor()
    kursor.execute("DELETE FROM riwayat")
    koneksi.commit()
    koneksi.close()