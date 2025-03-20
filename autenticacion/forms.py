from django import forms
from django.contrib.auth import authenticate


class RegisterForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    name = forms.CharField(max_length=255)
    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        name = self.cleaned_data.get('name')
        return self.cleaned_data

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        user = authenticate(email=email, password=password)
        if not user:
            raise forms.ValidationError('Credenciales incorrectos')
        return self.cleaned_data
