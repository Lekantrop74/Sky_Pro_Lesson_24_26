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


class Milage(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True, blank=True)
    moto = models.ForeignKey(Moto, on_delete=models.CASCADE, null=True, blank=True)

    milage = models.PositiveIntegerField(verbose_name='Пробег')
    year = models.PositiveSmallIntegerField(verbose_name='Год регистрации')

    def __str__(self):
        return f'{self.moto if self.moto else self.car} - {self.year}'

    class Meta:
        verbose_name = 'Пробег'
        verbose_name_plural = 'Пробег'
        ordering = ('-year',)
