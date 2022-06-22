from django.db import models


class Order(models.Model):
    position_number = models.BigAutoField(primary_key=True, verbose_name='№')
    order_number = models.IntegerField(verbose_name='Заказ №')
    dollar_value = models.IntegerField(verbose_name='Стоимость,$')
    delivery_time = models.DateField(verbose_name='Срок поставки')
    rubles_value = models.IntegerField(verbose_name='Стоимость в руб.', default=0)

    def __str__(self):
        return f'{self.position_number}'
