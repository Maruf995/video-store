# Generated by Django 5.0.1 on 2024-01-30 04:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_category_remove_product_category_product_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категории', 'verbose_name_plural': 'Категории'},
        ),
        migrations.RenameField(
            model_name='popularsolutions',
            old_name='name',
            new_name='title',
        ),
    ]
