from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        '''
        Override create_user for create a user with email and password
        '''
        if not email:
            raise ValueError('User must Have A email')
        if not password:
            raise ValueError('User Must Have A password') 
        
        user_email = self.normalize_email(email)
        user = self.model(email=user_email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        '''
        Override create_superuser for Create A Superuser With is_staff and is_superuser is True
        '''
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)

        if  extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must Have is_superuser=True')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must Have is_staff=True')
        
        return self.create_user(email, password, **extra_fields)
              