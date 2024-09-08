from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name_of_craft' : 'Crochet Bunny',
        'description': 'Bunny-shaped crocheted doll',
        'price': '65.000',
        'materials': 'Cotton Wool'
    }

    return render(request, "main.html", context)