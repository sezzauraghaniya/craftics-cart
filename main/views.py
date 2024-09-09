from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'nama' : 'Crochet Bunny',
        'kelas': 'PBP F',
        'crafts': [
            {'name': 'Crochet Bunny', 'price': 65.000, 'description': 'Boneka bentuk kelinci terbuat dari bahan rajutan.'},
            {'name': 'Clay Rings', 'price': 5.000, 'description': 'Cincin tanah liat warna-warni.'},
        ],
    }

    return render(request, "main.html", context)