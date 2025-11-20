from django import forms
from .models import UserProfile

class RegisterForm(forms.ModelForm):
    confirm_Password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = UserProfile
        fields = ['User_Name', 'Full_Name', 'Email', 'Phone_Number', 'Password', 'confirm_Password', 'Role']
        widgets = {
            'Password': forms.PasswordInput(),
            'confirm_Password': forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("Password")
        confirm_password = cleaned_data.get("confirm_Password")

        if password != confirm_password:
            self.add_error('confirm_Password', "Passwords do not match")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["Password"])
        if commit:
            user.save()
        return user

