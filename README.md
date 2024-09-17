# Craftics Cart

Project Django sederhana dengan tema *e-commerce*, sebagai Tugas Individu Mata Kuliah Pemrograman Berbasis Platform rancangan **Sezza Auraghaniya** dengan NPM **2306207291**.
> **Craftics Cart** adalah aplikasi jual-beli untuk pengrajin atau penggemar produk kerajinan tangan seperti rajutan, *glassware*, hiasan, dan masih banyak lainnya!

## Tugas 2 - Implementasi Model-View-Template (MVT) pada Django

### Membuat sebuah proyek Django baru 
1. Membuat *directory* lokal bernama `craftics-cart`
2. Membuat dan mengaktifkan *virtual environment* dengan perintah:

```bash
python -m venv env
env\Scripts\activate
```

3. Menyiapkan *dependencies* dengan file **requirements.txt** lalu *dependencies* di-install menggunakan perintah:

```bash
pip install -r requirements.txt
```

4. Membuat proyek Django dengan menjalankan perintah startproject di *command prompt*

```bash
django-admin startproject craftics_cart .
```

5. Konfigurasi proyek dengan menambahkan daftar host pada `settings.py` lalu menjalankan server Django dengan command:

```bash
python manage.py runserver
```

6. Inisiasi *directory* lokal ke repositori github dan membuat branch utama dengan *command*:

```bash
git branch -M main
```

dilanjut dengan melakukan git `add`, `commit`, dan `push` ke dalam repositori github.

7. Membuat aplikasi `main` pada proyek

```bash
python manage.py startapp main
```

kemudian menambahkan `main` pada variabel `INSTALLED_APPS`

8. Membuat berkas `main.html` berisikan atribut berupa `name of craft`, `description`, dan `price`.

9. Mendefinisikan model pada `models.py` dengan:

```bash
from django.db import models

class Crafts(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField() 
    description = models.TextField(max_length=2000)
    materials = models.CharField(max_length=255)

    @property
    def is_mood_strong(self):
        return self.mood_intensity > 5
```

10. Migrasi model untuk melacak perubahan pada model basis data.

```bash
python manage.py makemigrations
python manage.py migrate
```

11. Integrasi komponen MVT dengan impor fungsi `render` dari modul `django.shortcuts`, dan menambahkan fungsi `show_main` berisikan atributes

```bash
def show_main(request):
    context = {
        `name_of_craft` : `Crochet Bunny`,
        `description`: `Bunny-shaped crocheted doll`,
        `price`: `65.000`,
        `materials`: `Cotton Wool`
    }

    return render(request, "main.html", context)
```
12. Konfigurasi *routing* URL milik `main` di file `urls.py`

```bash
app_name = `main`

urlpatterns = [
    path(`, show_main, name=`show_main`),
]
```
13. Test final aplikasi pada `localhost` dengan command:

```bash
python manage.py runserver
```
lalu proyek di-*deploy* pada *PWS*

### Django Architecture Diagram

  <img src="image/diagram-django.png">

Diagram ini mencerminkan hubungan antara berbagai komponen dalam arsitektur Django, di mana views.py menjadi pusat pengolahan yang menghubungkan urls.py, models.py, dan template HTML. Alur kerjanya seperti berikut:

1. User melakukan permintaan (request) melalui URL yang dikonfigurasi dalam `urls.py`.
2. urls.py meneruskan permintaan tersebut ke views.py sesuai dengan view yang dibutuhkan.
3. views.py kemudian melakukan pengolahan, berinteraksi dengan models.py untuk membaca (read) atau menulis (write) data ke database.
4. views.py juga akan merender template (berkas HTML) yang dibutuhkan dengan menggunakan data yang diperoleh dari model.
5. Setelah pengolahan selesai, views.py memberikan respons kembali ke User dalam bentuk halaman web yang sudah di-render.

### Git for Software Development

Git digunakan sebagai sistem kontrol versi yang mengelola perubahan kode, mendukung kolaborasi tim, melacak riwayat, menyelesaikan konflik, dan menjaga keamanan. Git juga memungkinkan *rollback* serta integrasi dengan layanan CI/CD, membuat pengembangan *software* lebih efisien dan terorganisir.

### Pemilihan Django Framework

Berikut adalah alasan memilih Django sebagai *framework* pemula:

1. Django mencakup hampir semua yang dibutuhkan untuk membuat *website*. Mulai dari meng-*handle database* sampai validasi pengguna.

2. Instalasi Django yang hanya membutuhkan **python 3** dan aktivasi *virtual environment* terhitung mudah dari yang lain.

### Django as ORM (Object-Relational Mapping)

Sesuai dengan namanya, ORM berarti pemetaan dari Object-Oriented Programming **(OOP)** ke *relational database*. dengan kata lain, berfungsi untuk menjembatani kedua sistem dan secara otomatik mengonversi data-data di dalamnya.

## Tugas 3 - Implementasi Form dan Data Delivery pada Django

### *Data Delivery* pada Implementasi Platform

Data delivery memungkinkan komunikasi efisien dan pengiriman secara *real-time* antar komponen atau sistem, seperti dari *backend* ke *frontend*

### XML or JSON?

Untuk *website* modern, lebih disarankan penggunaan JSON karena lebih ringan, lebih mudah, dan lebih cepat diproses. 

Namun, XML memiliki kelebihan jika digunakan pada skenario yang lebih kompleks. Seperti data struktur yang *deep* dan dan membutuhkan validasi ketat.

### JSON lebih popular dari XML

Penulisan JSON lebih ringan dengan format yang lebih sederhana. Sehingga lebih mudah dipahami dan mudah di-integrasikan dengan JavaScript. Dimana JavaScript, merupakan bahasa yang banyak digunakan di *front-end*

### Fungsi dari method `is_valid()` pada form Django

`is_valid()` memeriksa apakah data yang dimasukkan ke dalam form sesuai dengan aturan validasi yang ditetapkan. Ketika data valid akan mengembalikan nilai **True**. Tanpa method `is_valid()` kemungkinan input penguna tidak sesuai akan lewat begitu saja.

### `crsf_token` saat Membuat Form di Django

**CRSF** atau Cross-Site Request Forgery, merupakan serangan  dimana penyerang dengan mudah mengirimkan permintaan jahat dari situs lain dengan cara meniru request asli dari aplikasi kita. `crsf_token` adalah untuk Django memverifikasi bahwa permintaan memang berasal dari pengguna dan bukan *source* lain.

### Pembuatan Form dan Data Delivery pada Craftics-Cart!

1. Membuat file `forms.py` untuk inisiasi atribut yang diminta kepada User

2. Membuat fungsi pada `views.py` dalam bentuk XML, JSON, XML by ID, dan JSON by ID.

3. Mmebuat *routing* URL dengan meng-*import* fungsi ke `urls.py` dan menambhahkan path URL ke `urlpatterns`

4. Hasil akses URL pada *Postman*

    - XML
    <img src="image/xml.png">
    - JSON
    <img src="image/json.png">
    - XML by ID
    <img src="image/xml-id.png">
    - JSON by ID
    <img src="image/json-id.png">

5. Melakukan `add`, `commit`, dan `push` ke github dan PWS.