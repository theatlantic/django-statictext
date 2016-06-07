from django import forms

from .models import StaticText


class StaticTextForm(forms.ModelForm):
    class Meta:
        model = StaticText
        fields = ("enabled", "content", "url",)
