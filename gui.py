import tkinter as tk
from tkinter import messagebox

from kalkulator import hitung_subnet
from database import buat_tabel, simpan


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


buat_tabel()

jendela = tk.Tk()
jendela.title("Subnet Calculator")
jendela.geometry("460x280")

tk.Label(jendela, text="Masukkan IP dan prefix:", font=("Arial", 11)).pack(pady=(15, 5))

entry_ip = tk.Entry(jendela, font=("Arial", 12), width=25)
entry_ip.insert(0, "192.168.1.0/24")
entry_ip.pack()

tk.Button(jendela, text="Hitung", font=("Arial", 11), command=hitung).pack(pady=10)

label_hasil = tk.Label(jendela, text="", font=("Consolas", 10), justify="left")
label_hasil.pack(pady=5)

jendela.mainloop()