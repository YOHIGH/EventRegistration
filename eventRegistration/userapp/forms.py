from django import forms
from .models import *

class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["username", "password","phone_number", "photo","date_of_birth", "gender" ]
        widgets = {
            'password': forms.PasswordInput(),
        }