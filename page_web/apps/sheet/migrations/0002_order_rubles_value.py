# Generated by Django 4.0.5 on 2022-06-22 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='rubles_value',
            field=models.IntegerField(default=0, verbose_name='стоимость в руб.'),
        ),
    ]