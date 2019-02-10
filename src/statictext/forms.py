from django import forms

from .models import StaticText


class StaticTextForm(forms.ModelForm):
    class Meta:
        model = StaticText
        fields = ("enabled", "content", "url",)


class StaticTextWithLayoutForm(StaticTextForm):
    class Meta(StaticTextForm.Meta):
        fields = StaticTextForm.Meta.fields + ("layout",)
