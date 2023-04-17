from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserType(models.Model):
    USER = "USER"
    MANAGER = "MANAGER"
    ADMIN = "ADMIN"
    USER_TYPE_CHOICES = [
        (USER, 'user'),
        (MANAGER, 'manager'),
        (ADMIN, 'admin')
    ]
    type_of_user = models.CharField(
        max_length=7,
        choices=USER_TYPE_CHOICES,
        default=USER,
    )

    def __str__(self):
        return self.type_of_user


class MyUserManager(BaseUserManager):

    def create_superuser(self, email, username, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Суперпользователь должен иметь поле is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Суперпользователь должен иметь поле is_superuser=True.')

        return self.create_user(email, username, password, **other_fields)

    def create_user(self, email, username, password, **other_fields):

        if not email:
            raise ValueError('Адрес электронной почты обязателен')

        email = self.normalize_email(email)
        user = self.model(email=email, username=username,
                          **other_fields)
        user.set_password(password)
        user.save()

        return user


class MyUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField('адрес электронной почты', max_length=150, unique=True)
    username = models.CharField(verbose_name='имя пользователя', max_length=150, unique=True)
    user_type = models.ForeignKey(UserType, on_delete=models.CASCADE, verbose_name='тип пользователя', null=True)
    date_of_birth = models.DateField(verbose_name='дата рождения', null=True)
    date_joined = models.DateTimeField(verbose_name='дата регистрации', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='дата последнего посещения', auto_now=True)

    is_superuser = models.BooleanField(verbose_name='является суперпользователем', default=False)
    is_staff = models.BooleanField(verbose_name='является сотрудником', default=False)
    is_active = models.BooleanField(verbose_name='учетная запись активирована', default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
