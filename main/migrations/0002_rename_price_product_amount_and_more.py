# Generated by Django 4.2.5 on 2023-09-12 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='amount',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='fruit',
            new_name='name',
        ),
    ]
