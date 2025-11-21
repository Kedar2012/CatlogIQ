from django import forms
from .models import User, UserProfile

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

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['First_Name', 'Last_Name', 'Email', 'Role', 'Phone_Number']

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        # Make these fields read-only
        self.fields['First_Name'].disabled = True
        self.fields['Last_Name'].disabled = True
        self.fields['Email'].disabled = True
        self.fields['Role'].disabled = True


class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'profile_picture', 'cover_photo', 'address', 'country',
            'state', 'city', 'postal_code', 'longitude', 'latitude'
        ]

