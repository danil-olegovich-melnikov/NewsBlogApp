from django.contrib.auth.models import User
from django.db import models

sections = (
    ('news', 'Новость'),
    ('articles', 'Статья'),
    ('review', 'Обзор'),
)


# Create your models here.
class Article(models.Model):
    section = models.CharField("Раздел", choices=sections, max_length=10)
    title = models.CharField("Заголовок", max_length=100)
    description = models.CharField("Описание", max_length=10000)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Автор')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    cover = models.ImageField("Обложка", upload_to='articles/cover/')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at', '-updated_at']
