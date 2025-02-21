from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    """Foydalanuvchilarni boshqaruvchi manager"""

    def create_user(self, phone_number,  password=None, **extra_fields):
        """Oddiy foydalanuvchi yaratish"""
        if not phone_number:
            raise ValueError("Telefon raqami majburiy")
        user = self.model(phone_number=phone_number,  **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        """Superuser yaratish"""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(phone_number,  password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    """Custom foydalanuvchi modeli"""
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('student', 'Student'),
    )

    phone_number = models.CharField(max_length=15, unique=True, null=False)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'phone_number'


    def str(self):
        return self.phone_number