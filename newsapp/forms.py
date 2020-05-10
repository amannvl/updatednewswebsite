from django import forms

from .models import news

class newsModelForm(forms.ModelForm):
    class Meta:
        model = news
        fields = ['title', 'url', 'image']