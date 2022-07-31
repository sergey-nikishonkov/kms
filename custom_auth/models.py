from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager


class CustomUser(AbstractUser):
    username = models.CharField(
        max_length=12,
        validators=[
            RegexValidator(regex=r'^((\+7|7|8)+([0-9]){10})$',
                           message='Введите корректный номер телефона'),
        ],
        unique=True,
        verbose_name='Номер телефонa')

    EMAIL_FIELD = ''
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return f'{self.first_name} {self.username}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'