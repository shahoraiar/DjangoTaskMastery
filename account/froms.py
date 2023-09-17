from django import forms
from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Enter valid username'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your first name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your last name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'id': 'required', 'placeholder': 'Enter email address'}))
    
    # Use the PasswordInput widget and set custom labels
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter a strong password'}),
        help_text="Your password must contain at least 8 characters, including both letters and numbers."
    )
    password2 = forms.CharField(
        label="Retype Password",
        widget=forms.PasswordInput(attrs={'placeholder': 'Re-enter your password'}),
        help_text="Please enter the same password as above, for verification."
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        
class ChangeUserData(UserChangeForm) : 
    password = None
    class Meta : 
        model = User
        fields = ['username' , 'first_name' , 'last_name' , 'email']
