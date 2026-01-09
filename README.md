# 📋 To-Do List Manager {UAS Pengantar Pemrograman}

- **Nama:** Najla Wening Khairunnisa
- **NIM:** 312510225
- **Kelas:** TI.25.A2
- **Mata Kuliah:** Pengantar Pemrograman
- **Dosen:** Agung Nugroho,S.Kom, M.Kom
- **Universitas:** Universitas Pelita Bangsa

## 📹 Video Presentasi
🎬 **Demo Program:** 

## 🎯 Deskripsi Singkat
Program **To-Do List Manager** sederhana berbasis Python yang mengimplementasikan:
- ✅ **Object-Oriented Programming (OOP)** - Class, Object, Encapsulation
- ✅ **Modular Programming** - Model, View, Controller terpisah
- ✅ **Exception Handling** - Validasi input dengan try-except
- ✅ **Table View** - Output dalam format tabel rapi

## 🚀 Cara Menjalankan
```bash
# 1. Clone repository
git clone https://github.com/njlwng/praktikumUAS.git

# 2. Masuk folder
cd uas-todo-list

# 3. Jalankan program
python main.py
```
## Struktur File
📂 uas-to-do-list/

├── 📄 main.py       # Program utama (standalone)

├── 📄 controller.py # Business logic

├── 📄 view.py       # User interface  

├── 📄 model.py      # Data structure

└── 📄 README.md     # Dokumentasi ini

## ✨ Fitur Program
➕ Tambah Task - Dengan validasi input tidak kosong

👁️ Lihat Semua Task - Tampilan tabel dengan formatting

🗑️ Hapus Task - Berdasarkan nomor dengan konfirmasi

📊 Statistik - Progress tracking dengan persentase

🔄 Menu Interaktif - Loop terus hingga exit

## 💻 Konsep Pemrograman yang Diterapkan

# 1. Object-Oriented Programming (OOP)
Class Design: ```SimpleView, SimpleController```

Encapsulation: Data task dalam dictionary/object

Methods: ```tambah_task(), hapus_task(), tampilkan_tasks()```

Constructor:``` __init__()``` untuk inisialisasi

# 2. Modular Architecture
Separation of Concerns: UI, Logic, Data terpisah

Reusability: Masing-masing module independen

Maintainability: Mudah di-update dan di-debug

# 3. Exception Handling
```
try:
    if not judul.strip():
        raise ValueError("Judul tidak boleh kosong!")
except ValueError as e:
    return f"❌ Error: {str(e)}"
```
# 4. User Experience
Input Validation: Cek data sebelum proses

Clear Messages: Feedback jelas untuk user

Table Formatting: Output rapi dengan string alignment

Error Prevention: Try-catch untuk unexpected errors

## 📊 Contoh Output Program
```
==================================================
       UAS PENGANTAR PEMROGRAMAN
       TO-DO LIST MANAGER
==================================================

📝 TO-DO LIST MANAGER
========================================
1. Tambah Task
2. Lihat Task
3. Hapus Task
4. Statistik
5. Keluar
========================================
Pilih menu (1-5): 2

==================================================
DAFTAR TASK
==================================================
1. Belajar Python OOP - Belum selesai
2. Buat Video Presentasi - Selesai
3. Upload ke GitHub - Belum selesai
==================================================
Total: 3 task
```
## 🎯 **Kesimpulan**

Program **To-Do List Manager** ini telah berhasil mengimplementasikan semua konsep yang dipelajari dalam mata kuliah Bahasa Pemrograman, khususnya pada pertemuan 11 (Pemrograman Modular/Fungsi) dan 12 (Python OOP). Dengan struktur **Model-View-Controller (MVC)** yang jelas, program menunjukkan pemahaman mendalam tentang **modularitas** dimana setiap komponen memiliki tanggung jawab terpisah: model.py sebagai data layer, view.py sebagai presentation layer, dan controller.py sebagai business logic layer. 

Implementasi **Object-Oriented Programming** tercermin dari penggunaan class, object, constructor, method, dan encapsulation. **Exception handling** dengan try-except block memastikan validasi input yang robust, sementara **table view** memberikan user experience yang baik dengan format output yang terstruktur. Program ini tidak hanya memenuhi semua requirement teknis UAS, tetapi juga menerapkan prinsip-prinsip clean code dan software engineering yang baik seperti separation of concerns, DRY (Don't Repeat Yourself), dan user-centered design.

Melalui project ini, terlihat kemampuan dalam **mengintegrasikan teori ke praktik**, mulai dari konsep dasar OOP hingga implementasi aplikasi fungsional yang interaktif. Program siap untuk dikembangkan lebih lanjut dengan tambahan fitur seperti penyimpanan database, antarmuka GUI, atau integrasi dengan API, menunjukkan skalabilitas yang baik dari arsitektur yang digunakan.
