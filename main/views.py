from django.shortcuts import render, redirect
from main.forms import CraftEntryForm
from main.models import Craft
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_main(request):
    # fetch objects from database
    craft_entries = Craft.objects.all()

    context = {
        'nama' : 'Sezza Auraghaniya Winanda',
        'kelas': 'PBP F',

        'crafts': [
            {'name': 'Crochet Bunny', 'price': 65.000, 'description': 'Boneka bentuk kelinci terbuat dari bahan rajutan.'},
            {'name': 'Clay Rings', 'price': 5.000, 'description': 'Cincin tanah liat warna-warni.'},
        ],

        'craft_entries' : craft_entries
    }

    return render(request, "main.html", context)

def create_craft_entry(request):
    form = CraftEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')
    
    context = {'form': form}
    return render(request, "create_craft_entry.html", context)

def show_xml(request):
    data = Craft.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Craft.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Craft.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Craft.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")