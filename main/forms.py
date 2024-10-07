from django.forms import ModelForm
from main.models import Craft
from django.utils.html import strip_tags
class CraftEntryForm(ModelForm):
    class Meta:
        model = Craft
        fields = ["name", "description", "price", "image_url"]

    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)  # Strip HTML tags from craft name

    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)  # Strip HTML tags from craft description