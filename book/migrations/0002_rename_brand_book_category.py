# Generated by Django 4.2.7 on 2023-12-30 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='brand',
            new_name='category',
        ),
    ]
