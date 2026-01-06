from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="email")
    phone_number = models.CharField(max_length=12, verbose_name="Номер телефона", blank=True, null=True, help_text="Добавте номер телефона")
    country = models.CharField(max_length=30, verbose_name="Страна", blank=True, null=True, help_text="Укажите вашу страну")
    avatar_photo =models.ImageField(upload_to="users/avatar/", null=True, blank=True, verbose_name="Аватар")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
