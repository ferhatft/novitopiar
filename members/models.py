from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User


class Organization(models.Model):
    TYPE_CHOICES = (
        ('IND', 'Şahıs'),
        ('LARGE', 'Büyük işletme'),
        ('SME', 'KOBİ'),
        ('NGO', 'STK'),
    )
    
    name = models.CharField(max_length=100, verbose_name="Kuruluş Adı")
    logo = models.ImageField(upload_to='logos/', verbose_name="Kuruluş Logo")
    org_type = models.CharField(max_length=5, choices=TYPE_CHOICES, verbose_name="Kuruluş Türü")
    country = CountryField(verbose_name="Ülke")  # you can use a package like django-countries for this
    foundation_date = models.DateField(verbose_name="Kuruluş Tarihi")
    employee_count = models.PositiveIntegerField(verbose_name="Çalışan Sayısı")
    followers = models.ManyToManyField(User, related_name='followed_organizations')
    
    def __str__(self):
        return self.name
