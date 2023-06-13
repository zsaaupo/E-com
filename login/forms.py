from django.forms import ModelForm 
from .model import *
from django.contrib.auth.forms import UserCreationForm


class ProfileForm(ModelForm):
    
    class Meta:
        model = Profile
        exclude = ('user',)
        

class SignUpForm(ModelForm):
    
    class Mete:
        model = User
        fields = ('email', 'password1', 'password2')