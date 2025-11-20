from django.db import models

# Create your models here.

class UserType(models.TextChoices):
    CUSTOMER = 'CU', 'Customer'
    VENDOR = 'VE', 'Vendor'

class UserProfile(models.Model):
    Role = models.CharField(
        max_length=2,
        choices=UserType.choices,
    )

    User_Name = models.CharField(max_length=100)
    Full_Name = models.CharField(max_length=200)
    Email = models.EmailField(unique=True)
    Phone_Number = models.CharField(max_length=15)
    Address = models.TextField()
    Password = models.CharField(max_length=100)
    confirm_Password = models.CharField(max_length=100)
    Created_At = models.DateTimeField(auto_now_add=True)
    Updated_At = models.DateTimeField(auto_now=True)
    Is_Active = models.BooleanField(default=True)
    Profile_Picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    def __str__(self):
        return self.User_Name

    def set_password(self, raw_password):
        self.Password = raw_password
        