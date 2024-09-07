from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name_of_craft' : 'Crochet Bunny',
        'materials': 'Cotton Wool',
        'price': '65.000'
    }

    return render(request, "main.html", context)