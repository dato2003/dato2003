from django import forms
from .models import author,book


class authorforms (forms.ModelForm):
    class Meta:
        model= author
        fields = ["name","surname","personal_troughts"]


class bookforms(forms.ModelForm):
    class Meta:
        release_date= forms.DateField(widget=forms.DateInput())
        model=book
        fields = ["title","description","author","ganre","release_date","personal_trought"]




