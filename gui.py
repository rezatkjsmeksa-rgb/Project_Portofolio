import tkinter as tk
from tkinter import ttk, messagebox

from kalkulator import hitung_subnet, bagi_subnet, cek_ip
from database import buat_tabel, simpan, ambil_riwayat

# ----- Warna tema -----
BG = "#eef3f8"
KARTU = "#ffffff"
TEKS = "#14213d"
ABU = "#5b6b85"
BIRU = "#1f6feb"
BIRU_GELAP = "#1757b8"
ORANYE = "#f08c2e"


def buat_tombol(induk, teks, perintah):
    return tk.Button(
        induk,
        text=teks,
        command=perintah,
        font=("Segoe UI", 11, "bold"),
        bg=BIRU,
        fg="white",
        activebackground=BIRU_GELAP,
        activeforeground="white",
        relief="flat",
        padx=22,
        pady=7,
        cursor="hand2",
    )


def buat_input(induk, isi, lebar):
    kotak = tk.Entry(
        induk,
        font=("Consolas", 13),
        width=lebar,
        relief="solid",
        bd=1,
        justify="center",
    )
    kotak.insert(0, isi)
    return kotak


def buat_label_hasil(induk):
    return tk.Label(
        induk,
        text="Hasil akan tampil di sini",
        font=("Consolas", 11),
        bg=KARTU,
        fg=ABU,
        justify="left",
        anchor="w",
        padx=16,
        pady=12,
        relief="solid",
        bd=1,
    )


def hitung():
    ip = entry_ip.get()
    try:
        hasil = hitung_subnet(ip)
    except ValueError:
        messagebox.showerror("Error", "Input tidak valid, contoh: 192.168.1.0/24")
        return

    teks = (
        f"Network address : {hasil['network']}\n"
        f"Broadcast       : {hasil['broadcast']}\n"
        f"Subnet mask     : {hasil['mask']}\n"
        f"Range host      : {hasil['host_awal']} - {hasil['host_akhir']}\n"
        f"Jumlah host     : {hasil['jumlah_host']}"
    )
    label_hasil.config(text=teks, fg=TEKS)
    simpan(ip, hasil)
    muat_riwayat()


def bagi():
    ip = entry_ip_bagi.get()
    try:
        jumlah = int(entry_jumlah.get())
        daftar = bagi_subnet(ip, jumlah)
    except ValueError:
        messagebox.showerror("Error", "Cek IP dan jumlah subnet (minimal 2).")
        return

    teks = ""
    for nomor, subnet in enumerate(daftar, start=1):
        teks += f"{nomor}. {subnet} | host: {subnet.num_addresses - 2}\n"
    label_bagi.config(text=teks.strip(), fg=TEKS)


def cek():
    try:
        hasil = cek_ip(entry_ip_cek.get(), entry_jaringan_cek.get())
    except ValueError:
        messagebox.showerror("Error", "Cek penulisan IP dan jaringannya.")
        return

    if hasil["termasuk"]:
        status = "IP ini TERMASUK dalam jaringan tersebut."
    else:
        status = "IP ini TIDAK termasuk dalam jaringan tersebut."
    label_cek.config(text=f"{status}\nJenis IP : {hasil['jenis']}", fg=TEKS)


def muat_riwayat():
    kotak_riwayat.delete(0, tk.END)
    data = ambil_riwayat()
    if not data:
        kotak_riwayat.insert(tk.END, "Riwayat masih kosong.")
        return
    for waktu, ip, network, broadcast, host in data:
        kotak_riwayat.insert(tk.END, f"{waktu} | {ip} | host: {host}")


buat_tabel()

jendela = tk.Tk()
jendela.title("Subnet Calculator")
jendela.geometry("620x520")
jendela.configure(bg=BG)

# ----- Judul -----
tk.Label(jendela, text="Subnet Calculator", font=("Segoe UI", 20, "bold"), bg=BG, fg=TEKS).pack(pady=(14, 0))
tk.Label(jendela, text="Hitung dan bagi subnet jaringan dengan cepat", font=("Segoe UI", 10), bg=BG, fg=ABU).pack(pady=(0, 8))
tk.Frame(jendela, bg=ORANYE, height=3).pack(fill="x", padx=40)

