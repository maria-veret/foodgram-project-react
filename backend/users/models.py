from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(
        'Никнейм',
        max_length=150,
        unique=True,
        help_text='Введите уникальное имя'
    )
    email = models.EmailField(
        'Email',
        max_length=254,
        unique=True,
        help_text='Введите электронную почту'
    )
    first_name = models.CharField(
        'Имя',
        max_length=150,
        help_text='Введите имя'
    )
    last_name = models.CharField(
        'Фамилия',
        max_length=150,
        help_text='Введите фамилию'
    )

    class Meta:
        ordering = ('username',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.username}, {self.email}'
