from django import forms

class LoginForm(forms.Form):
    usuario = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)