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

## Tugas 4 - Implementasi Autentikasi, *Session*, dan *Cookies* pada Django

### Perbedaan antara `HttpResponseRedirect()` dan `redirect()`

- `HttpResponseRedirect()`: Merupakan kelas di Django yang digunakan untuk membuat respon HTTP yang mengarahkan ulang pengguna ke URL lain. Pada Craftics-Cart! penggunaannya dapat dilihat di potongan kode pada `views.py` 

    ``` bash
        response = HttpResponseRedirect(reverse("main:show_main"))
    ```

- `redirect()`: Ini adalah shortcut yang disediakan Django yang lebih fleksibel dibandingkan `HttpResponseRedirect`. Pada kode bisa memberikan argumen berupa URL, view name, atau objek, dan Django akan mengatur semuanya. Contoh:

    ``` bash
    return redirect('main:login')
    ```

Jadi, perbedaan utamanya adalah `redirect()` lebih sederhana dan fleksibel dibandingkan `HttpResponseRedirect()` karena menggunakan `redirect()` bisa menggunakan view name atau model instance sebagai argumen.

### Menghubungkan Entry dengan User.

- Menambahkan **ForeignKey** pada `models.py`

``` bash
user = models.ForeignKey(User, on_delete=models.CASCADE)
```

- Pada fungsi `create_craft_entry` inisiasikan User dengan User yang sedang *logged-in*

``` bash
raft_entry.user = request.user
```

- pada fungsi `show_main` data yang ditampilkan adalah data pengguna yang sedang *logged_in*

``` bash
 context = {
        ...
        'nama' : request.user.username,
        ...
    }
```

### Authentication dan Authorization

- Authentication *(Autentikasi)*: Proses verifikasi identitas pengguna, biasanya menggunakan username dan password. Ketika pengguna login, mereka memasukkan kredensial yang kemudian diverifikasi untuk memastikan bahwa mereka adalah pengguna terdaftar.

Contohnya berupa metode `login()` dan `authenticate()`:

``` bash  
def login_user(request):
    ...
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main:show_main')
    ...
    return render(request, 'login.html', context)
```

- Authorization *(Otorisasi)*: Proses menentukan hak akses pengguna setelah mereka terverifikasi. Misalnya, setelah login, apakah pengguna memiliki hak untuk mengakses halaman tertentu atau melakukan tindakan tertentu.

Otorisasi dapat diatur menggunakan decorator, seperti:

``` bash
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def show_main(request):
    ...
```

### Session pada Logged-in User dan Cookies

Django mengingat pengguna yang telah login menggunakan session yang disimpan di dalam cookies. Ketika pengguna login:

- Django membuat session ID dan menyimpannya dalam cookie sessionid di browser pengguna.
- Pada setiap permintaan (request) selanjutnya, browser mengirimkan cookie ini sehingga Django dapat mengenali pengguna yang sudah login.

Contoh potongan kode **Cookie** pada project:
``` bash
if form.is_valid():
    user = form.get_user()
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main"))
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
```

- **Kegunaan lain dari cookies**: Cookies dapat digunakan untuk menyimpan preferensi pengguna, melacak sesi pengguna, atau menyimpan data seperti keranjang belanja.
- **Keamanan cookies**: Tidak semua cookies aman. Cookies harus diatur dengan flag HttpOnly dan Secure untuk mencegah akses JavaScript dan memastikan hanya dikirim melalui koneksi HTTPS. Misalnya:

``` bash
response.set_cookie('last_login', value, httponly=True, secure=True)
```

### Pengerjaan Checklist

1. Akses User ke Aplikasi Django dengan *register, login dan logout*

- Buat form registrasi yang memungkinkan pengguna mendaftarkan akun baru dengan metode `register()`,

``` bash
def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created successfully!')
            return redirect('login')
    context = {'form': form}
    return render(request, 'register.html', context)
```

lalu tambahkan path fungsi ke `urls.py`

``` bash
path('register/', register, name='register'),
```

dan create file `register.html` sebagai tampilannya

- Buat form login untuk memungkinkan pengguna mengakses akun mereka dengan membuat fungsi `login_user()`,

``` bash
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
```

tambahkan path `login_user()` ke `urls.py`;

``` bash
path('login/', login_user, name='login'),
```

lalu buat file `login.html` sebagai tampilan utamanya.

- Implementasikan fungsi logout untuk keluar dari aplikasi dengan membuat fungsi `logout_user()`,

``` bash 
def logout_user(request):
    logout(request)
    return redirect('login')
```

tambahkan path fungsi ke `urls.py`,

``` bash
path('logout/', logout_user, name='logout'),
```

2. Membuat dua akun User yang memiliki tiga dummy data.

    - Membuat dua akun pengguna: Setelah fungsi registrasi berhasil diimplementasikan, buat dua akun pengguna dengan menggunakan form registrasi di halaman aplikasi (misalnya /register).

    - Menambahkan tiga dummy data: Untuk setiap pengguna, tambahkan tiga data menggunakan model yang sudah ada, misalnya `name` atau `description`.

    - contoh:

        <img src="image/USER1.png">
        <img src="image/USER2.png">


3. Menghubungkan model dengan User

    - Untuk menghubungkan model Product dengan User, tambahkan ForeignKey di model Product:

    ``` bash
    class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    ```

    - Pastikan pengguna yang login dihubungkan saat membuat produk:

    ``` bash
    def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect('main')
    else:
        form = ProductForm()
    ```

    - Jika pengguna dihapus, produk terkait juga akan dihapus karena `on_delete=models.CASCADE`.

4. menampilkan atribut User pada aplikasi dan penerapan Cookies

Untuk menampilkan username pengguna yang login, pada view utama `show_main`, ambil informasi dari pengguna yang sedang login dengan menambahkan `request.user.username` ke dalam context seperti berikut:

``` bash
def show_main(request):
    context = {
        'username': request.user.username,
        ...
    }
    return render(request, 'main.html', context)
```

Selain itu, untuk menerapkan cookie `last_login`, tambahkan logika di fungsi `login_user()` untuk menyimpan waktu login terakhir ke dalam cookie dengan menggunakan `response.set_cookie('last_login', str(datetime.datetime.now()))`, seperti pada contoh berikut:

``` bash
def login_user(request):
    i...
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse('main'))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            ...
    return render(request, 'login.html', {'form': form})
```
Kemudian, di `show_main()`, ambil data dari cookie `last_login` dan tambahkan ke dalam context:

``` bash
...
'username': request.user.username,
        'last_login': last_login,
...
```

Terakhir, inisiasi tampilan pada `main.html`