# ----- Gaya tab -----
gaya = ttk.Style()
gaya.theme_use("clam")
gaya.configure("TNotebook", background=BG, borderwidth=0)
gaya.configure("TNotebook.Tab", font=("Segoe UI", 10, "bold"), padding=(18, 8), background="#d5e0ee", foreground=TEKS)
gaya.map("TNotebook.Tab", background=[("selected", BIRU)], foreground=[("selected", "white")])

tab = ttk.Notebook(jendela)
tab.pack(fill="both", expand=True, padx=14, pady=12)

# ----- Tab 1: Hitung -----
frame_hitung = tk.Frame(tab, bg=BG)
tab.add(frame_hitung, text="Hitung")

tk.Label(frame_hitung, text="Masukkan IP dan prefix", font=("Segoe UI", 11), bg=BG, fg=TEKS).pack(pady=(18, 6))
entry_ip = buat_input(frame_hitung, "192.168.1.0/24", 24)
entry_ip.pack(ipady=5)
buat_tombol(frame_hitung, "Hitung", hitung).pack(pady=14)
label_hasil = buat_label_hasil(frame_hitung)
label_hasil.pack(fill="x", padx=30)

# ----- Tab 2: Bagi Subnet -----
frame_bagi = tk.Frame(tab, bg=BG)
tab.add(frame_bagi, text="Bagi Subnet")

tk.Label(frame_bagi, text="Masukkan IP dan prefix", font=("Segoe UI", 11), bg=BG, fg=TEKS).pack(pady=(18, 6))
entry_ip_bagi = buat_input(frame_bagi, "192.168.1.0/24", 24)
entry_ip_bagi.pack(ipady=5)
tk.Label(frame_bagi, text="Dibagi jadi berapa subnet?", font=("Segoe UI", 11), bg=BG, fg=TEKS).pack(pady=(12, 6))
entry_jumlah = buat_input(frame_bagi, "4", 8)
entry_jumlah.pack(ipady=5)
buat_tombol(frame_bagi, "Bagi", bagi).pack(pady=14)
label_bagi = buat_label_hasil(frame_bagi)
label_bagi.pack(fill="x", padx=30)

# ----- Tab 3: Riwayat -----
frame_riwayat = tk.Frame(tab, bg=BG)
tab.add(frame_riwayat, text="Riwayat")

buat_tombol(frame_riwayat, "Muat Ulang", muat_riwayat).pack(pady=14)
kotak_riwayat = tk.Listbox(
    frame_riwayat,
    font=("Consolas", 10),
    bg=KARTU,
    fg=TEKS,
    relief="solid",
    bd=1,
    highlightthickness=0,
    selectbackground=BIRU,
    height=14,
)
kotak_riwayat.pack(fill="both", expand=True, padx=20, pady=(0, 14))

# ----- Tab 4: Cek IP -----
frame_cek = tk.Frame(tab, bg=BG)
tab.add(frame_cek, text="Cek IP")

tk.Label(frame_cek, text="Alamat IP yang dicek", font=("Segoe UI", 11), bg=BG, fg=TEKS).pack(pady=(18, 6))
entry_ip_cek = buat_input(frame_cek, "192.168.1.25", 24)
entry_ip_cek.pack(ipady=5)
tk.Label(frame_cek, text="Jaringan (IP/prefix)", font=("Segoe UI", 11), bg=BG, fg=TEKS).pack(pady=(12, 6))
entry_jaringan_cek = buat_input(frame_cek, "192.168.1.0/26", 24)
entry_jaringan_cek.pack(ipady=5)
buat_tombol(frame_cek, "Cek", cek).pack(pady=14)
label_cek = buat_label_hasil(frame_cek)
label_cek.pack(fill="x", padx=30)

muat_riwayat()
jendela.mainloop()