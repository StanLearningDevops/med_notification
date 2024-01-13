from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name,
                    phone_number, password=None, **extra_fields):
        if not email:
            raise ValueError("The email field must be set")
        if not first_name and last_name:
            raise ValueError("Please provide First Name and Last name")
        if not phone_number:
            raise ValueError("Please provide a valid phone number")

        
        user = self.model(email = self.normalize_email(email),
                          first_name=first_name, last_name=last_name,
                          phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
     
    def create_superuser(self, email,
                         first_name, last_name, phone_number,
                         password=None, **extra_fields):
        
        user=self.create_user(email=email, first_name=first_name, last_name=last_name,
                              phone_number=phone_number, password=password,
                            **extra_fields)
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_superuser', True)
        user.save(using=self._db)
        return user

    
    
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, blank=True, default='')
    first_name = models.CharField(max_length=50, blank=True, default='')
    last_name = models.CharField(max_length=50, blank=True, default='')
    phone_number = models.CharField(max_length=20, blank=True, default='')
    start_date = models.DateTimeField(default=timezone.now)
    
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)

    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number']
    
    def __str__(self):
        return self.email
    
    def get_absolute_url(self):
        return reverse("data_detail")
    