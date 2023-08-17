from .models import Link
from django import forms


class LinkForm(forms.ModelForm):  # form associated with model.
    class Meta:
        model = Link
        fields = ["name", "url", "slug"]
