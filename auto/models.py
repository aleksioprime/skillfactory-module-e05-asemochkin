from django.db import models
from django.utils.translation import gettext as _

# Модель таблицы автомобилей
class Car(models.Model):
    TRANS = [
        (1, 'Механика'),
        (2, 'Автомат'),
        (3, 'Робот'),
    ]
    manufacturer = models.CharField(max_length=255,verbose_name=_("Производитель"))
    model = models.CharField(max_length=255,verbose_name=_("Модель"))
    year = models.IntegerField(verbose_name=_("Год выпуска"), null=True, blank=True)
    transmission = models.SmallIntegerField(choices=TRANS, default=1, null=True, blank=True)
    color = models.CharField(max_length=255,verbose_name=_("Цвет"), null=True, blank=True)
    class Meta:
            verbose_name = 'Автомобиль'
            verbose_name_plural = 'Автомобили'
            ordering = ['manufacturer', 'model']
    def __str__(self):
        return "{} {}".format(self.manufacturer, self.model)
