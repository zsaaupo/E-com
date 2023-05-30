from django.db import models

# for custom user model and admin pannel
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy


class CustomUserManager(BaseUserManager):
    """ Custom user manager : create a user by email and password"""
    
    def _create_user(self, email, password, **extra_fields):
        """create user with email and password"""
        
        if not email:
            raise ValueError("The email must be set")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user