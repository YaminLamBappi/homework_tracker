from typing import Any

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import( UserCreationForm, AuthenticationForm)


class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email',]
        


            
class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__( *args, **kwargs)
        
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type":"text",
        "placeholder":"enter username"
    }))
    
    password = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type":"password",
        "placeholder":"enter password"
    }))
    
class UserRegistrationForm(UserCreationForm):
    
        username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type":"text",
        "placeholder":"enter username"
    }))
        email = forms.EmailField(widget=forms.TextInput(attrs={
        "class": "input",
        "type":"text",
        "placeholder":"enter email"
    }))
        firstname = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type":"text",
        "placeholder":"enter firstname"
    }))
        lastname = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type":"text",
        "placeholder":"enter lastname"
    }))
        
        password1 = forms.CharField(label="Password",widget=forms.TextInput(attrs={
            "class":"input",
            "type":"password",
            "placeholder":"enter password"
        }))
        password2 = forms.CharField(label="Confirm Password",widget=forms.TextInput(attrs={
            "class":"input",
            "type":"password",
            "placeholder":"enter password"
        }))
        
        class Meta:
            model = User
            fields = ['username','firstname', 'lastname','email','password1','password2']

            
        def save(self, commit=True):
            user = super(UserRegistrationForm, self).save(commit=False)
            user.first_name = self.cleaned_data['firstname']
            user.last_name = self.cleaned_data['lastname']
            if commit:
                user.save()
            return user
            