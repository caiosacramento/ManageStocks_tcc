from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class UsuarioForm(UserCreationForm):
    email = forms.EmailField(max_length = 100)
    first_name = forms.CharField(max_length = 10)
    last_name = forms.CharField(max_length = 20)
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1', 'password2']

    def clean_email(self):
        email_digitado = self.cleaned_data['email']
        if User.objects.filter(email=email_digitado).exists():
            raise ValidationError("O email {} já está em uso.".format(email_digitado))
        return email_digitado
    
class UsuarioUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']
    
    def clean_email(self):
        email_digitado = self.cleaned_data['email']
        if User.objects.filter(email=email_digitado).exists():
            raise ValidationError("O email {} já está em uso.".format(email_digitado))
        return email_digitado