0. Tema aplikasi
1. # RentalMobil_apps

1. Deskripsi Aplikasi
Sistem rental mobil berbasis Python CLI untuk mensimulasikan proses penyewaan mobil sederhana. Program ini memungkinkan pengelolaan data mobil, customer, serta transaksi sewa oleh admin dan customer dalam bentuk aplikasi berbasis terminal.

1. User/stakeholder
Aplikasi ini digunakan oleh 2 jenis pengguna:

- Customer
Melakukan registrasi akun
Melihat daftar mobil yang tersedia
Menyewa mobil
Mengupdate lama sewa
Membatalkan transaksi sewa
- Admin
Mengelola data mobil
Menambah, mengubah, dan menghapus data mobil
Mengubah status mobil (Tersedia / Booked / Nonaktif)
Melihat seluruh data mobil

1. Tujuan pembuatan aplikasi
- Melatih pemahaman konsep CRUD (Create, Read, Update, Delete) menggunakan Python
- Mensimulasikan sistem rental mobil sederhana seperti di dunia nyata
- Melatih logika pemrograman, struktur data (list & dictionary), dan flow aplikasi berbasis menu
- Membangun dasar pemahaman backend logic tanpa database
  
1. Penjelasan fitur:
   a. CRUD
       - Create
          1. Menambah data mobil baru
          2. Registrasi customer baru
          3. Membuat transaksi penyewaan mobil
        - Read
          1. Menampilkan daftar mobil
          2. Menampilkan data customer
        -  Update
          1. Mengubah data mobil
          2. Update lama sewa pada transaksi
        - Delete
          1. Soft delete mobil (mengubah status menjadi Nonaktif)
          2. Membatalkan transaksi dan mengembalikan status mobil menjadi Tersedia
   
   b. FITUR TAMBAHAN
          - Validasi input user (tidak boleh kosong, harus angka, dll)
          - Sistem status mobil:
                1. Tersedia
                2. Booked
                3. Nonaktif
          - Relasi data antara mobil dan transaksi menggunakan id_mobil
          - Auto generate ID transaksi
          - Sistem cancel transaksi dengan update status mobil otomatis
          - Manajemen Mobil Nonaktif:
                1. Menampilkan daftar mobil dengan status Nonaktif
                2. Melihat mobil yang sudah dinonaktifkan (soft deleted)
                3. Mengaktifkan kembali mobil dari status Nonaktif → Tersedia


1. Limitasi Aplikasi
- Data belum tersimpan permanen (masih menggunakan list dan dictionary)
- Aplikasi masih berbasis CLI (terminal)
- Belum mendukung pengaturan sewa berdasarkan tanggal

1. Pengembangan selanjutnya
- Menambahkan database untuk penyimpanan data
- Menambahkan sistem sewa berdasarkan tanggal
- Mengembangkan aplikasi menjadi berbasis web

1. Requirements
- Python 3.14
- Vscode
  
1. Credits
Project ini dibuat sebagai bagian dari pembelajaran Python untuk memahami:
- CRUD system
- Data structure (list & dictionary)
- Flow control programming

Dibuat oleh: Sari Theresia
Sebagai latihan personal project Python CLI (Car Rental System)
