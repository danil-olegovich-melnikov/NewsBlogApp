from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import send_mail
import random

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    picture = models.ImageField('Фотография', upload_to='auth/users/')

    def __str__(self):
        return self.user.username


class UserEmailVerification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь", to_field='username')
    code = models.PositiveSmallIntegerField('Код активации')

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        self.code = random.randint(100000, 999999)
        send_mail(
            subject='Subject here',
            message=f'Verification code: {self.code}',
            recipient_list=['danil369.ru@mail.ru'],
            from_email=settings.EMAIL_HOST_PASSWORD,
        )
        super(UserEmailVerification, self).save(*args, **kwargs)