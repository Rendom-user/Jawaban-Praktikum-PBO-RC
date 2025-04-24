import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import json, os

file_data = "catatan.json"
catatan = {}

def simpan_ke_file():
    with open(file_data, "w") as f: json.dump(catatan, f)

def muat_dari_file():
    global catatan
    if os.path.exists(file_data):
        with open(file_data, "r") as f: catatan = json.load(f)
        for k in catatan: listbox.insert(tk.END, k)

def tambah_catatan():
    judul, isi = entry_judul.get().strip(), text_isi.get("1.0", tk.END).strip()
    if not judul or not isi: return messagebox.showerror("Error", "Judul dan isi tidak boleh kosong!")
    waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    key = f"{judul} ({waktu})"
    catatan[key] = {"judul": judul, "isi": isi, "waktu": waktu}
    listbox.insert(tk.END, key)
    entry_judul.delete(0, tk.END)
    text_isi.delete("1.0", tk.END)

def tampilkan_isi(event):
    key = listbox.get(tk.ACTIVE)
    if key: entry_judul.delete(0, tk.END); entry_judul.insert(0, catatan[key]["judul"])
    text_isi.delete("1.0", tk.END)
    text_isi.insert(tk.END, catatan.get(key, {}).get("isi", ""))

def hapus_catatan():
    key = listbox.get(tk.ACTIVE)
    if key and messagebox.askyesno("Konfirmasi", "Yakin ingin menghapus catatan?"):
        listbox.delete(tk.ACTIVE)
        catatan.pop(key, None)
        entry_judul.delete(0, tk.END)
        text_isi.delete("1.0", tk.END)

def edit_catatan():
    key = listbox.get(tk.ACTIVE)
    if key:
        judul_baru, isi_baru = entry_judul.get().strip(), text_isi.get("1.0", tk.END).strip()
        if not judul_baru or not isi_baru: return messagebox.showerror("Error", "Judul dan isi tidak boleh kosong!")
        catatan[key] = {"judul": judul_baru, "isi": isi_baru, "waktu": catatan[key]["waktu"]}
        listbox.delete(tk.ACTIVE)
        listbox.insert(tk.END, f"{judul_baru} ({catatan[key]['waktu']})")
        entry_judul.delete(0, tk.END)
        text_isi.delete("1.0", tk.END)

def keluar():
    simpan_ke_file()
    root.destroy()

root = tk.Tk()
root.title("📘 Catatan Harian")
root.geometry("850x450")

frame_atas = ttk.Frame(root, padding=10)
frame_atas.pack(fill="x")

entry_judul = ttk.Entry(frame_atas, width=50)
entry_judul.pack(side="left", padx=5)
ttk.Button(frame_atas, text="Tambah", command=tambah_catatan).pack(side="left", padx=5)
ttk.Button(frame_atas, text="Edit", command=edit_catatan).pack(side="left", padx=5)
ttk.Button(frame_atas, text="Hapus", command=hapus_catatan).pack(side="left", padx=5)

frame_bawah = ttk.Frame(root, padding=10)
frame_bawah.pack(fill="both", expand=True)

listbox = tk.Listbox(frame_bawah, width=35, height=20, font=("Segoe UI", 10))
listbox.pack(side="left", fill="y")
listbox.bind("<<ListboxSelect>>", tampilkan_isi)
scrollbar = ttk.Scrollbar(frame_bawah, orient="vertical", command=listbox.yview)
scrollbar.pack(side="left", fill="y")
listbox.config(yscrollcommand=scrollbar.set)

text_isi = tk.Text(frame_bawah, width=70, height=20, font=("Segoe UI", 10), wrap="word", bg="#f7f7f7")
text_isi.pack(side="left", fill="both", expand=True)

muat_dari_file()
root.protocol("WM_DELETE_WINDOW", keluar)
root.mainloop()
