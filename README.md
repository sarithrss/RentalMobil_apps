# RentalMobil_apps

## Deskripsi Aplikasi

Sistem rental mobil berbasis Python CLI untuk mensimulasikan proses penyewaan mobil sederhana. Program ini memungkinkan pengelolaan data mobil, customer, serta transaksi sewa oleh admin dan customer dalam bentuk aplikasi berbasis terminal.

---

## User / Stakeholder

### Customer

* Melakukan registrasi akun
* Melihat daftar mobil yang tersedia
* Menyewa mobil
* Mengupdate lama sewa
* Membatalkan transaksi sewa

### Admin

* Mengelola data mobil
* Menambah, mengubah, dan menghapus data mobil
* Mengubah status mobil (Tersedia / Booked / Nonaktif)
* Melihat seluruh data mobil

---

## Tujuan Pembuatan Aplikasi

* Melatih pemahaman konsep CRUD (Create, Read, Update, Delete) menggunakan Python
* Mensimulasikan sistem rental mobil sederhana seperti di dunia nyata
* Melatih logika pemrograman, struktur data (list & dictionary), dan flow aplikasi berbasis menu
* Membangun dasar pemahaman backend logic tanpa database

---

## ⚙️ Penjelasan Fitur

### A. CRUD

#### Create

* Menambah data mobil baru
* Registrasi customer baru
* Membuat transaksi penyewaan mobil

#### Read

* Menampilkan daftar mobil
* Menampilkan data customer

#### Update

* Mengubah data mobil
* Update lama sewa pada transaksi

#### Delete

* Soft delete mobil (mengubah status menjadi Nonaktif)
* Membatalkan transaksi dan mengembalikan status mobil menjadi Tersedia

### B. Fitur Tambahan

* Validasi input user (tidak boleh kosong, harus angka, dll)
* Sistem status mobil:

  * Tersedia
  * Booked
  * Nonaktif
* Relasi data antara mobil dan transaksi menggunakan `id_mobil`
* Auto generate ID transaksi
* Sistem cancel transaksi dengan update status mobil otomatis

#### Manajemen Mobil Nonaktif

* Menampilkan daftar mobil dengan status Nonaktif
* Melihat mobil yang sudah dinonaktifkan (soft delete)
* Mengaktifkan kembali mobil dari status Nonaktif menjadi Tersedia

---

## Limitasi Aplikasi

* Data belum tersimpan permanen (masih menggunakan list dan dictionary)
* Aplikasi masih berbasis CLI (terminal)
* Belum mendukung pengaturan sewa berdasarkan tanggal

---

## Pengembangan Selanjutnya

* Menambahkan database untuk penyimpanan data
* Menambahkan sistem sewa berdasarkan tanggal
* Mengembangkan aplikasi menjadi berbasis web

---

## Requirements

* Python 3.x
* Visual Studio Code (VS Code)

---

## Credits

Project ini dibuat sebagai bagian dari pembelajaran Python untuk memahami:

* CRUD System
* Data Structure (List & Dictionary)
* Flow Control Programming

Dibuat oleh: **Sari Theresia**

Sebagai latihan personal project Python CLI (Car Rental System).
