# Generated by Django 5.0.1 on 2024-01-29 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ourworks',
            old_name='date_finis',
            new_name='date_finish',
        ),
    ]
