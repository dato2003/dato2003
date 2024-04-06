from django import forms

class user_form(forms.Form):
    name = forms.CharField(max_length=30)
    lasatname = forms.CharField(max_length=50)
    email = forms.EmailField()
    passsword = forms.CharField(max_length=20)