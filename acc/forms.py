from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User



class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    
    class Meta:
        model = User
        fields = ("username", "email","first_name","last_name", "password1", "password2")
        
   
   
   
class RegisterUpdateForm(UserChangeForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    
    class Meta:
        model = User
        fields = ("username","email","first_name","last_name","password")
        # fields = '__all__' 
   
   
class ChangePasswordForm(UserChangeForm):
    old_password = forms.PasswordInput()
    new_password1 = forms.PasswordInput()
    new_password2 = forms.PasswordInput() 
    
    model = User
    fields = ('old_password', 'new_password1', 'new_password2')  