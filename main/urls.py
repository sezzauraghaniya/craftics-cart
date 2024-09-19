from django.urls import path
from . import views
from uuid import UUID
from main.views import show_main, create_craft_entry, show_xml, show_json, show_json_by_id, show_xml_by_id
from main.views import login_user, register, logout_user


app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('create-craft-entry', create_craft_entry, name='create_craft_entry'),
    path('craft/delete/<uuid:pk>/', views.delete_craft, name='delete_craft'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]

