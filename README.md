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
        'name_of_craft' : 'Crochet Bunny',
        'description': 'Bunny-shaped crocheted doll',
        'price': '65.000',
        'materials': 'Cotton Wool'
    }

    return render(request, "main.html", context)
```
12. Konfigurasi *routing* URL milik `main` di file `urls.py`

```bash
app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```
13. Test final aplikasi pada `localhost` dengan command:

```bash
python manage.py runserver
```
lalu proyek di-*deploy* pada *PWS*

### Django Architecture Diagram

<!-- ![](D:\sems3\PBP TUGAS INDIVIDU\assets\bagan PBP.png) -->
Diagram ini mencerminkan hubungan antara berbagai komponen dalam arsitektur Django, di mana views.py menjadi pusat pengolahan yang menghubungkan urls.py, models.py, dan template HTML. Alur kerjanya seperti berikut:

1. User melakukan permintaan (request) melalui URL yang dikonfigurasi dalam urls.py.
2. urls.py meneruskan permintaan tersebut ke views.py sesuai dengan view yang dibutuhkan.
3. views.py kemudian melakukan pengolahan, berinteraksi dengan models.py untuk membaca (read) atau menulis (write) data ke database.
4. views.py juga akan merender template (berkas HTML) yang dibutuhkan dengan menggunakan data yang diperoleh dari model.
5. Setelah pengolahan selesai, views.py memberikan respons kembali ke User dalam bentuk halaman web yang sudah di-render.

### Git for Software Development

Git digunakan sebagai sistem kontrol versi yang mengelola perubahan kode, mendukung kolaborasi tim, melacak riwayat, menyelesaikan konflik, dan menjaga keamanan. Git juga memungkinkan *rollback* serta integrasi dengan layanan CI/CD, membuat pengembangan *software* lebih efisien dan terorganisir.
