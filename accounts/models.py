from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='email', unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=110, verbose_name='first name')
    last_name = models.CharField(max_length=110, verbose_name='last name')
    is_staff = models.BooleanField(verbose_name='is staff?', default=False)
    is_active = models.BooleanField(verbose_name='is active?', default=False)
    is_superuser = models.BooleanField(verbose_name='is superuser?', default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return f'User:{self.first_name}'

    def get_user_information(self):
        '''
        This Method Will Return Combine of first_name field and last_name field of user !
        '''
        return f'{self.first_name}-{self.last_name}'