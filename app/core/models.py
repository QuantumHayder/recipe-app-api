"""Database Models"""
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    "Manager fro users"

    def create_user(self, email, password=None, **extra_fields):
        "Create, save , and return a new user"
        user = self.model(email=email, **extra_fields)
        # **extra_fields is used in case we added new fields to the user
        # model in the future, we don't modify the code and pass them
        user.set_password(password)
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    "User in the system"
    email = models.EmailField(max_length=2555, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    # To determine if user can log in to django admin

    objects = UserManager()

    USERNAME_FIELD = 'email'
