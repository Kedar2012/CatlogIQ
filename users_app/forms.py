from django import forms
from .models import User

class RegisterForm(forms.ModelForm):
    Password = forms.CharField(widget=forms.PasswordInput())
    confirm_Password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['First_Name', 'Last_Name', 'username', 'Email', 'Phone_Number', 'Role', 'Password']
    
    def clean(self):
        cleaned_data = super().clean()
        Password = cleaned_data.get("Password")
        confirm_Password = cleaned_data.get("confirm_Password")

        if Password != confirm_Password:
            raise forms.ValidationError(
                "Password and Confirm Password does not match"
            )

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label="Username")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
