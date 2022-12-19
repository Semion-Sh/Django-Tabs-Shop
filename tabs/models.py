from django.db import models

# Create your models here.
from django.test import TestCase
from django.db import models
from django.core.validators import MinValueValidator


class Guitar_tabs(models.Model):
    __tablename__ = 'guitar'
    tab_text = models.TextField(blank=True)
    # tab_text = models.ImageField(blank=True)


class Songs(models.Model):
    __tablename__ = 'songs'
    # id = models.IntegerField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=500)
    photo = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True)
    guitar_tabs = models.ForeignKey(Guitar_tabs, on_delete=models.PROTECT, related_name='guitar_tabs')
    # piano_tabs = models.ForeignKey(Piano_tabs, on_delete=models.PROTECT, related_name='piano_tabs')
    price = models.FloatField(default=0)
    views = models.IntegerField(default=0, verbose_name='views')
    add_date = models.DateTimeField(auto_now_add=True, verbose_name='create')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


# class UserBalanceChange(models.Model):
#     user = models.ForeignKey('User', related_name='balance_changes')
    # reason = models.IntegerField(choices=REASON_CHOICES, default=NO_REASON)
    # amount = models.DecimalField(_('Amount'), default=0, max_digits=18, decimal_places=6)
    # datetime = models.DateTimeField(_('date'), default=timezone.now)