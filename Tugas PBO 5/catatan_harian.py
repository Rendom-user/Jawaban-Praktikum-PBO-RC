import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import json, os

catatan = {}
file_data = "catatan.json"

def simpan_ke_file():
    with open(file_data, "w") as f:
        json.dump(catatan, f)

def muat_dari_file():
    global catatan
    if os.path.exists(file_data):
        with open(file_data, "r") as f:
            catatan = json.load(f)
            for k in catatan:
                listbox.insert(tk.END, k)

def tambah_catatan():
    judul = entry_judul.get().strip()
    isi = text_isi.get("1.0", tk.END).strip()
    if not judul or not isi:
        messagebox.showerror("Error", "Judul dan isi tidak boleh kosong!")
        return
    waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    key = f"{judul} ({waktu})"
    catatan[key] = {"judul": judul, "isi": isi, "waktu": waktu}
    listbox.insert(tk.END, key)
    entry_judul.delete(0, tk.END)
    text_isi.delete("1.0", tk.END)

def tampilkan_isi(event):
    if not listbox.curselection():
        return
    key = listbox.get(listbox.curselection())
    data = catatan.get(key)
    if data:
        entry_judul.delete(0, tk.END)
        entry_judul.insert(0, data["judul"])
        text_isi.delete("1.0", tk.END)
        text_isi.insert(tk.END, data["isi"])

def hapus_catatan():
    if not listbox.curselection():
        return
    if not messagebox.askyesno("Konfirmasi", "Yakin ingin menghapus catatan?"):
        return
    key = listbox.get(listbox.curselection())
    listbox.delete(listbox.curselection())
    catatan.pop(key, None)
    entry_judul.delete(0, tk.END)
    text_isi.delete("1.0", tk.END)

def edit_catatan():
    if not listbox.curselection():
        return
    key = listbox.get(listbox.curselection())
    data = catatan.get(key)
    if not data:
        return
    judul_baru = entry_judul.get().strip()
    isi_baru = text_isi.get("1.0", tk.END).strip()
    if not judul_baru or not isi_baru:
        messagebox.showerror("Error", "Judul dan isi tidak boleh kosong!")
        return
    waktu = data["waktu"]
    new_key = f"{judul_baru} ({waktu})"
    catatan.pop(key)
    catatan[new_key] = {"judul": judul_baru, "isi": isi_baru, "waktu": waktu}
    listbox.delete(listbox.curselection())
    listbox.insert(tk.END, new_key)
    entry_judul.delete(0, tk.END)
    text_isi.delete("1.0", tk.END)

def tentang():
    messagebox.showinfo("Tentang", "Catatan Harian Modern\nVersi 1.5 made by kikks")

def keluar():
    simpan_ke_file()
    root.destroy()

root = tk.Tk()
root.title("📘 Catatan Harian")
root.geometry("850x450")
style = ttk.Style(root)
style.theme_use("clam")

menubar = tk.Menu(root)
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Keluar", command=keluar)
menubar.add_cascade(label="File", menu=file_menu)

help_menu = tk.Menu(menubar, tearoff=0)
help_menu.add_command(label="Tentang", command=tentang)
menubar.add_cascade(label="Bantuan", menu=help_menu)

root.config(menu=menubar)

frame_atas = ttk.Frame(root, padding=10)
frame_atas.pack(fill="x")

entry_judul = ttk.Entry(frame_atas, width=50)
entry_judul.pack(side="left", padx=(0,10))

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

text_isi = tk.Text(frame_bawah, width=70, height=20, font=("Segoe UI", 10), wrap="word", bg="#f7f7f7", relief="solid", borderwidth=1)
text_isi.pack(side="left", fill="both", expand=True)

muat_dari_file()
root.protocol("WM_DELETE_WINDOW", keluar)
root.mainloop()
