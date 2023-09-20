from cProfile import label
from email import generator
from django import forms
from .models import *
from captcha.fields import CaptchaField

class ItemForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Planets
        fields = ('name', 'color', 'captcha')

class SearchForm(forms.Form):
    run = forms.CharField(max_length=20)