from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = [
        ('user', 'Пользователь'),
        ('mentor', 'Наставник'),
        ('tutor', 'Куратор'),
        ('admin', 'Админ'),
    ]
    role = models.CharField(max_length=128, choices=ROLE_CHOICES, default='user', verbose_name='Роль пользователя')
