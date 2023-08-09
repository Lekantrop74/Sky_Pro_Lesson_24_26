from django.db import models


# Create your models here.
class Car(models.Model):
    objects = None

    title = models.CharField(max_length=100, verbose_name='название')  # Поле для названия (максимум 100 символов)
    description = models.TextField(verbose_name='описание')  # Поле для описания (текстовое поле)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'


class Moto(models.Model):
    objects = None

    title = models.CharField(max_length=100, verbose_name='название')  # Поле для названия (максимум 100 символов)
    description = models.TextField(verbose_name='описание')  # Поле для описания (текстовое поле)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Мотоцикл'
        verbose_name_plural = 'Мотоциклы'
