from django.db import models
from django.contrib.auth.models import User
# from . import service
from . import tasks
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
        # service.send(self.user.email, self.code)
        tasks.send_register_code.delay(self.user.email, self.code)
        super(UserEmailVerification, self).save(*args, **kwargs)