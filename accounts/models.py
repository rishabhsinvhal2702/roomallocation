from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from sqlalchemy import null

class MyAccountManager(BaseUserManager):
    def create_user(self, rollno, phone, email, first_name, last_name, password = None):
        if not rollno:
            raise ValueError("Users must have a roll no")
        if not phone:
            raise ValueError("Users must have a valid phone number")
        if not email:
            raise ValueError("Users must have an email address")
        if not first_name:
            raise ValueError("Users must have a first name")
        if not last_name:
            raise ValueError("Users must have a last name")
        
        user    = self.model(
            rollno = rollno,
            phone = phone,
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,rollno, phone, email, first_name, last_name, password):
        user = self.create_user(
            rollno = rollno,
            phone = phone,
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            password = password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    rollno = models.CharField(max_length=10, unique=True, null=False, blank=False)
    phone = models.CharField(max_length=10, unique=True, null=False, blank=False)
    email = models.EmailField(max_length=60, unique=True, null=False, blank=False)
    room_no = models.CharField(max_length=6, null=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_alloted = models.BooleanField(default=False)
    first_name = models.CharField(max_length=51, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)

    USERNAME_FIELD = 'rollno'
    REQUIRED_FIELDS = ['phone', 'email', 'first_name', 'last_name']

    objects = MyAccountManager()

    def __str__(self):
        return self.rollno
    
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True    