from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class userManager(BaseUserManager):
    def create_user(self, First_Name, Last_Name, User_Name, Email, Role, password=None):
        if not Email:
            raise ValueError("Email is required")
        if not User_Name:
            raise ValueError("Username is required")
        user = self.model(
            First_Name=First_Name,
            Last_Name=Last_Name,
            User_Name=User_Name,
            Email=self.normalize_email(Email),
            Role=Role,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, First_Name, Last_Name, User_Name, Email, password=None, Role=None):
        user = self.create_user(
            First_Name=First_Name,
            Last_Name=Last_Name,
            User_Name=User_Name,
            Email=self.normalize_email(Email),
            Role=UserType.ADMIN,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user

class UserType(models.TextChoices):
    CUSTOMER = 'Customer', 'Customer'
    VENDOR = 'Vendor', 'Vendor'
    ADMIN = 'Admin', 'Admin'

class User(AbstractBaseUser):

    First_Name = models.CharField(max_length=200)
    Last_Name = models.CharField(max_length=200)
    User_Name = models.CharField(max_length=100, unique=True)
    Email = models.EmailField(unique=True)
    Phone_Number = models.CharField(max_length=15)
    Role = models.CharField(max_length=10,choices=UserType.choices)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    modified_date = models.DateTimeField(auto_now=True)

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'User_Name'
    REQUIRED_FIELDS = ['First_Name', 'Last_Name', 'Email', 'Role']

    objects = userManager()

    def __str__(self):
        return self.User_Name
    
    def get_role(self):
        return self.Role
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    cover_photo = models.ImageField(upload_to='cover_photos/', null=True, blank=True)
    address = models.TextField(max_length=500, blank=True)
    country = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    postal_code = models.CharField(max_length=20, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.User_Name
    
