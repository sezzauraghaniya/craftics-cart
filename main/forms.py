from django.forms import ModelForm
from main.models import Craft

class CraftEntryForm(ModelForm):
    class Meta:
        model = Craft
        fields = ["name", "description", "price", "image_url"]