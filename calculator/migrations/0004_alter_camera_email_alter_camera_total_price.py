# Generated by Django 5.0.1 on 2024-02-08 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0003_alter_camera_email_alter_camera_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camera',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=254, verbose_name='Почта'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='camera',
            name='total_price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Итог'),
        ),
    ]
