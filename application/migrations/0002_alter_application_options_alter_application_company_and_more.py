# Generated by Django 5.0.1 on 2024-01-08 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='application',
            options={'verbose_name': 'Заявки', 'verbose_name_plural': 'Заявки'},
        ),
        migrations.AlterField(
            model_name='application',
            name='company',
            field=models.CharField(max_length=20, verbose_name='Компания'),
        ),
        migrations.AlterField(
            model_name='application',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Почта'),
        ),
        migrations.AlterField(
            model_name='application',
            name='name',
            field=models.CharField(max_length=40, verbose_name='ФИО'),
        ),
        migrations.AlterField(
            model_name='application',
            name='number',
            field=models.IntegerField(verbose_name='Номер телефона'),
        ),
    ]