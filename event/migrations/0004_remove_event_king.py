# Generated by Django 2.1.1 on 2018-09-28 06:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_auto_20180928_0314'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='king',
        ),
    ]
