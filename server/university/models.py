from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField

from .models_abstract import SingletonModel

class City(models.Model):
    name = models.CharField('',max_length=255)

    class Meta:
        verbose_name = 'İl'
        verbose_name_plural = 'İller'


class FAQ(models.Model):
    title = models.CharField('Soru',max_length=255)
    content = models.TextField('Cevap')

    class Meta:
        verbose_name = 'Sıkça Sorulan Soru'
        verbose_name_plural = 'Sıkça Sorulan Sorular'


class Post(models.Model):
    title = models.CharField('Başlık',max_length=255)
    image = models.ImageField('Resim',upload_to='posts/')
    content = models.TextField('İçerik')

    class Meta:
        verbose_name = 'Haber'
        verbose_name_plural = 'Haberler'


class Area(models.Model):
    title = models.CharField('Başlık',max_length=255)
    price = models.IntegerField('Fiyat?')
    continuance = models.IntegerField('Kaç Yıl?')
    language = models.CharField('Dil',max_length=255)

    class Meta:
        verbose_name = 'Bölüm'
        verbose_name_plural = 'Bölümler'


class Faculty(models.Model):
    title = models.CharField('Başlık',max_length=255)
    image = models.ImageField('Resim',upload_to='faculties/')

    areas = models.ManyToManyField(Area,verbose_name='Bölümler',related_name='areas')  

    class Meta:
        verbose_name = 'Fakülte'
        verbose_name_plural = 'Fakülteler'

    def get_absolute_url(self):
        return reverse(
            'university:faculty-detail',
            args = [self.id]
        )

    
class Request(models.Model):
    name = models.CharField('Ad',max_length=255)
    tc = models.IntegerField('T.C. Numarası')
    phone = PhoneNumberField('Telefon Numarası')
    area = models.ForeignKey(Area, verbose_name='Bölüm', on_delete=models.CASCADE)
    viewed = models.BooleanField(default=False)
    message = models.TextField()

    city = models.ForeignKey(City, verbose_name='İl', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Başvuru'
        verbose_name_plural = 'Başvurular'


class SiteSettings(SingletonModel):
    title = models.CharField('Site Başlığı',max_length=255,blank=True,null=True)
    logo = models.ImageField('Logotip',upload_to='logo/',blank=True,null=True)
    support_phone = PhoneNumberField('Destek Numarası',blank=True,null=True)
    support_email = models.EmailField('Destek E-Postası',blank=True,null=True)

    class Meta:
        verbose_name = 'Ayarlar'
        verbose_name_plural = 'Ayarlar'