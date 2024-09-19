from django.shortcuts import get_object_or_404, render, redirect
from main.forms import CraftEntryForm
from main.models import Craft
import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse


# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    # fetch objects from database
    craft_entries = Craft.objects.filter(user=request.user)

    context = {
        'nama' : request.user.username,
        'kelas': 'PBP F',

        'crafts': [
            {'name': 'Crochet Bunny', 'price': 65.000, 'description': 'Boneka bentuk kelinci terbuat dari bahan rajutan.'},
            {'name': 'Clay Rings', 'price': 5.000, 'description': 'Cincin tanah liat warna-warni.'},
        ],

        'craft_entries' : craft_entries,
        'last_login': request.COOKIES['last_login']
    }

    return render(request, "main.html", context)

def create_craft_entry(request):
    form = CraftEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        craft_entry = form.save(commit=False)
        craft_entry.user = request.user
        craft_entry.save()
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

def delete_craft(request, pk):
    craft = get_object_or_404(Craft, pk=pk)
    craft.delete()
    return redirect('main:show_main')

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New account created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response



