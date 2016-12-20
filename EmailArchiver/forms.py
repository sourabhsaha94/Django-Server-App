
from django import forms
from .models import Login

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = ('username','password',)

class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = ('username','password',)
