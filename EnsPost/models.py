from django.db import models
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=120,verbose_name='Başlık') # başlık için karakter sınırlıyoruz
    content = models.TextField(verbose_name='İçerik')                # uzun metinler için textfield kullanıyoruz.
    publishing_date = models.DateTimeField(verbose_name='Yayınlanma Tarihi', auto_now_add=True) # yazılan postun tarihini kaydedecek

    def __str__(self):    # postun başlığının görünmesi için yapıyoruz
        return self.title

    def get_absolute_url(self):
        return reverse('post:detail',kwargs={'id': self.id})
