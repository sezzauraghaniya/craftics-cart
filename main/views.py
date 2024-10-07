from django.shortcuts import get_object_or_404, render, redirect, reverse
from main.forms import CraftEntryForm
from main.models import Craft
import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    context = {
        'nama' : request.user.username,
        'kelas': 'PBP F',
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
    data = Craft.objects.filter(user=request.user)    
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Craft.objects.filter(user=request.user)    
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Craft.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Craft.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

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

def edit_craft(request, id):
    # Get craft entry berdasarkan id
    craft = Craft.objects.get(pk = id)

    # Set craft entry sebagai instance dari form
    form = CraftEntryForm(request.POST or None, instance=craft)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_craft.html", context)

def delete_craft(request, id):
    # Get mood berdasarkan id
    craft = Craft.objects.get(pk = id)
    # Hapus mood
    craft.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
@require_POST
def add_craft_entry_ajax(request):
    name = strip_tags(request.POST.get("name"))  # strip HTML tags from craft name
    description = strip_tags(request.POST.get("description"))  # strip HTML tags from craft description
    name = request.POST.get("name")
    description = request.POST.get("description")
    price = request.POST.get("price")
    image_url = request.POST.get("image_url", "")  # Optional field, so we default to an empty string if not provided
    user = request.user

    # Creating a new CraftEntry object
    new_craft = Craft(
        name=name,
        description=description,
        price=price,
        image_url=image_url,  # If you are using image uploads, make sure to handle file data properly
        user=user
    )
    new_craft.save()

    # Return a success response
    return HttpResponse(b"CREATED", status=201)