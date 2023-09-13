# razzle-fresh-stock
Click untuk menuju website [razzle-fresh-stock](https://razzle-fresh-stock.adaptable.app)

# Implementasi Checklist
step-by-step pengerjaan proyek Django.

## Membuat Proyek Django Baru
1. Mempersiapkan direktori lokal baru yaitu razzle_fresh_stock serta repositori di GitHub bernama razzle-fresh-stock.
2. Melakukan inisiasi repositori lokal dengan repositori GitHub dengan melakukan perintah `git init` pada command prompt direktori lokal.
3. Membuat branch baru dengan menjalankan perintah `git branch -M master` di command prompt direktori lokal.
4. Menghubungkan repositori lokal dengan repositori GitHub dengan menjalankan perintah `git remote add origin master`.
5. Membuat _virtual environment_ dengan menjalankan perintah `python -m venv env` di command prompt direktori lokal.
6. Menjalankan _virtual environment_ dengan menjalankan perintah `env\Scripts\activate.bat` di command prompt direktori lokal. _Virtual environment_ digunakan untuk mengisolasi package sehingga tidak bertabrakan dengan app lainnya.
7. Membuat berkas requirements.txt yang berisi _dependencies_. Isi dari file _dependencies_ mengikuti tutorial.
8. Menginstall _dependencies_ dengan menjalankan perintah `pip install -r requirements.txt` di dalam _virtual environment_.
9. Membuat proyek razzle_fresh_stock dengan menjalankan perintah `django-admin startproject razzle_fresh_stock .`.
10. Menambahkan '*' pada `ALLOWED HOSTS` di `settings.py` untuk mengizinkan akses dari semua host.
11. Menjalankan server Django dengan menjalankan perintah `python manage.py runserver`, kemudian membuka link http://localhost:8000 untuk mengecek apakah 
12. Mematikan server dengan `Ctrl+C` serta mematikan _virtual environment_ dengan menjalankan perintah `deactivate`.
13. Menambahkan berkas `.gitignore` agar beberapa berkas tidak ditrack. Isi dari berkas .gitignore mengikuti tutorial 0.
14. Melakukan git add, commit, push.

## Membuat Aplikasi dengan Nama main pada Proyek
1. Aktifkan _virtual environment_.
2. Buat aplikasi/app baru bernama `main` dengan menjalankan perintah `python manage.py startapp main`.
3. Mendaftarkan aplikasi `main` dengan cara memasukkan `'main'` ke dalam variabel `INSTALLED_APPS` di dalam file settings.py

## Melakukan Routing pada Proyek
1. Buka berkas `urls.py` yang adaa di dalam direktori `razzle_fresh_stock`, lalu impor fungsi include dari library `django.urls`.
2. Menambahkan rute URL ke dalam variabel `urlpatterns`
```
urlpatterns = [
    ...
    path('main/', include('main.urls')),
    ...
]
```

## Membuat Model pada Aplikasi main
1. Membuka file `models.py` pada direktori `main`.
2. Isi file `models.py` dengan kode:
```
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)
    amount = models.IntegerField()
    description = models.TextField()
```
5. Setiap variabel pada file `models.py` akan dihubungkan ke views.
6. Jalankan perintah `python manage.py makemigrations`. Perintah ini dijalankan untuk membuat berkas migrasi perubahan dari isi file `models.py` yang belum diaplikasikan ke database.
7. Jalankan perintah `python manage.py migrate`. Perintah ini dijalankan untuk mengaplikasikan perubahan models yang ada di dalam berkas migrasi.

## Membuat Fungsi pada views.py
1. Pastikan sudah memiliki file template HTML.
2. Tambahkan baris impor `from django.shortcuts import render`.
3. Tambahkan fungsi `show_main`. Isi fungsi `show_main` dengan data-data yang ingin digunakan.

## Membuat Routing pada urls.py dalam Direktori main
1. Membuat file `urls.py` di dalam direktori `main`.
2. Mengisi `urls.py` dengan kode berikut :
```
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```

## Melakukan Deployment ke Adaptable
1. Pilih tombol New App di dashboard Adaptable
2. Pilih Connect an Existing Repository, lalu pilih repositori `razzle-fresh-stock`
3. Pilih Python App Template sebagai template deployment
4. Pilih PostgreSQL sebagai tipe database yang digunakan
5. Cocokkan versi python dengan python yang ada di dalam virtual environment 
6. Masukkan perintah `python manage.py migrate && gunicorn shopping_list.wsgi` ke Start Command
7. Masukkan nama domain yang diinginkan yaitu razzle-fresh-stock
8. Centang bagian `HTTP Listener on PORT` lalu klik deploy app

# Bagan Request Client
![](<Screenshot 2023-09-13 072411.png>)

1. User memberikan request ke Django melalui browser. Django bekerja sebagai controller melakukan pengecekan keberadaan resource di `urls.py`.
2. Jika ditemukan URL, `views.py` akan dipanggil. `views.py` akan berinteraksi dengan model dan template.
3. `models.py` adalah interface dari database. 
4. `main.html` adalah template dari bagian yang statis/tidak berubah dari web app.
5. `views.py` adalah user interface. `views.py` berinteraksi dengan `models.py` untuk mendapatkan data. `views.py` juga berinteraksi dengan `main.html` untuk mendapatkan output HTML yang diinginkan.

# Mengapa harus menggunakan _virtual environment_?
Penggunaan _virtual environment_ dilakukan dengan mengisolasi package serta dependencies dari aplikasi yang sedang kita buat. Mengisolasi package dilakukan untuk menghindari adanya tabrakan antara versi-versi lain aplikasi yang ada di devicemu. Dengan mengaktifkan _virtual environment_ kita memiliki kontrol penuh untuk membuat versi yang kita inginkan. Membuat aplikasi tanpa _virtual environment_ tetap dapat dilakukan, namun lebih baik digunakan.

# Apa itu MVC, MVT, MVVM?
MVC, MVT, dan MVVM adalah pola desain arsitektur yang yang membagi aplikasi menjadi beberapa komponen.<br />

**MVC** 
1. Model : pusat komponen arsitektur. Mengelola data, logika, serta constraints dari aplikasi.
2. View :  mengatur bagaiaman data akan ditampilkan dan menyediakan berbagai macam data representasi komponen.
3. Controller : memanipulasi  Model
 dan render view dengan menjadi sebagai jembatan antara keduanya.

 **MVT**
 1. Model : bekerja sebagai interface dari database. Dalam garis besar adalah struktur logika dibalik keseluruhan web app.
 2. View : berinteraksi dengan model dan template. Menerima HTTP request dan mengembalikan HTTP responses.
 3. Template : bagian statis dari web app. Berupa kode HTML.

 **MVVM**
 1. Model : menyimpan logika program.
 2. View : kumpulan elemen yang tampak, termasuk user interface. Menerima user input. 
 3. ViewModel : terletak di antara view dan model. Letak kontrol interaksi dengan view.

Perbedaan utama antara MVC, MVT, dan MVVM adalah peran penenah komponen. Pada MVC, yang berperan sebagai penengah komponen adalah Controller. Pada MVT, yang menjadi penengah adalah View. Sedangkan pada MVVM, yang menjadi penengah adalah ViewModel.


