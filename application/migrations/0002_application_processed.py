# Generated by Django 4.2.11 on 2024-04-07 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='processed',
            field=models.BooleanField(default=False),
        ),
    ]
