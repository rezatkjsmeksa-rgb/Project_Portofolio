import tkinter as tk
from tkinter import ttk, messagebox

from kalkulator import hitung_subnet, bagi_subnet
from database import buat_tabel, simpan, ambil_riwayat


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
    label_hasil.config(text=teks)
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
    label_bagi.config(text=teks)


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
jendela.geometry("560x420")

tab = ttk.Notebook(jendela)
tab.pack(fill="both", expand=True, padx=10, pady=10)

# ----- Tab 1: Hitung -----
frame_hitung = tk.Frame(tab)
tab.add(frame_hitung, text="Hitung")

tk.Label(frame_hitung, text="Masukkan IP dan prefix:", font=("Arial", 11)).pack(pady=(15, 5))
entry_ip = tk.Entry(frame_hitung, font=("Arial", 12), width=25)
entry_ip.insert(0, "192.168.1.0/24")
entry_ip.pack()
tk.Button(frame_hitung, text="Hitung", font=("Arial", 11), command=hitung).pack(pady=10)
label_hasil = tk.Label(frame_hitung, text="", font=("Consolas", 10), justify="left")
label_hasil.pack(pady=5)

# ----- Tab 2: Bagi Subnet -----
frame_bagi = tk.Frame(tab)
tab.add(frame_bagi, text="Bagi Subnet")

tk.Label(frame_bagi, text="Masukkan IP dan prefix:", font=("Arial", 11)).pack(pady=(15, 5))
entry_ip_bagi = tk.Entry(frame_bagi, font=("Arial", 12), width=25)
entry_ip_bagi.insert(0, "192.168.1.0/24")
entry_ip_bagi.pack()
tk.Label(frame_bagi, text="Dibagi jadi berapa subnet?", font=("Arial", 11)).pack(pady=(10, 5))
entry_jumlah = tk.Entry(frame_bagi, font=("Arial", 12), width=10)
entry_jumlah.insert(0, "4")
entry_jumlah.pack()
tk.Button(frame_bagi, text="Bagi", font=("Arial", 11), command=bagi).pack(pady=10)
label_bagi = tk.Label(frame_bagi, text="", font=("Consolas", 10), justify="left")
label_bagi.pack()

# ----- Tab 3: Riwayat -----
frame_riwayat = tk.Frame(tab)
tab.add(frame_riwayat, text="Riwayat")

tk.Button(frame_riwayat, text="Muat Ulang", font=("Arial", 11), command=muat_riwayat).pack(pady=10)
kotak_riwayat = tk.Listbox(frame_riwayat, font=("Consolas", 10), width=70, height=14)
kotak_riwayat.pack(padx=10)

muat_riwayat()
jendela.mainloop()