from django import forms
from customers.models import cliente
from django.contrib.auth.models import User

class ClienteForm(forms.ModelForm):
    class Meta:
        model = cliente 
        fields = '__all__'

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','password', ]