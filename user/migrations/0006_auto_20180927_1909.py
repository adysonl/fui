# Generated by Django 2.1 on 2018-09-27 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20180927_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_animal',
            name='photo',
            field=models.ImageField(default='clients_photos/default.jpg', upload_to='clients_photos/'),
        ),
    ]
