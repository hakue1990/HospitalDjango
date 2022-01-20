from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegUser(UserCreationForm):
    email = forms.EmailField()
#nadpisywanie oryginalnej klasy usercreationform przez własną klasę która rozszerza ją o dodatkowe pole email
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

